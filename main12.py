import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint


def func1():
    l1.config(text="button clicked")


def func2(ev):
    l1.config(text="cursor enter@(%d,%d)" % (ev.x, ev.y), bg='#C0FFEE')
    print("ev=%s" % ev)


def func3(ev):
    l1.config(text="cursor leave@(%d,%d)" % (ev.x, ev.y), bg='#EEC0FF')


main = tk.Tk()
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)

l1 = tk.Label(main, text="status", font=font1, bg="#EEC0FF")
b1 = tk.Button(main, text="area", bg="#C0FFEE", font=font1, padx=20, pady=20)
l1.pack(fill=tk.X)
b1.pack()
b1.bind('<Enter>', func2)
b1.bind('<Leave>', func3)
main.minsize(300, 200)
main.maxsize(300, 200)
main.mainloop()
