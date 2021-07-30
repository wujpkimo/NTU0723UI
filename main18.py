import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint
from PIL import Image, ImageTk
import cv2

print(cv2.__version__)
main = tk.Tk()
main.geometry("640x480")

label1 = tk.Label(main, bg='#C0FFEE')
label1.grid(row=0, column=0)
cap = cv2.VideoCapture(0)


def show_frames():
    cv2Image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2Image)
    imageTk = ImageTk.PhotoImage(image=img)
    label1.imgtk = imageTk
    label1.configure(image=imageTk)
    label1.after(20, show_frames())
    pass


show_frames()

main.mainloop()
