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

#first row 
for x in range (0,500, 125):
    c.create_rectangle(x, 0, x+62.5, 62.5, fill='grey')
    c.create_rectangle(x+62.5, 0, x+125, 62.5, fill='white')

#second row
for x in range (0, 500, 125):
    c.create_rectangle(x, 62.5, x+62.5, 125, fill='white')
    c.create_rectangle(x+62.5, 62.5, x+125, 125, fill='grey')

#third row
for x in range (0, 500, 125):
    c.create_rectangle(x, 125, x+62.5, 187.5, fill='grey')
    c.create_rectangle(x+62.5, 125, x+125, 187.5, fill='white')

#forth row
for x in range (0, 500, 125):
    c.create_rectangle(x, 187.5, x+62.5, 250, fill='white')
    c.create_rectangle(x+62.5, 187.5, x+125, 250, fill='grey')

#fifth row
for x in range (0, 500, 125):
    c.create_rectangle(x, 250, x+62.5, 312.5, fill='grey')
    c.create_rectangle(x+62.5, 250, x+125, 312.5, fill='white')

#sixth row
for x in range (0, 500, 125):
    c.create_rectangle(x, 312.5, x+62.5, 375, fill='white')
    c.create_rectangle(x+62.5, 312.5, x+125, 375, fill='grey')

#seventh row
for x in range (0, 500, 125):
    c.create_rectangle(x, 375, x+62.5, 437.5, fill='grey')
    c.create_rectangle(x+62.5, 375, x+125, 437.5, fill='white')

#eightth row
for x in range (0, 500, 125):
    c.create_rectangle(x, 437.5, x+62.5, 500, fill='white')
    c.create_rectangle(x+62.5, 437.50, x+125, 500, fill='grey')

#first row circles
for x in range (0, 500, 125):
    c.create_oval(x+5, 5, x+57.5, 57.5, fill='red')

#second row circles
for x in range (0, 500, 125):
    c.create_oval(x+67.5, 67.5, x+119.5, 119.5, fill='red')

#third row circles
for x in range (0, 500, 125):
    c.create_oval(x+5, 130, x+57.5, 182.5, fill='red')

#first row circles
for x in range (0, 500, 125):
    c.create_oval(x+67.5, 442.5, x+119.5, 495, fill='blue')

#second row circles
for x in range (0, 500, 125):
    c.create_oval(x+5, 380.5, x+57.5, 432.5, fill='blue')

#third row circles
for x in range (0, 500, 125):
    c.create_oval(x+67.5, 317.5, x+119.5, 370, fill='blue')

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
