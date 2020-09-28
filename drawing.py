from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

# Put drawing here!
c.create_rectangle(0, 0, 500, 350, fill='blue')
c.create_rectangle(0, 350, 500, 500, fill='green')
c.create_rectangle(150, 150, 350, 400, fill='red')
c.create_rectangle(175, 50, 225, 125, fill='red')
c.create_rectangle(200, 250, 300, 400, fill='brown')
c.create_polygon(150, 150, 250, 50, 350, 150, fill='green')
c.create_oval(350, 50, 500, 150, fill='white')

#draw grid
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
