from tkinter import *

window = Tk()

window.title("Nathan's Button")

icon = 'med.ico'
window.iconbitmap(icon)


# making the object
b1 = Button(text = "Click Me!", height=100,width=200)

# placing the object
b1.grid(row = 0, column = 0)

window.mainloop()