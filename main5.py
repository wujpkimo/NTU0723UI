import tkinter as tk

top = tk.Tk()
w1 = tk.Button(top, text="Hi first gui")
w2 = tk.Button(top, text="second gui")
w1.pack()
w2.pack()

top.mainloop()
