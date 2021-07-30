import tkinter as tk
from tkinter import font as font
from tkinter.font import Font
from pprint import pprint
import cv2

print(cv2.__version__)
main = tk.Tk()
main.geometry("640x480")

label1 = tk.Label(main, bg='#C0FFEE')
label1.grid(row=0, column=0)
cap = cv2.VideoCapture(0)


def show_frames():
    cv2Image = cv2.cvtColor(cap.read())


show_frames()

main.mainloop()
