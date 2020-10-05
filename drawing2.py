from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

# Put drawing here!
# c.create_rectangle(0, 0, 62.5, 62.5, fill='grey')
# c.create_rectangle(62.5, 0, 125, 62.5, fill='white')
# c.create_rectangle(125, 0, 187.5, 62.5, fill='grey')
# c.create_rectangle(187.5, 0, 250, 62.5, fill='white')
# c.create_rectangle(250, 0, 312.5, 62.5, fill='grey')
# c.create_rectangle(312.5, 0, 375, 62.5, fill='white')
# c.create_rectangle(375, 0, 437.5, 62.5, fill='grey')
# c.create_rectangle(437.5, 0, 500, 62.5, fill='white')

for x in (0, 125):
    c.create_rectangle(x, 0, x+62.5, 62.5, fill='grey')
    c.create_rectangle(x+62.5, 0, x+125, 62.5, fill='white')



for y in range(50, 500, 50):
    c.create_line(0, y, 500, y)
    c.create_text(18, y + 10, text=str(y))

for x in range(50, 500, 50):
    c.create_line(x, 0, x, 500)
    c.create_text(x + 18, 10, text=str(x))

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
