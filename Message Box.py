from tkinter import *
from tkinter import messagebox

root = Tk()

#showinfo, showerror, showwarning, askquestion, askocancel, askyesno
def popup():
    response = messagebox.askyesno("This is a popup", "Hello World")
    Label(root, text= response).pack()
    if response==1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()

Button(root, text='popup', command=popup).pack()

root.mainloop()