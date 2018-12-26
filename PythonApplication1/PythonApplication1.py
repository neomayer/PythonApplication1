import tkinter as tk
from tkinter import *


win=tk.Tk()
win.title("Hello World")
win.geometry("800x600")

def btn_OnClick():
    print("Hello")

lbl = Label(win, text="Hello World!")
lbl.pack()

btn = Button(win, text="test", command=btn_OnClick)

btn.pack()

win.mainloop()



