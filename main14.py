import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint


def func1():
    label1.config(text=message % 'pixel5')


def func2():
    label1.config(text=message % 'iphone12')


def funcX():
    if sel1.get() == 1:
        label1.config(text=message % 'pixel5')
    else:
        label1.config(text=message % 'iphone12')


message = "你選擇的是:%s"

main = tk.Tk()
sel1 = tk.IntVar()
sel1.set(1)
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)

label1 = tk.Label(main, text=message % "", font=font2)
rb1 = tk.Radiobutton(main, text="Android", font=font1, value=1, variable=sel1,
                     command=funcX)
rb2 = tk.Radiobutton(main, text="iOS", font=font1, value=2, variable=sel1,
                     command=funcX)
label1.pack()
rb1.pack()
rb2.pack()

main.mainloop()
