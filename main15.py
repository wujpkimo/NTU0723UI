import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint


def func1(ev):
    print("value=", ev)
    label1.config(text=message % int(ev))


message = "your value=%d"
main = tk.Tk()
value = tk.IntVar()
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)
label1 = tk.Label(main, text=message % value.get(), font=font1, bg='#C0FFEE')
scale1 = tk.Scale(main, label="volumn", font=font1, orient='h',
                  variable=value,
                  command=func1)
label1.pack()
scale1.pack(fill=tk.X)

main.minsize(400, 300)
main.maxsize(400, 300)

main.mainloop()
