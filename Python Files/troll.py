from tkinter import *
from random import choice
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap(
    "@/home/walid/Coding/Python Files/images/troll/91df39a49ca139681e4914a6eff15d7b.xbm"
)
root.title("le trollage")
root.configure(bg="white")
num_list = [0, 1, 2]

img = ImageTk.PhotoImage(
    Image.open("images/troll/4-42120_bleed-area-may-not-be-visible-meme-troll.jpg")
)
back = Label(root, image=img)
back.place(x=0, y=0, relwidth=1, relheight=1)


def ran():
    global ann2

    ran_num1 = choice(num_list)
    ran_num2 = choice(num_list)
    c = ann2.grid_info()["column"]
    r = ann2.grid_info()["row"]
    if ran_num1 + ran_num2 == c + r:
        while ran_num1 + ran_num2 == c + r:
            ran_num1 = choice(num_list)
            ran_num2 = choice(num_list)
    ann2.grid_forget()
    ann2 = Button(root, padx=25, pady=10, text="Click me!", command=ran)
    ann2.grid(row=ran_num1, column=ran_num2)


ann2 = Button(root, padx=25, pady=10, text="Click me!", command=ran)
ann2.grid(row=1, column=1)

root.rowconfigure(0, minsize=140)
root.columnconfigure(0, minsize=140)
root.rowconfigure(1, minsize=180)
root.columnconfigure(1, minsize=140)
root.rowconfigure(2, minsize=180)
root.columnconfigure(2, minsize=140)


root.mainloop()
