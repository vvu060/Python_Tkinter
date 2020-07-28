from tkinter import *
#from PIL import ImageTK, Image
root =Tk()

def open():
    global my_Label
    top = Toplevel()
    top.title("My New Window")
    #my_img = ImageTK.PhotoImage(Image.open())
    my_Lable = Label(top, text='Hello World').pack
    btn2 = Button(top, text='Close window', command=top.quit).pack()


btn = Button(root, text='Open Second window', command=open).pack()

mainloop()