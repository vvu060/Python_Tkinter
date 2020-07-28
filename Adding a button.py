from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text="Button Clicked")
    myLabel.pack()

myButton = Button(root, text= "Click Me!", padx=40, fg="blue", bg='yellow', command = myClick) #state = Disabled
myButton.pack()
root.mainloop()