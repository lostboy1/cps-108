import ast
import json
import linecache
import re
import traceback
from builtins import __import__  # for use when we patch it in "builtins"
from difflib import SequenceMatcher
from functools import partial
from unittest.mock import patch

from IPython.display import HTML
from ipykernel.ipkernel import IPythonKernel
from nbconvert.filters.ansi import ansi2html

BOOT = """\
%load_ext autoreload
%autoreload 2
"""

LESSON_NUMBER = 1

def start_lesson(lesson_number):
    global LESSON_NUMBER
    take_over_control()
    LESSON_NUMBER = lesson_number
    print(green(embox('Welcome to lesson {}'.format(lesson_number))), end='')

def take_over_control():
    if hasattr(IPythonKernel, '_original_do_execute'):
        return
    IPythonKernel._original_do_execute = IPythonKernel.do_execute
    IPythonKernel._booted = False
    IPythonKernel.do_execute = replacement_do_execute

def replacement_do_execute(self, code, silent, store_history=True,
                           user_expressions=None, allow_stdin=False):
    # with open('/tmp/tmp', 'w') as f:
    #     f.write(output)
    if not self._booted:
        self._original_do_execute(BOOT, True, False)
        self._booted = True
    code = '__import__("course_engine").run({!r})'.format(code)
    return self._original_do_execute(code, silent, store_history,
                                     user_expressions, allow_stdin)

def parse_exercise_number(source):
    words = source.split(None, 3)
    if len(words) >= 3 and words[0:2] == ['#', 'Exercise']:
        return words[2]
    return None

def run(source):
    number = parse_exercise_number(source)
    if number is None:
        return run_non_exercise(source)
    else:
        return run_exercise(number, source)

def run_non_exercise(source):
    run_code('Notebook cell', source)
    metadata = read_notebook_metadata(LESSON_NUMBER)
    if 'start_lesson' not in source and len(metadata) > 0:
        print()
        print(embox('Note: without an “# Exercise” number comment,',
                    'a cell cannot be given specific feedback.'))

STYLE_DICT = {
    'ansi-red-fg': 'color: red',
    'ansi-red-intense-fg': 'color: red',
    'ansi-bold': 'font-weight: bold',
    'ansi-green-fg': 'color: #4f4',
    'ansi-green-intense-fg': 'color: #4f4',
    'ansi-yellow-fg': 'color: #ff2',
}

def run_exercise(number, source):
    """Workaround for bug in VS Code.

    For details, see: https://github.com/microsoft/vscode/issues/104446

    """
    output_strings = []
    def wrapped_write(string):
        output_strings.append(string)
    with patch('sys.stdout.write', wrapped_write):
        _run_exercise(number, source)
    output = ''.join(output_strings)
    output = ansi2html(output)
    def color_span(match):
        styles = [STYLE_DICT[class_name] for class_name in match[1].split(' ')]
        return match[0] + f' style="{";".join(styles)}"'
    output = re.sub(r'<span class="([^"]*)"', color_span, output)
    output = f'<pre>{output}</pre>'
    # output = '\n'.join(output_strings)
    # with open('/tmp/tmp', 'w') as f:
    #     f.write(output)
    return HTML(output)

def _run_exercise(number, source):
    output_strings = []
    #real_write = sys.stdout.write
    def wrapped_write(string):
        output_strings.append(string)
        #real_write(string)

    name = 'Exercise {}'.format(number)
    with patch('sys.stdout.write', wrapped_write):
        result, local_scope, modules_imported = run_code(name, source)

    output = ''.join(output_strings)

    if result != 'successful':
        print(output)
        return  # If it printed an exception, make no further complaints

    metadata = read_notebook_metadata(LESSON_NUMBER).get(number)
    if metadata is None:
        print(yellow(embox(f'Alas, there is no exercise “{number}”.')))
        return

    verdicts = []

    if 'expected' in metadata:
        expected = metadata['expected']
        if output != expected:
            output, expected = festoon_diff(output, expected)
            print(output)
            print(red(embox('Your output does not quite match',
                            'what the exercise is expecting:')))
            print(expected)
            return
        else:
            print(output)
            verdicts.append((True, 'Your output looks correct'))
    else:
        print(output)

    def demand(source, message):
        true_or_false = eval(source, {}, local_scope)
        verdicts.append((true_or_false, message))

    def forbid_importing(name):
        message = f'You should avoid using the {name} module'
        verdict = name not in modules_imported, message
        verdicts.append(verdict)

    def needs(code_pattern, message):
        tree = compile(source, '', 'exec', flags=ast.PyCF_ONLY_AST)
        pattern = compile(code_pattern, '', 'exec', flags=ast.PyCF_ONLY_AST)
        verdict = search_ast(tree, pattern), message
        verdicts.append(verdict)

    texts = []
    color = green

    if 'checks' in metadata:
        checks = metadata['checks']
        compiled = compile(checks, 'checks', 'exec')
        eval(compiled)
        success = all(good for good, message in verdicts)
        color = green if success else yellow
        texts = [
            green('✔ ' + message) if good else yellow('  ' + message)
            for good, message in verdicts
        ]
    else:
        success = True

    if success:
        texts.extend(['', 'Good job! You have completed this exercise'])

    print(color(embox(*texts)))

def run_code(name, source):
    """Run ``source``, tracking imports and printing pretty tracebacks."""
    lines = source.splitlines(True)
    linecache.cache[name] = len(source), None, lines, name

    def wrapped_import(name, *args, **kw):
        modules_imported.append(name)
        return __import__(name, *args, **kw)

    local_scope = {}
    modules_imported = []

    try:
        compiled = compile(source, name, 'exec')
        with patch('builtins.__import__', wrapped_import):
            eval(compiled, {}, local_scope)
    except Exception:
        lines = traceback.format_exc().splitlines()
        lines[0] = yellow(lines[0])    # Line that says "Traceback"
        lines[-1] = yellow(lines[-1])  # Hopefully the exception itself
        print('\n'.join(lines))
        return 'exception', local_scope, modules_imported
    else:
        return 'successful', local_scope, modules_imported
    finally:
        del linecache.cache[name]

def read_notebook_metadata(lesson_number):
    filename = f'lesson-{lesson_number:02}.ipynb'
    with open(filename) as f:
        notebook = json.load(f)
    return {
        str(cell['metadata']['exercise_number']): cell['metadata']
        for cell in notebook['cells']
        if 'exercise_number' in cell['metadata']
    }

def festoon_diff(a, b):
    """Return strings ``a`` and ``b``, marking their differences."""
    sm = SequenceMatcher(a=a, b=b, autojunk=False)
    blocks = sm.get_matching_blocks()
    a_blocks = [(a, size) for a, b, size in blocks]
    b_blocks = [(b, size) for a, b, size in blocks]
    festooned_a = festoon_text(a, a_blocks, extra_text_color, end_color)
    festooned_b = festoon_text(b, b_blocks, missing_text_color, end_color)
    return festooned_a, festooned_b

def festoon_text(text, blocks, start_color, end_color):
    """Return ``text`` with text outside the ``blocks`` marked with color."""
    pieces = []
    i = 0
    for j, size in blocks:
        if j > i:
            pieces.append(start_color)
            pieces.append(text[i:j]) #.replace('\n', '↲\n'))
            pieces.append(end_color)
        i = j + size
        pieces.append(text[j:i])
    return ''.join(pieces)

def search_ast(tree, pattern):
    """Search the ``tree`` for a subtree matching the ``pattern``."""
    pattern = pattern.body[0]
    for node in ast.walk(tree):
        if match_ast(node, pattern):
            return True
    return False

def match_ast(tree, pattern):
    """Determine whether ``tree`` matches the given ``pattern``.

    The ``pattern`` should be a small AST.  Everything in the ``tree``
    needs to match the ``pattern``, except where the ``pattern`` has a
    wildcard: an expression that's the lone name ``X``.

    """
    if is_wildcard(pattern):
        return True
    if type(tree) is not type(pattern):
        return False
    for field in tree._fields:
        t = getattr(tree, field)
        p = getattr(pattern, field)
        if isinstance(t, ast.AST):
            if not match_ast(t, p):
                return False
        elif isinstance(t, list):
            if not is_wildcard_block(p):
                for ti, pi in zip(t, p):
                    if not match_ast(ti, pi):
                        return False
        else:
            if t != p:
                return False
    return True

def is_wildcard(pattern):
    """Whether an AST node is the name ``X``."""
    return isinstance(pattern, ast.Name) and pattern.id == 'X'

def is_wildcard_block(pattern):
    """Whether a list of AST nodes is a single name ``X``."""
    return (len(pattern) == 1 and isinstance(pattern[0], ast.Expr)
            and is_wildcard(pattern[0].value))

def embox(*lines):
    """Return ``lines`` of text with a pretty box drawn around them."""
    length = max(width_of(line) for line in lines)
    pieces = ['┌', '─' * (length + 2), '┐\n']
    for line in lines:
        pieces.extend(['│ ', line + ' ' * (length - width_of(line)), ' │\n'])
    pieces.extend(['└', '─' * (length + 2), '┘'])
    return ''.join(pieces)

def width_of(text):
    """Return the width of `text`, ignoring ANSI color code sequences."""
    return len(re.sub(r'\033.*?m', '', text))

def colorize(color, text):
    """Give ``text`` a color, without overwriting any existing colors in it."""
    start = '\033[{}m'.format(color)
    text = text.replace(end_color, start)
    return '{}{}{}'.format(start, text, end_color)

end_color = '\033[0m'
red = partial(colorize, 31)
green = partial(colorize, 32)
yellow = partial(colorize, 33)
extra_text_color = '\033[1;31m'
missing_text_color = '\033[1;32m'
