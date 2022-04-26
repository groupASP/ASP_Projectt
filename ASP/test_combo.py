from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
import mysql.connector
from tkinter import font as tkfont
import db

a=tkinter.Tk()
a.geometry("1500x900")

#connect database
conn = pymysql.connect(user="root", password="", host="Localhost",database="asp_base")
curs = conn.cursor()

#combobox form database
curs.execute('select Name from tb_face;')
results = curs.fetchall()
for_combobox1 = [result[0] for result in results]

#set font
cbFont = tkfont.Font(family="Saysettha OT", size=16)

#combobox1
cb = ttk.Combobox(a, width=25, value=for_combobox1)
cb.place(x=250, y=520)
cb.config(font=(cbFont), state="readonly")
cb.option_add("*font", cbFont)
cb.current()

a.mainloop()
