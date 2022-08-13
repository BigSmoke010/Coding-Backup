from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("230x490+550+200")
root.configure(background="#511414")


def plus():
    global fst_num
    global operation

    oprator_list = [
        ("+", plus, 5, 0, 1, 27, DISABLED),
        ("-", minus, 5, 1, 1, 29, DISABLED),
        ("/", division, 5, 2, 1, 29, DISABLED),
        ("x", multiply, 6, 0, 1, 27, DISABLED),
        ("clear", clear, 4, 0, 2, 50, None),
        ("=", equal, 6, 2, 1, 27, DISABLED),
        ("√", sqrt, 1, 4, 1, 25, None),
        (".", comma, 6, 1, 1, 29, None),
    ]
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=state
        ).grid(row=row, column=column, columnspan=columnspan)
    operation = "addition"
    fst_num = output.get()
    output.delete(0, "end")
    output.insert(0, "+")


def minus():
    global fst_num
    global operation
    oprator_list = [
        ("+", plus, 5, 0, 1, 27, DISABLED),
        ("-", minus, 5, 1, 1, 29, DISABLED),
        ("/", division, 5, 2, 1, 29, DISABLED),
        ("x", multiply, 6, 0, 1, 27, DISABLED),
        ("clear", clear, 4, 0, 2, 50, None),
        ("=", equal, 6, 2, 1, 27, DISABLED),
        ("√", sqrt, 1, 4, 1, 25, None),
        (".", comma, 6, 1, 1, 29, None),
    ]
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=state
        ).grid(row=row, column=column, columnspan=columnspan)
    operation = "minus"
    fst_num = output.get()
    output.delete(0, "end")
    output.insert(0, "-")


def multiply():
    global fst_num
    global operation

    oprator_list = [
        ("+", plus, 5, 0, 1, 27, DISABLED),
        ("-", minus, 5, 1, 1, 29, DISABLED),
        ("/", division, 5, 2, 1, 29, DISABLED),
        ("x", multiply, 6, 0, 1, 27, DISABLED),
        ("clear", clear, 4, 0, 2, 50, None),
        ("=", equal, 6, 2, 1, 27, DISABLED),
        ("√", sqrt, 1, 4, 1, 25, None),
        (".", comma, 6, 1, 1, 29, None),
    ]
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=state
        ).grid(row=row, column=column, columnspan=columnspan)
    operation = "multiplication"
    fst_num = output.get()
    output.delete(0, "end")
    output.insert(0, "x")


def clear():
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=None
        ).grid(row=row, column=column, columnspan=columnspan)
    output.delete(0, "end")


def division():
    global fst_num
    global operation
    oprator_list = [
        ("+", plus, 5, 0, 1, 27, DISABLED),
        ("-", minus, 5, 1, 1, 29, DISABLED),
        ("/", division, 5, 2, 1, 29, DISABLED),
        ("x", multiply, 6, 0, 1, 27, DISABLED),
        ("clear", clear, 4, 0, 2, 50, None),
        ("=", equal, 6, 2, 1, 27, DISABLED),
        ("√", sqrt, 1, 4, 1, 25, None),
        (".", comma, 6, 1, 1, 29, None),
    ]
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=state
        ).grid(row=row, column=column, columnspan=columnspan)
    operation = "division"
    fst_num = output.get()
    output.delete(0, "end")
    output.insert(0, "/")


def sqrt():
    global fst_num
    global output2

    fst_num = output.get()
    output.delete(0, "end")
    result = math.sqrt(int(fst_num))
    output.insert(0, int(result))
    nums = ["√", str(result)]
    ro = output2.grid_info()["row"]
    if ro == 0:
        output2.insert(0, "".join(nums))
        output2 = Entry(fram2, width=25)
        output2.grid(row=ro + 1, column=0)
    else:
        output2.insert(0, "".join(nums))
        output2 = Entry(fram2, width=25)
        output2.grid(row=ro + 1, column=0)


def comma():
    output.insert("end", ".")


def equal():
    global output2
    global nums

    oprator_list = [
        ("+", plus, 5, 0, 1, 27, None),
        ("-", minus, 5, 1, 1, 29, None),
        ("/", division, 5, 2, 1, 29, None),
        ("x", multiply, 6, 0, 1, 27, None),
        ("clear", clear, 4, 0, 2, 50, None),
        ("=", equal, 6, 2, 1, 27, DISABLED),
        ("√", sqrt, 1, 4, 1, 25, None),
        (".", comma, 6, 1, 1, 29, None),
    ]
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=state
        ).grid(row=row, column=column, columnspan=columnspan)
    scn_num = output.get()
    output.delete(0, "end")
    if operation == "addition":
        result = float(fst_num) + float(scn_num)
        output.insert(0, result)
        nums = [str(fst_num), "+", str(scn_num), "=", str(result)]
        ro = output2.grid_info()["row"]
        if ro == 0:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
        else:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
    elif operation == "division":
        result = float(fst_num) / float(scn_num)
        output.insert(0, float(result))
        nums = [str(fst_num), "/", str(scn_num), "=", str(result)]
        ro = output2.grid_info()["row"]
        if ro == 0:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
        else:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
    elif operation == "multiplication":
        result = float(fst_num) * float(scn_num)
        output.insert(0, result)
        nums = [str(fst_num), "x", str(scn_num), "=", str(result)]
        ro = output2.grid_info()["row"]
        if ro == 0:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
        else:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
    elif operation == "minus":
        result = float(fst_num) - float(scn_num)
        output.insert(0, result)
        ro = output2.grid_info()["row"]
        nums = [str(fst_num), "-", str(scn_num), "=", str(result)]
        if ro == 0:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)
        else:
            output2.insert(0, "".join(nums))
            output2 = Entry(fram2, width=25)
            output2.grid(row=ro + 1, column=0)


def nex():
    next_back = [(">>", nex, SUNKEN, 1, 3), ("<<", back, None, 2, 3)]
    for nb, fun, reli, row, column in next_back:
        Button(root, text=nb, relief=reli, command=fun, padx=2, pady=2).grid(
            row=row, column=column
        )
    root.geometry("500x490")


def back():
    next_back = [(">>", nex, None, 1, 3), ("<<", back, SUNKEN, 2, 3)]
    for nb, fun, reli, row, column in next_back:
        Button(root, text=nb, relief=reli, command=fun, padx=2, pady=2).grid(
            row=row, column=column
        )
    root.geometry("245x490")


def delete():
    output.delete(len(output.get()) - 1, END)


def cos():
    numb = output.get()
    output.delete(0, "end")
    output.insert("end", math.cos(int(numb)))


def sin():
    numb = output.get()
    output.delete(0, "end")
    output.insert("end", math.sin(int(numb)))


def tan():
    numb = output.get()
    output.delete(0, "end")
    output.insert("end", math.tan(int(numb)))


def cosh():
    numb = output.get()
    output.delete(0, "end")
    output.insert("end", math.cosh(float(numb)))


def sinh():
    numb = output.get()
    output.delete(0, "end")
    output.insert("end", math.sinh(float(numb)))


def tanh():
    numb = output.get()
    output.delete(0, "end")
    output.insert("end", math.tanh(float(numb)))


def showh():
    global coshbutton
    global sinhbutton
    global tanhbutton

    root.geometry("600x490")
    coshbutton = Button(root, text="cosh", command=cosh, padx=25, pady=25)
    coshbutton.grid(row=3, column=5)
    sinhbutton = Button(root, text="sinh", command=sinh, padx=25, pady=25)
    sinhbutton.grid(row=3, column=6)
    tanhbutton = Button(root, text="tanh", command=tanh, padx=25, pady=25)
    tanhbutton.grid(row=3, column=7)

    next_back = [
        (">>", nex, None, 1, 3, 2),
        ("<<", back, SUNKEN, 2, 3, 2),
        ("del", delete, None, 0, 3, 2),
        ("<<", hideh, None, 3, 4, 25),
    ]

    for nb, fun, reli, row, column, size in next_back:
        Button(root, text=nb, relief=reli, command=fun, padx=size, pady=size).grid(
            row=row, column=column
        )


def show():
    global cosbutton
    global sinbutton
    global tanbutton

    root.geometry("600x490")
    cosbutton = Button(root, text="cos", command=cos, padx=25, pady=25)
    cosbutton.grid(row=2, column=5)
    sinbutton = Button(root, text="sin", command=sin, padx=25, pady=25)
    sinbutton.grid(row=2, column=6)
    tanbutton = Button(root, text="tan", command=tan, padx=25, pady=25)
    tanbutton.grid(row=2, column=7)

    next_back = [
        (">>", nex, None, 1, 3, 2),
        ("<<", back, SUNKEN, 2, 3, 2),
        ("del", delete, None, 0, 3, 2),
        ("<<", hide, None, 2, 4, 25),
    ]

    for nb, fun, reli, row, column, size in next_back:
        Button(root, text=nb, relief=reli, command=fun, padx=size, pady=size).grid(
            row=row, column=column
        )


def hide():
    root.geometry("600x490")

    cosbutton.grid_forget()
    sinbutton.grid_forget()
    tanbutton.grid_forget()

    next_back = [
        (">>", nex, None, 1, 3, 2),
        ("<<", back, SUNKEN, 2, 3, 2),
        ("del", delete, None, 0, 3, 2),
        (">>", show, None, 2, 4, 25),
    ]

    for nb, fun, reli, row, column, size in next_back:
        Button(root, text=nb, relief=reli, command=fun, padx=size, pady=size).grid(
            row=row, column=column
        )


def hideh():
    root.geometry("600x490")

    coshbutton.grid_forget()
    sinhbutton.grid_forget()
    tanhbutton.grid_forget()

    next_back = [
        (">>", nex, None, 1, 3, 2),
        ("<<", back, SUNKEN, 2, 3, 2),
        ("del", delete, None, 0, 3, 2),
        (">>", showh, None, 3, 4, 25),
    ]

    for nb, fun, reli, row, column, size in next_back:
        Button(root, text=nb, relief=reli, command=fun, padx=size, pady=size).grid(
            row=row, column=column
        )


oprator_list = [
    ("+", plus, 5, 0, 1, 27, None),
    ("-", minus, 5, 1, 1, 29, None),
    ("/", division, 5, 2, 1, 29, None),
    ("x", multiply, 6, 0, 1, 27, None),
    ("clear", clear, 4, 0, 2, 50, None),
    ("=", equal, 6, 2, 1, 27, DISABLED),
    ("√", sqrt, 1, 4, 1, 25, None),
    (".", comma, 6, 1, 1, 29, None),
]
button_list = [
    (1, 1, 0),
    (2, 1, 1),
    (3, 1, 2),
    (4, 2, 0),
    (5, 2, 1),
    (6, 2, 2),
    (7, 3, 0),
    (8, 3, 1),
    (9, 3, 2),
    (0, 4, 2),
]

next_back = [
    (">>", nex, None, 1, 3, 2),
    ("<<", back, SUNKEN, 2, 3, 2),
    ("del", delete, None, 0, 3, 2),
    (">>", show, None, 2, 4, 25),
    (">>", showh, None, 3, 4, 25),
]


def click(number) -> int:
    output.insert("end", number)
    for operator, operationn, row, column, columnspan, padx, state in oprator_list:
        Button(
            root, text=operator, padx=padx, pady=25, command=operationn, state=None
        ).grid(row=row, column=column, columnspan=columnspan)
    a = output.get()
    if a[0] == "+":
        output.delete(0, "end")
        output.insert("end", number)
    elif a[0] == "-":
        output.delete(0, "end")
        output.insert("end", number)
    if a[0] == "x":
        output.delete(0, "end")
        output.insert("end", number)
    elif a[0] == "/":
        output.delete(0, "end")
        output.insert("end", number)


fram = LabelFrame(root, text="output", pady=3, bg="#511414", fg="red")
fram.grid(row=0, column=0, columnspan=3)
fram2 = LabelFrame(root, text="history", bg="#511414", fg="#D7BAFF")
fram2.grid(row=2, column=4, columnspan=3, rowspan=9)
output = Entry(fram, width=25)
output.grid(row=0, column=0)
output2 = Entry(fram2, width=25)
output2.grid(row=0, column=0)

for number, row, column in button_list:
    Button(root, text=number, padx=27, pady=25, command=lambda a=number: click(a)).grid(
        row=row, column=column
    )

for operator, operationn, row, column, columnspan, padx, state in oprator_list:
    Button(
        root, text=operator, padx=padx, pady=25, command=operationn, state=state
    ).grid(row=row, column=column, columnspan=columnspan)

for nb, fun, reli, row, column, size in next_back:
    Button(root, text=nb, relief=reli, command=fun, padx=size, pady=size).grid(
        row=row, column=column
    )

root.mainloop()
