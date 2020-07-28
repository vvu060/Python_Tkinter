from tkinter import *
#from tkinter import filedialog
root =Tk()

def show():
    my_Label = Label(root, text=var.get()).pack()
var = StringVar()
c= Checkbutton(root, text="Check Me", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


my_Button = Button(root, text="Show Selection", command=show).pack()

root.mainloop()