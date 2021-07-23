import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint


def display(event):
    print(type(event), event)
    label1.config(text=entry1.get())


main = tk.Tk()
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)
label1 = tk.Label(main, font=font1, text="status")
entry1 = tk.Entry(main, font=font2)
button1 = tk.Button(main, font=font1, text="Submit")
label1.pack()
entry1.pack()
button1.pack()
entry1.bind("<Return>", display)
button1.bind("<Button-1>", display)
button1.bind("<Return>", display)
button1.bind("<space>", display)
entry1.focus_set()
main.mainloop()
