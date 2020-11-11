
from tkinter import Tk, Canvas, mainloop

SPEED = 10

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

# Put drawing here!
c.create_rectangle(0, 0, 500, 300, fill='blue')
c.create_rectangle(0, 300, 500, 500, fill='yellow')
c.create_rectangle(347, 380, 353, 450, fill='white')
c.create_polygon(350, 360, 400, 400, 300, 400, fill='green')
c.create_oval(80, 320, 140, 380, fill='white')
c.create_oval(85, 320, 135, 380, fill='blue')
c.create_oval(90, 320, 130, 380, fill='red')
c.create_oval(95, 320, 125, 380, fill='white')
c.create_oval(100, 320, 120, 380, fill='blue')
c.create_oval(105, 320, 115, 380, fill='red')
c.create_oval(109, 320, 111, 380, fill='white')
c.create_oval(440, 0, 550, 110, fill='yellow')
c.create_rectangle(0, 0, 505, 50, fill='light grey')

birds = [
    c.create_polygon(300, 175, 335, 200, 300, 185, 265, 200, fill='white'),
    c.create_polygon(165, 125, 200, 150, 165, 135, 130, 150, fill='white'),
]

def animate():
    # Make bird wings flap.

    if c.count % 5 == 0:
        for bird in birds:
            b = c.coords(bird)
            yc = (b[1] + b[5]) / 2
            for i in 3, 7:
                yw = b[i]
                if yw > yc:
                    b[i] = yc - 20
                else:
                    b[i] = yc + 20
            c.coords(bird, b)

    # Move missiles.
    for x, y, shape in missiles:
        coords = c.coords(shape)
        mx = coords[0]
        my = coords[1]
        dx = x - mx
        if dx > SPEED:
            dx = +SPEED
        elif dx < -SPEED:
            dx = -SPEED
        dy = y - my
        if dy > SPEED:
            dy = +SPEED
        elif dy < -SPEED:
            dy = -SPEED
        if dx == 0 and dy == 0:
            c.delete(shape)
        else:
            c.move(shape, dx, dy)

    root.after(42, animate)
    c.count = c.count + 1

c.count = 0
missiles = []
animate()

def launch_missile(event):
    missile = c.create_polygon(
        250,450, 245,455, 245,480, 240,485, 240,495, 245,490, 245,480, 245,490,
        255,490, 255,480, 255,490, 260,495, 260,485, 255,480, 255,455,
        fill='white', outline='black', width=3,
    )
    missiles.append([event.x, event.y, missile])

c.bind('<Button-1>', launch_missile)
mainloop()
