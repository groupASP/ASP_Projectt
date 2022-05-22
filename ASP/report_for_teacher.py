from tkinter import *
from tkinter import font as tkFont
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *

a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()


def report_teacher_today():
    a.withdraw()
    b.deiconify()
    st = ttk.Style(b)
    st.theme_use("clam")
    st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
    st.configure("Treeview", rowheight=60, font=("Saysettha OT", 14))
    cl_Name = cb_class.get()
    today = str(date(2022, 5, 2))
    sql = (
        "select st_Id, Name, Surname, cl_Name, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where cl_Name = '"
        + cl_Name
        + "' and date = '"
        + today
        + "' ;"
    )
    conn.execute(sql)

    tree = ttk.Treeview(b)
    tree["columns"] = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    )

    tree.column("#0", width=5)
    tree.column("#1", width=180, anchor="center")
    tree.column("#2", width=150, anchor="center")
    tree.column("#3", width=150, anchor="center")
    tree.column("#4", width=150, anchor="center")
    tree.column("#5", width=150, anchor="center")
    tree.column("#6", width=150, anchor="center")
    tree.column("#7", width=150, anchor="center")
    tree.column("#8", width=150, anchor="center")
    tree.column("#9", width=150, anchor="center")

    tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
    tree.heading("#2", text="ຊື່")
    tree.heading("#3", text="ນາມສະກຸນ")
    tree.heading("#4", text="ຊັ້ນຮຽນ")
    tree.heading("#5", text="ເວລາເຂົ້າຮຽນ")
    tree.heading("#6", text="ເວລາອອກຮຽນ")
    tree.heading("#7", text="ໝາຍເຂົ້າຮຽນ")
    tree.heading("#8", text="ໝາຍອອກຮຽນ")
    tree.heading("#9", text="ວັນທີ")

    # ຄຳສັ່ງສະແດງຜົນ

    i = 0
    for row in conn:
        tree.insert(
            "",
            i,
            text="",
            values=(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
            ),
        )
        i = i + 1
    tree.place(x=-30, y=80)


def back():
    b.withdraw()
    a.deiconify()


def ex():
    v = messagebox.askquestion("ການອອກຈາກລະບົບ", "ທ່ານຕ້ອງການອອກຈາກລະບົບ ຫຼື ບໍ່?")
    if v == "yes":
        exit()


# button
canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report.png")
background = canvas.create_image(950.0, 540.0, image=background_img)


b = Tk()
b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.attributes("-fullscreen", True)
b.withdraw()

lbShow = tkinter.Label(b, text="ລາຍງານຂໍ້ມູນນັກສຶກສາປະຈຳວັນ")
lbShow.pack(side="top", fill="x")
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")


cb_Class = ["HCS6B", "HCS6C", "HCS6E"]

cbFont = tkFont.Font(family="Saysettha OT", size=16)

cb_Style = ttk.Style()
cb_Style.theme_use("default")
cb_Style.configure("TCombobox", fieldbackground="orange", background="white")

label = Label(
    a,
    text="ກະລຸນາເລືອກຫ້ອງຂອງທ່ານ",
    font=("Phetsarath OT", 20, "bold"),
    bg="#FFFFFF",
    fg="black",
)
label.place(x=570, y=200)


cb_class = ttk.Combobox(a, width=20, height=20, values=cb_Class)
cb_class.place(x=600, y=300)
cb_class.config(font=(cbFont), state="readonly")
cb_class.option_add("*font", cbFont)
cb_class.current(0)

bts = tkinter.Button(b, text="Back", command=back, width=20)
bts.place(x=550, y=750)
bts.configure(font=("Saysettha OT", 18), bg="green", fg="white")

# bt1 = PhotoImage(file="ASP/Image/bg_report_today.png")
# button_1 = Button(
#     image=bt1,
#     borderwidth=0,
#     highlightthickness=0,
#     # command=report_teacher_today,
#     relief="flat",
# )

img0 = PhotoImage(file=f"ASP/Image/exit.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=ex, relief="flat")

b0.place(x=400, y=750)


bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=report_teacher_today,
    relief="flat",
)
button_5.place(x=900, y=750)


a.mainloop()