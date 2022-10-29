import sqlite3 as sql
from tkinter import *
from random import choices
import bcrypt
from tkinter import messagebox

root = Tk()
root.title("Log In")

database = sql.connect("Passwords.db")
cursor = database.cursor()
btns_to_delete = []
everything = list(
    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&²()*+,-./:;<=>?@[]^_`{|}~"
)
cursor.execute("CREATE TABLE IF NOT EXISTS Pass ( Pswrd )")
elements = []
cursor.execute("CREATE TABLE IF NOT EXISTS Passwords (Passwrd , Website)")
cursor.execute("SELECT oid, * FROM Pass")
valid = cursor.fetchall()


def sub():
    global access
    global root1

    check = pas.get()
    if bcrypt.checkpw(bytes(check.encode("utf-8")), bytes(valid[0][1])):
        messagebox.showinfo("correct!", "Correct Password!")
        root.destroy()
        root1 = Tk()
        root1.title("Password Manager")
        option = IntVar()
        option.set(0)

        selection = Radiobutton(root1,
                                text="Show Passwords",
                                variable=option,
                                value=0,
                                command=Show)
        selection.grid(row=0, column=1)

        selection2 = Radiobutton(root1,
                                 text="Create New Password",
                                 variable=option,
                                 value=1,
                                 command=Create)
        selection2.grid(row=1, column=1)

        selection3 = Radiobutton(root1,
                                 text="Delete Password",
                                 variable=option,
                                 value=2,
                                 command=Delete)
        selection3.grid(row=2, column=1)

        root1.columnconfigure(0, minsize=150)
        root1.columnconfigure(1, minsize=150)
        root1.columnconfigure(2, minsize=150)

        root1.mainloop()
    else:
        messagebox.showwarning("incorrect password", "incorrect password!")


if valid == []:
    root.title("Sign Up")

    def new():
        passs = pas.get()
        encoded_pass = passs.encode("utf-8")
        enc_pass = bcrypt.hashpw(encoded_pass, bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO Pass (Pswrd) VALUES (:enc_pass)",
            {
                "enc_pass": enc_pass,
            },
        )
        database.commit()
        root.quit()

    newind = Label(
        root,
        text="it looks like you dont have a password please create a new one")
    newind.grid(row=0, column=1)

    frame = LabelFrame(root, text="Enter your new password")
    frame.grid(row=1, column=1, padx=30, pady=10)

    pas = Entry(frame)
    pas.grid(row=0, column=1)

    submit = Button(frame, text="Submit", command=new)
    submit.grid(row=1, column=1)

else:
    frame = LabelFrame(root, text="Enter your password")
    frame.grid(row=0, column=1, padx=30, pady=10)

    pas = Entry(frame)
    pas.grid(row=0, column=1)

    submit = Button(frame, text="Submit", command=sub)
    submit.grid(row=1, column=1)

    def forgor():
        yn = messagebox.askyesno(
            "password reset", "Are You Sure You Want To Reset Your Password")
        if yn == 1:
            cursor.execute("DELETE FROM Pass WHERE oid = 1")
            database.commit()
            root.quit()
        else:
            pass

    forgot = Button(root, text="i forgor :skull:", command=forgor)
    forgot.grid(row=1, column=1)


def Show():
    for i in btns_to_delete:
        i.grid_forget()
    db = sql.connect("Passwords.db")
    crsr = db.cursor()
    crsr.execute("SELECT * FROM Passwords")
    x = crsr.fetchall()
    corr = ""
    for peb in x:
        corr += peb[0] + " - " + peb[1] + "\n"

    la = Label(root1, text=corr)
    la.grid(row=3, column=1)

    btns_to_delete.append(la)


def chars():
    global choilab

    a = int(paschars.get())
    choi = choices(everything, k=a)
    elements.insert(0, "".join(choi))
    choilab = Label(amnchr, text=str("".join(choi)))
    choilab.grid(row=2, column=0, columnspan=3)

    btns_to_delete.append(choilab)


def web():
    elements.insert(1, wbsite.get())


def Add():
    db = sql.connect("Passwords.db")
    crsr = db.cursor()
    web = wbsite.get()
    choi = choilab.cget("text")
    crsr.execute(
        "INSERT INTO Passwords(Passwrd , Website) VALUES (:web, :choi)",
        {
            "web": web,
            "choi": choi
        },
    )
    labpas = Label(root1,
                   text="succesfully added " + str(choi) + " - " + str(web))
    labpas.grid(row=11, column=1)
    db.commit()
    db.close()
    btns_to_delete.append(labpas)


def Create():
    global paschars
    global amnchr
    global wbsite

    for i in btns_to_delete:
        i.grid_forget()

    amnchr = LabelFrame(root1, text="how many characters should be generated")
    amnchr.grid(row=3, column=1)

    amnchr.columnconfigure(0, minsize=60)
    paschars = Entry(amnchr)
    paschars.grid(row=0, column=1)

    smit = Button(amnchr, text="Submit", command=chars)
    smit.grid(row=1, column=1)

    fram = LabelFrame(root1, text="the website for the password")
    fram.grid(row=4, column=1)

    wbsite = Entry(fram)
    wbsite.grid(row=0, column=1)

    smitwb = Button(fram, text="Submit", command=web)
    smitwb.grid(row=1, column=1)

    Save = Button(root1, text="Add Password", command=Add)
    Save.grid(row=5, column=1)

    btns_to_delete.extend((paschars, amnchr, smit, fram, wbsite, Save, smitwb))


def select():
    id0 = slct.get()
    db = sql.connect("Passwords.db")
    crsr = db.cursor()
    crsr.execute("DELETE FROM Passwords WHERE oid =" + id0)
    db.commit()

    successlabel = Label(root1, text="Password succesfully deleted!")
    successlabel.grid(row=10, column=1)

    btns_to_delete.append(successlabel)


def Delete():
    global slct

    for i in btns_to_delete:
        i.grid_forget()

    slct = Entry(root1)
    slct.grid(row=3, column=1)

    slcbtn = Button(root1, text="select element", command=select)
    slcbtn.grid(row=4, column=1)

    db = sql.connect("Passwords.db")
    crsr = db.cursor()
    crsr.execute("SELECT oid,* FROM Passwords")
    o = crsr.fetchall()
    elem = ""
    for element in o:
        elem += str(element[0]) + "  " + element[1] + " - " + element[2] + "\n"

    elabel = Label(root1, text=elem)
    elabel.grid(row=9, column=1)

    btns_to_delete.extend((elabel, slct, slcbtn))


root.mainloop()
