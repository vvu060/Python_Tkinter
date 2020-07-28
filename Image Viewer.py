from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image Viewer")
#root.iconbitmap('E:/Games/FIFA 14/Game/fifapc.ico')

my_img = ImageTk.PhotoImage(Image.open("F:/Photos/Friends/Manali 2018/IMG_5044.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("F:/Photos/Friends/Manali 2018/IMG_5047.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("F:/Photos/Friends/Manali 2018/IMG_5048.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("F:/Photos/Friends/Manali 2018/IMG_5057.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("F:/Photos/Friends/Manali 2018/IMG_5058.jpg"))

img_list = [my_img, my_img1, my_img2, my_img3, my_img4]


my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)



def button_forward(img_num):
    global my_label
    global buttton_forward
    global buttton_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])
    buttton_forward = Button(root,text='>>', command=lambda:button_forward(img_num+1))
    buttton_back = Button(root, text='<<', command=lambda:button_back(img_num - 1))

    if img_num == 5:
        buttton_forward=Button(root,text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    buttton_back.grid(row=1, column=0)
    buttton_forward.grid(row=1, column=2)

def button_back(img_num):
    global my_label
    global buttton_forward
    global buttton_back

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num - 1])
    buttton_forward = Button(root, text='>>', command=lambda: button_forward(img_num + 1))
    buttton_back = Button(root, text='<<', command=lambda: button_back(img_num - 1))

    if img_num == 1:
        buttton_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    buttton_back.grid(row=1, column=0)
    buttton_forward.grid(row=1, column=2)

buttton_back = Button(root, text='<<', command=button_back)
buttton_exit = Button(root, text='EXIT', command=root.quit)
buttton_forward = Button(root, text='>>', command=lambda :button_forward(2))

buttton_back.grid(row=1, column=0)
buttton_exit.grid(row=1, column=1)
buttton_forward.grid(row=1, column=2)

root.mainloop()



root.mainloop()