from tkinter import *
root = Tk()
e = Entry(root, width = 40, borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text= "Click Me!", padx=40, fg="blue", bg='yellow', command = myClick) #state = Disabled
myButton.pack()
root.mainloop()