from tkinter import *
#from tkinter import filedialog
root =Tk()
root.geometry

vertical= Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_Label = Label(root, text=horizontal.get()).pack()

def slide():
    my_Label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()