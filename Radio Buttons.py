from tkinter import *

root = Tk()
root.title("Radio Buttons")

#r = IntVar()
#r.set("2")

Toppings = [
    ("Chicken", "Chicken"),
    ("Lamb", "Lamb"),
    ("Egg", "Egg"),
    ("Veggies", "Veggies"),
]

pizza = StringVar()
pizza.set("Chicken")

for text, topping in Toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor =W)

def clicked(value):
    myLable = Label(root, text=value)
    myLable.pack()

#Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda :clicked(r.get())).pack()
#Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda :clicked(r.get())).pack()

#myLable = Label(root, text=pizza.get())
#myLable.pack()

myButton = Button(root, text="Clicl Me!", command=lambda :clicked(pizza.get()))
myButton.pack()
root.mainloop()
