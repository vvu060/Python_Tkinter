from tkinter import *
#from tkinter import filedialog
root =Tk()

def show():
    my_Label = Label(root, text=clicked.get()).pack()

options= [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_Button = Button(root, text="Show Selection", command=show).pack()

root.mainloop()