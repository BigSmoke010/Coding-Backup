from tkinter import *
from random import choice
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("XO")
background_image = ImageTk.PhotoImage(
    Image.open(r"images/XO/XO1.png")
)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# TODO:
# change the background everytime someone wins

opscore = 0
userscore = 0
win = False
winbot = False
winplyr = False

usscore = Label(root, text=userscore, fg="#938D9C")
usscore.grid(row=4, column=0)

opsscore = Label(root, text=opscore, fg="#938D9C")
opsscore.grid(row=4, column=2)

bet = Label(root, text="-", bg="white")
bet.grid(row=4, column=1)

tu = [1, 0]
role = input("X or O :")
turn = choice(tu)

if role == "x":
    oprole = "O"
    print(f"you are {role.upper()} and your opponent is {oprole}")
elif role == "o":
    oprole = "X"
    print(f"you are {role.upper()} and your opponent is {oprole}")
else:
    print("invalid input")
    exit(0)


def clear():
    global tl
    global t
    global tr
    global ml
    global m
    global mr
    global bl
    global b
    global br
    global turn
    global vs1
    global usedbtns
    global usedbbtns
    global ref
    global btns_to_delete
    global vs
    global opsscore
    global usscore
    global opscore
    global userscore
    global cho
    global usedpbtns

    vs = [
        tl,
        t,
        tr,
        ml,
        m,
        mr,
        bl,
        b,
        br,
    ]

    for button in btns_to_delete:
        button.grid_forget()

    for x in vs:
        x.grid_forget()

    if userscore < opscore:
        opsscore.grid_forget()
        opsscore = Label(root, text=opscore, fg="#38D523", bg="white")
        opsscore.grid(row=4, column=2)
        opsscore.configure(font="Verdana 15 underline")
        usscore.grid_forget()
        usscore = Label(root, text=userscore, fg="#A30000", bg="white")
        usscore.grid(row=4, column=0)
    elif userscore > opscore:
        opsscore.grid_forget()
        opsscore = Label(root, text=opscore, fg="#A30000", bg="white")
        opsscore.grid(row=4, column=2)
        usscore.grid_forget()
        usscore = Label(root, text=userscore, fg="#38D523", bg="white")
        usscore.grid(row=4, column=0)
        usscore.configure(font="Verdana 15 underline")

    cho = Button(root, text="bot", command=chose)
    cho.grid(row=0, column=0)

    tl = Button(
        root,
        text="...",
        command=lambda var="tl", a=1, b=0: [click(var, a, b), scndplyr(var, a, b)],
    )
    tl.grid(row=1, column=0)
    t = Button(
        root,
        text="...",
        command=lambda var="t", a=1, b=1: [click(var, a, b), scndplyr(var, a, b)],
    )
    t.grid(row=1, column=1)
    tr = Button(
        root,
        text="...",
        command=lambda var="tr", a=1, b=2: [click(var, a, b), scndplyr(var, a, b)],
    )
    tr.grid(row=1, column=2)
    ml = Button(
        root,
        text="...",
        command=lambda var="ml", a=2, b=0: [click(var, a, b), scndplyr(var, a, b)],
    )
    ml.grid(row=2, column=0)
    m = Button(
        root,
        text="...",
        command=lambda var="m", a=2, b=1: [click(var, a, b), scndplyr(var, a, b)],
    )
    m.grid(row=2, column=1)
    mr = Button(
        root,
        text="...",
        command=lambda var="mr", a=2, b=2: [click(var, a, b), scndplyr(var, a, b)],
    )
    mr.grid(row=2, column=2)
    bl = Button(
        root,
        text="...",
        command=lambda var="bl", a=3, b=0: [click(var, a, b), scndplyr(var, a, b)],
    )
    bl.grid(row=3, column=0)
    b = Button(
        root,
        text="...",
        command=lambda var="b", a=3, b=1: [click(var, a, b), scndplyr(var, a, b)],
    )
    b.grid(row=3, column=1)
    br = Button(
        root,
        text="...",
        command=lambda var="br", a=3, b=2: [click(var, a, b), scndplyr(var, a, b)],
    )
    br.grid(row=3, column=2)

    clr = Button(root, text="clear", command=clear)
    clr.grid(row=0, column=2)

    ref = [
        ("tl", tl),
        ("t", t),
        ("tr", tr),
        ("ml", ml),
        ("m", m),
        ("mr", mr),
        ("bl", bl),
        ("b", b),
        ("br", br),
    ]

    vs1 = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]

    vs = [
        tl,
        t,
        tr,
        ml,
        m,
        mr,
        bl,
        b,
        br,
    ]

    btns_to_delete = []
    usedbtns = []
    usedbbtns = []
    usedpbtns = []


def click(v, r, c):
    global turn
    global userscore
    global usscore
    global opsscore

    if turn == 1:
        for name, var in ref:
            if name == v:
                btn = var
                a = (name, var)

        for i in ref:
            if i == a:
                ind = ref.index(i)

        usedbtns.append(btn)

        btn.grid_forget()
        btn = Button(root, text=role.upper())
        btn.grid(row=r, column=c)
        btns_to_delete.append(btn)
        vs[ind] = " "
        vs1[ind] = " "
        turn = 0
        win = False

        if tl in usedbtns and m in usedbtns and br in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True

        elif t in usedbtns and m in usedbtns and b in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True

        elif tr in usedbtns and mr in usedbtns and br in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True

        elif tl in usedbtns and ml in usedbtns and bl in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)

        elif tr in usedbtns and m in usedbtns and bl in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True

        elif tl in usedbtns and t in usedbtns and tr in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True
        elif ml in usedbtns and m in usedbtns and mr in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True
        elif bl in usedbtns and b in usedbtns and br in usedbtns and not win:
            messagebox.showinfo("we have a winner!", "you won!")
            userscore += 1
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#938D9C")
            usscore.grid(row=4, column=0)
            win = True
        elif set(vs) == {" "} and not winbot:
            messagebox.showinfo("sadly, we have no winner :(", "draw!")

        if userscore < opscore:
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#38D523", bg="white")
            opsscore.grid(row=4, column=2)
            opsscore.configure(font="Verdana 15 underline")
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#A30000", bg="white")
            usscore.grid(row=4, column=0)
        elif userscore > opscore:
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#A30000", bg="white")
            opsscore.grid(row=4, column=2)
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#38D523", bg="white")
            usscore.grid(row=4, column=0)
            usscore.configure(font="Verdana 15 underline")


def chose():
    global turn
    global opscore
    global opsscore
    global usscore

    if turn == 0 and mode.get() == 0:

        ranchoice = choice(vs)

        if ranchoice == " ":
            while ranchoice == " ":
                ranchoice = choice(vs)

        lis = []
        ind = vs.index(ranchoice)

        for x in vs1[ind]:
            lis.append(x)

        usedbbtns.append(ranchoice)

        ranchoice.grid_forget()
        ranchoice = Button(root, text=oprole)
        ranchoice.grid(row=lis[0], column=lis[1])
        btns_to_delete.append(ranchoice)
        turn = 1
        lis.clear()

        vs[ind] = " "
        vs1[ind] = " "
        winbot = False

        if tl in usedbbtns and m in usedbbtns and br in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif t in usedbbtns and m in usedbbtns and b in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif tr in usedbbtns and mr in usedbbtns and br in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif tl in usedbbtns and ml in usedbbtns and bl in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif tr in usedbbtns and m in usedbbtns and bl in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif tl in usedbbtns and t in usedbbtns and tr in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif ml in usedbbtns and m in usedbbtns and mr in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif bl in usedbbtns and b in usedbbtns and br in usedbbtns and not winbot:
            messagebox.showinfo("we have a winner!", "bot won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winbot = True
        elif set(vs) == " " and not winbot:
            messagebox.showinfo("sadly, we have no winner :(", "draw!")

        if userscore < opscore:
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#38D523", bg="white")
            opsscore.grid(row=4, column=2)
            opsscore.configure(font="Verdana 15 underline")
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#A30000", bg="white")
            usscore.grid(row=4, column=0)
        elif userscore > opscore:
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#A30000", bg="white")
            opsscore.grid(row=4, column=2)
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#38D523", bg="white")
            usscore.grid(row=4, column=0)
            usscore.configure(font="Verdana 15 underline")
        elif set(vs) == {" "} and not winbot:
            messagebox.showinfo("sadly, we have no winner :(", "draw!")
    else:
        pass


def scndplyr(v, r, c):
    global turn
    global opscore
    global opsscore
    global usscore

    if turn == 0 and mode.get() == 1:
        for name, var in ref:
            if name == v:
                btn = var
                global a
                a = (name, var)

        for i in ref:
            if i == a:
                ind = ref.index(i)

        usedpbtns.append(btn)

        btn.grid_forget()
        btn = Button(root, text=oprole.upper())
        btn.grid(row=r, column=c)
        btns_to_delete.append(btn)
        vs[ind] = " "
        vs1[ind] = " "
        turn = 1
        winplyr = False

        if tl in usedpbtns and m in usedpbtns and br in usedpbtns and not winbot:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True

        elif t in usedpbtns and m in usedpbtns and b in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True

        elif tr in usedpbtns and mr in usedpbtns and br in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True

        elif tl in usedpbtns and ml in usedpbtns and bl in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)

        elif tr in usedpbtns and m in usedpbtns and bl in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True

        elif tl in usedpbtns and t in usedpbtns and tr in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True
        elif ml in usedpbtns and m in usedpbtns and mr in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True
        elif bl in usedpbtns and b in usedpbtns and br in usedpbtns and not winplyr:
            messagebox.showinfo("we have a winner!", "2nd player won!")
            opscore += 1
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#938D9C")
            opsscore.grid(row=4, column=2)
            winplyr = True
        elif set(vs) == {" "} and not winbot:
            messagebox.showinfo("sadly, we have no winner :(", "draw!")

        if userscore < opscore:
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#38D523", bg="white")
            opsscore.grid(row=4, column=2)
            opsscore.configure(font="Verdana 15 underline")
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#A30000", bg="white")
            usscore.grid(row=4, column=0)
        elif userscore > opscore:
            opsscore.grid_forget()
            opsscore = Label(root, text=opscore, fg="#A30000", bg="white")
            opsscore.grid(row=4, column=2)
            usscore.grid_forget()
            usscore = Label(root, text=userscore, fg="#38D523", bg="white")
            usscore.grid(row=4, column=0)
            usscore.configure(font="Verdana 15 underline")


usedbtns = []
usedbbtns = []
usedpbtns = []

root.columnconfigure(0, minsize=100)
root.rowconfigure(1, minsize=100)
root.columnconfigure(1, minsize=100)
root.rowconfigure(2, minsize=100)
root.columnconfigure(2, minsize=100)
root.rowconfigure(3, minsize=100)

cho = Button(root, text="bot", command=chose)
cho.grid(row=0, column=0)

tl = Button(
    root,
    text="...",
    command=lambda var="tl", a=1, b=0: [click(var, a, b), scndplyr(var, a, b)],
)
tl.grid(row=1, column=0)
t = Button(
    root,
    text="...",
    command=lambda var="t", a=1, b=1: [click(var, a, b), scndplyr(var, a, b)],
)
t.grid(row=1, column=1)
tr = Button(
    root,
    text="...",
    command=lambda var="tr", a=1, b=2: [click(var, a, b), scndplyr(var, a, b)],
)
tr.grid(row=1, column=2)
ml = Button(
    root,
    text="...",
    command=lambda var="ml", a=2, b=0: [click(var, a, b), scndplyr(var, a, b)],
)
ml.grid(row=2, column=0)
m = Button(
    root,
    text="...",
    command=lambda var="m", a=2, b=1: [click(var, a, b), scndplyr(var, a, b)],
)
m.grid(row=2, column=1)
mr = Button(
    root,
    text="...",
    command=lambda var="mr", a=2, b=2: [click(var, a, b), scndplyr(var, a, b)],
)
mr.grid(row=2, column=2)
bl = Button(
    root,
    text="...",
    command=lambda var="bl", a=3, b=0: [click(var, a, b), scndplyr(var, a, b)],
)
bl.grid(row=3, column=0)
b = Button(
    root,
    text="...",
    command=lambda var="b", a=3, b=1: [click(var, a, b), scndplyr(var, a, b)],
)
b.grid(row=3, column=1)
br = Button(
    root,
    text="...",
    command=lambda var="br", a=3, b=2: [click(var, a, b), scndplyr(var, a, b)],
)
br.grid(row=3, column=2)


clr = Button(root, text="clear", command=clear)
clr.grid(row=0, column=2)

mode = IntVar()
twop = Checkbutton(root, text="2nd player turn", variable=mode)
twop.grid(row=5, column=1)

ref = [
    ("tl", tl),
    ("t", t),
    ("tr", tr),
    ("ml", ml),
    ("m", m),
    ("mr", mr),
    ("bl", bl),
    ("b", b),
    ("br", br),
]

vs1 = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]

vs = [
    tl,
    t,
    tr,
    ml,
    m,
    mr,
    bl,
    b,
    br,
]
btns_to_delete = []

root.mainloop()
