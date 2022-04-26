from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
import mysql.connector
from tkinter import font as tkfont
from tkinter import messagebox
import os
import db

a=tkinter.Tk()
# a.geometry("1500x900")
a.attributes("-fullscreen", True)

def back():
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if(l == 'yes'):
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\window1.py")

#button
canvas = Canvas(
    a,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "ASP/Image/bg_attan.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

bt1 = PhotoImage(file="ASP/Image/bt_start.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    # command=clear,
    relief="flat")
button_1.place(
    x=500.,
    y=180)

bt3= PhotoImage(file="ASP/Image/back.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_3.place(
    x=200,
    y=650,
    width=246,
    height=90
)

a.mainloop()
