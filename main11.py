import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint

# print("func1 is ", type(func1))
# print("func1() is ", type(func1()))
main = tk.Tk()
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)

l1 = tk.Label(main, text="label1", font=font2, bg='#C0FFEE')
l2 = tk.Label(main, text="label2", font=font2, bg='#C0EEFF')

counter = 0
counter2 = [0]


def func1():
    global counter
    l1.config(text="button1 clicked %d times" % counter, bg="#FFFFEE")
    counter += 1


def func2():
    l2.config(text="button2 clicked %d times" % counter2[0], bg="#C0FFEE")
    counter2[0] += 1


def func3():
    b4.pack()


def func4():
    b4.pack_forget()


b1 = tk.Button(main, text="button1", font=font1, command=func1)
b2 = tk.Button(main, text="button2", font=font1, command=func2)
b3 = tk.Button(main, text="button3", font=font1, command=func3)
b4 = tk.Button(main, text="button4", font=font1, command=func4)
l1.pack()
l2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()

main.mainloop()
