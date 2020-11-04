# from urllib.request import Request, urlopen

# r = Request('https://blufftonbeavers.com/sports/mgolf/2020-21/files/golf.htm')
# r.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'

# u = urlopen(r)
# content = u.read()

# with open('golf.htm', 'wb') as f:
#     f.write(content)

content = open('golf.htm').read()

content = content.split('Player Standings')[1]
content = content.split('Team-by-Team Results')[0]

numbers = []
lines = content.splitlines()
countdown = 0
for line in lines:
    if countdown > 0:
        countdown = countdown - 1
        if countdown == 0:
            if ';' in line:
                s = line.split(';')[1]
                s = s.split('<')[0]
                numbers.append(s)
    if line == '<tr>':
        countdown = 4

print(numbers)
