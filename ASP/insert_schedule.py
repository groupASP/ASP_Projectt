from math import comb
import tkinter
from tkinter import ttk
from tkinter import font as tkfont
import os
from tkinter import messagebox
from tkinter import *
import pymysql

frm = tkinter.Tk()
frm.title("Insert Student")
frm.geometry('1920x1080')
frm.attributes('-fullscreen', True)

def getId():
    connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
    conn = connection.cursor()
    sql = "SELECT sc_Id FROM tb_schedule order by sc_Id desc limit 1;"
    conn.execute(sql)
    profile=None
    for row in conn:
        profile=row
    connection.close()
    c = int(''.join(map(str, profile)))
    return c

def insert():
    import pymysql
    connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
    conn = connection.cursor()

    oid=getId()
    Id=oid+1
    sc_Id = Id
    d_Id = cb_day.get()
    sc_Peroid = cb_period.get()
    sc_Year = en_year.get()
    r_Id = cb_room.get()
    cl_Id=cb_cl.get()
    s_Id=cb_subject.get()
    t_Id=cb_teacher.get()
    
    value = messagebox.askquestion("ການຢືນຢັນ", "ທ່ານຕ້ອງການເພີ່ມຂໍ້ມູນແທ້ຫຼືບໍ່?")
    if(value == 'yes'):
        sql_insert = "insert into tb_schedule values('"+str(sc_Id)+"','"+d_Id+"','"+sc_Peroid+"','"+sc_Year+"','"+r_Id+"','"+cl_Id+"','"+s_Id+"','"+t_Id+"');"
        conn.execute(sql_insert)
        connection.commit()
        messagebox.showinfo("ການສະແດງຜົນ","ທ່ານໄດ້ເພີ່ມຂໍ້ມູນຕາຕະລາງຮຽນສຳເລັດແລ້ວ")
    cb_day.set("")
    cb_period.set("")
    en_year.delete(0,END)
    cb_room.set("")
    cb_subject.set("")
    cb_cl.set("")
    cb_teacher.set("")


def back():
    l = messagebox.askquestion("Back","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຂໍ້ມູນນັກສຶກສາ ຫຼື ບໍ່?")
    if(l == 'yes'):
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\schedule.py")



canvas = Canvas(
    frm,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"ASP/Image/bg_insert_sche.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)


lb1 = tkinter.Label(frm, text="ມື້ຮຽນ:")
lb1.place(x=40, y=150)
lb1.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb2 = tkinter.Label(frm, text="ຮອບຮຽນ:")
lb2.place(x=500, y=150)
lb2.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb3 = tkinter.Label(frm, text="ສົກຮຽນ:")
lb3.place(x=1050, y=150)
lb3.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb4 = tkinter.Label(frm, text="ຫ້ອງຮຽນ:")
lb4.place(x=20, y=450)
lb4.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb5 = tkinter.Label(frm, text="ຊັ້ນຮຽນ:")
lb5.place(x=390, y=450)
lb5.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb6 = tkinter.Label(frm, text="ວິຊາຮຽນ:")
lb6.place(x=800, y=450)
lb6.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb7 = tkinter.Label(frm, text="ລະຫັດອາຈານ:")
lb7.place(x=1180, y=450)
lb7.config(font=("Saysettha OT", 18),bg="#ECF8DC")


# Entry
en_year = tkinter.Entry(frm)
en_year.place(x=1150, y=150)
en_year.config(font=("Saysettha OT",18),width=20)



#SET FONT
cbFont = tkfont.Font(family="Saysettha OT", size=16)


# combo peroid
cb_list_period = ["ພາກເຊົ້າ", "ພາກບ່າຍ", "ພາກຄ່ຳ"]

cb_period = ttk.Combobox(frm, width=15, value=cb_list_period)
cb_period.place(x=650, y=150)
cb_period.config(font=("Saysettha OT", 18), state="readonly")
cb_period.current(0)
cb_period.option_add("*font", cbFont)

#connect database
conn = pymysql.connect(user="root", password="", host="Localhost",database="asp_base")
curs = conn.cursor()


# combo day
curs.execute('select d_Id from tb_day;')
results = curs.fetchall()
combo_d_id = [result[0] for result in results]

cb_day = ttk.Combobox(frm, width=15, value=combo_d_id)
cb_day.place(x=150, y=150)
cb_day.config(font=("Saysettha OT", 18), state="readonly")
cb_day.option_add("*font", cbFont)
cb_day.current()

#combo_room_id form database
curs.execute('select r_Id from tb_room;')
results = curs.fetchall()
combo_r_id = [result[0] for result in results]

#combobox_room_id
cb_room =ttk.Combobox(frm, width=12,values=combo_r_id)
cb_room.place(x=150, y=450)
cb_room.config(font=(cbFont), state="readonly")
cb_room.option_add("*font", cbFont)
cb_room.current()

#combo_subject_id form database
curs.execute('select s_Id from tb_subject;')
results = curs.fetchall()
combo_s_id = [result[0] for result in results]

#combobox_subject_id
cb_subject =ttk.Combobox(frm, width=18,values=combo_s_id)
cb_subject.place(x=910, y=450)
cb_subject.config(font=(cbFont), state="readonly")
cb_subject.option_add("*font", cbFont)
cb_subject.current()

#combo_class_id form database
curs.execute('select cl_Id from tb_class;')
results = curs.fetchall()
combo_cl_id = [result[0] for result in results]

#combobox_class_id
cb_cl =ttk.Combobox(frm, width=17,values=combo_cl_id)
cb_cl.place(x=520, y=450)
cb_cl.config(font=(cbFont), state="readonly")
cb_cl.option_add("*font", cbFont)
cb_cl.current()

#combo_teacher_id form database
curs.execute('select t_Id from tb_teacher;')
results = curs.fetchall()
combo_t_id = [result[0] for result in results]

#combobox_student_id
cb_teacher =ttk.Combobox(frm, width=13,values=combo_t_id)
cb_teacher.place(x=1330, y=450)
cb_teacher.config(font=(cbFont), state="readonly")
cb_teacher.option_add("*font", cbFont)
cb_teacher.current()


#Button
img1 = PhotoImage(file = f"ASP/Image/add.png")
btAdd = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = insert,
    relief = "flat")

btAdd.place(
    x = 900, y = 690,)

img2 = PhotoImage(file = f"ASP/Image/back.png")
btBack = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back,
    relief = "flat")

btBack.place(
    x = 400, y = 690,)


frm.mainloop()