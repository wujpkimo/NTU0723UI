import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint


def func1():
    print("button1 clicked")


print("func1 is ", type(func1))
print("func1() is ", type(func1()))
main = tk.Tk()
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)

l1 = tk.Label(main, text="label1", font=font2, bg='#C0FFEE')
l2 = tk.Label(main, text="label2", font=font2, bg='#C0EEFF')
b1 = tk.Button(main, text="button1", font=font1, command=func1)
b2 = tk.Button(main, text="button2", font=font1, command=func1)
l1.pack()
l2.pack()
b1.pack()
b2.pack()

main.mainloop()
