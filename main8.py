import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint

main = tk.Tk()
font1 = Font(family='Segoe UI', size=24)

b1 = tk.Button(main, text="Python", font=font1)
b2 = tk.Button(main, text="C#", font=font1)
b3 = tk.Button(main, text="Java", font=font1)

b1.place(anchor=tk.NW, height=100, width=100, x=0, y=0)
b2.place(anchor=tk.CENTER, height=100, width=100, x=100, y=0)
b3.place(anchor=tk.SW, height=100, width=100, x=100, y=100)
main.minsize(400, 400)
main.maxsize(400, 400)

main.mainloop()
