import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint

main = tk.Tk()
font1 = Font(family='Segoe UI', size=24)

b1 = tk.Button(main, text="button1", font=font1, bg='#C0FFEE')
b2 = tk.Button(main, text="button2", font=font1, bg='#FFC0EE')
b3 = tk.Button(main, text="button3", font=font1, bg='#C0EEFF')
b4 = tk.Button(main, text="button4", font=font1, bg='#FFEEC0')
b5 = tk.Button(main, text="button5", font=font1, bg='#EEC0FF')
b6 = tk.Button(main, text="button6", font=font1, bg='#EEFFC0')
# step1
# b1.pack(expand=True, fill=tk.X)
# b2.pack(fill=tk.Y)
# step2
b1.pack(fill=tk.X)
b2.pack(side=tk.LEFT)
b3.pack(side=tk.LEFT, fill=tk.Y)
b4.pack(side=tk.TOP)
b5.pack(side=tk.TOP, fill=tk.X)
b6.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
main.minsize(600, 600)
main.maxsize(600, 600)

main.mainloop()
