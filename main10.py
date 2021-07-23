import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint

main = tk.Tk()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)
reliefs = ['flat', 'raised', 'sunken', 'solid', 'groove']
# for i in range(5):
#     button = tk.Button(main, font=font1, border=5 + i * 3)
#     button.pack()

for r in reliefs:
    button = tk.Button(main, font=font1, relief=r, bg='#C0FFEE')
    button.pack()

main.mainloop()
