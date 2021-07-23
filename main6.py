import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint

main = tk.Tk()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="@標楷體", size=28)
label1 = tk.Label(main, text="main label",
                  font=font1,
                  padx=10, pady=30,
                  bg='#C0FFEE')
button1 = tk.Button(main, text="button1",
                    font=font1,
                    padx=20, pady=20,
                    bg="#FFC0EE")
button2 = tk.Button(main, text="按鈕",
                    font=font2,
                    padx=20, pady=20,
                    bg="#FFC0EE")
label1.pack()
button1.pack()
button2.pack()

main.mainloop()
