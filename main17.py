import tkinter as tk
from tkinter import font as font, messagebox
from tkinter.font import Font
from pprint import pprint
from PIL import Image, ImageTk


def func1():
    messagebox.showinfo("About Gigabyte", "Your description will go here")


# get a image to images\ directory

main = tk.Tk()
# pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)

PATH = "./images/img_1.png"
image = Image.open(PATH)
print(type(image))
photoImage = ImageTk.PhotoImage(image)
label1 = tk.Label(main, image=photoImage, bg="#C0FFEE")
label2 = tk.Label(main, text="技嘉科技", font=font2)
button1 = tk.Button(main, text="About", font=font2, command=func1)
label1.pack()
label2.pack()
button1.pack()
main.mainloop()
