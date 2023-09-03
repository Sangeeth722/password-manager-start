from tkinter import *


# You can also use additional options like rowspan and columnspan to
# specify how many rows or columns a widget should span.

window = Tk()

r = Label(bg="red", width=50, height=5)
r.grid(row=0, column=0,columnspan=2)

g = Label(bg="green", width = 50, height=5)
g.grid(row=1, column=1,columnspan=1)

b = Label(bg="blue", width=50, height=5)
b.grid(row=2, column=0, columnspan = 2)


window.mainloop()