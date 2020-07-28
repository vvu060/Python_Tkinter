from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Fifa 14")
root.iconbitmap('E:/Games/FIFA 14/Game/fifapc.ico')

my_img = ImageTk.PhotoImage(Image.open("C:/Users/Vishal/Downloads/download"))
my_label = Label(image=my_img)
my_label.pack()





button_quit = Button(root, text="Exit", command=root.quit())
button_quit.pack()

root.mainloop()