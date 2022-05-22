from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *

a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)



def ex():
   v = messagebox.askquestion("ການອອກຈາກລະບົບ","ທ່ານຕ້ອງການອອກຈາກລະບົບ ຫຼື ບໍ່?")
   if(v == 'yes'):
       exit()

# button
canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

bt1 = PhotoImage(file="ASP/Image/bg_report_today.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    # command=check_in,
    relief="flat",
)
img0 = PhotoImage(file = f"ASP/Image/exit.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = ex,
    relief = "flat")

b0.place(
    x = 400, y = 750)


bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    # command=back,
    relief="flat",
)
button_5.place(x=900, y=750)


a.mainloop()