import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("539x560")
root.resizable(False, False)
root.configure(background="black")

screen = Label(root, width=25, height=2,text="", font=("arial", 30))
screen.pack()

equation = ""
def show(value):
    global equation
    if (value=="%"):
        value="/100"

    current = screen['text']
    equation += value
    screen.config(text=equation)

def clear():
    global equation
    equation = ""
    screen.config(text=equation)


def calculation ():
    global equation
    cal=""
    if equation != "":
        try:
            cal=eval(equation)
        except:
            cal="Error"
            equation=""

    screen.config(text=cal)


Button(root, text="C", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="orange", fg="white",
       command=lambda: clear()).place(x=5, y=110)
Button(root, text="%", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("%")).place(x=140, y=110)
Button(root, text="/", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("/")).place(x=275, y=110)
Button(root, text="*", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("*")).place(x=410, y=110)


Button(root, text="7", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("7")).place(x=5, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("8")).place(x=140, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("9")).place(x=275, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("-")).place(x=410, y=200)


Button(root, text="4", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("4")).place(x=5, y=290)
Button(root, text="5", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("5")).place(x=140, y=290)
Button(root, text="6", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("6")).place(x=275, y=290)
Button(root, text="+", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("+")).place(x=410, y=290)


Button(root, text="1", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("1")).place(x=5, y=380)
Button(root, text="2", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("2")).place(x=140, y=380)
Button(root, text="3", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("3")).place(x=275, y=380)
Button(root, text="=", width=5, height=3, font=("arial", 28, "bold"), bd=1, background="#CC5500", fg="white",
       command=lambda: calculation()).place(x=410, y=380)


Button(root, text="0", width=10, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show("0")).place(x=15, y=470)
Button(root, text=".", width=5, height=1, font=("arial", 28, "bold"), bd=1, background="#2a2d36", fg="white",
       command=lambda: show(".")).place(x=275, y=470)


root.mainloop()
