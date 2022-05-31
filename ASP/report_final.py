from tkcalendar import *
from tkinter import *
from tkinter import font as tkFont
from datetime import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os

frm = Tk()
frm.geometry("1500x900")
frm.attributes("-fullscreen", True)

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()

def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\\report.py")


def report_teacher_today():
    frm.withdraw()
    b.deiconify()
    st = ttk.Style(b)
    st.theme_use("clam")
    st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
    st.configure("Treeview", rowheight=60, font=("Saysettha OT", 12))
    cl_Name = cb_class.get()
    s_Name = cb_Subject.get()
    start_Date = cale_1.get_date()
    end_Date = cale_2.get_date()
    sql = (
        "select st_Id, Name, Surname, s_Name, cl_Name, sc_Period, sc_Year, SUM(first_Absence + second_Absence) from tb_attandance where cl_Name ='"
        + str(cl_Name)
        + "' and s_Name='"
        + str(s_Name)
        + "' and date BETWEEN '"
        + str(start_Date)
        + "' and '"
        + str(end_Date)
        + "';"
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
    )

    tree.column("#0", width=5)
    tree.column("#1", width=180, anchor="center")
    tree.column("#2", width=180, anchor="center")
    tree.column("#3", width=180, anchor="center")
    tree.column("#4", width=250, anchor="center")
    tree.column("#5", width=180, anchor="center")
    tree.column("#6", width=180, anchor="center")
    tree.column("#7", width=180, anchor="center")
    tree.column("#8", width=180, anchor="center")

    tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
    tree.heading("#2", text="ຊື່")
    tree.heading("#3", text="ນາມສະກຸນ")
    tree.heading("#4", text="ວິຊາ")
    tree.heading("#5", text="ຊັ້ນຮຽນ")
    tree.heading("#6", text="ພາກ")
    tree.heading("#7", text="ສົກຮຽນ")
    tree.heading("#8", text="ຜົນລວມການຂາດຮຽນ")

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
            ),
        )
        i = i + 1
    tree.place(x=-15, y=80)

canvas = Canvas(frm, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report_final.png")
background = canvas.create_image(950.0, 540.0, image=background_img)




###calendar
lb1 = Label(frm, text="ກະລຸນາເລືອກວັນທີ່ເລີ່ມຮຽນ", font=("Saysettha OT", 16),bg="#ECF8DC")
lb1.place(x=300, y=100)

cale_1 = Calendar(frm, date_pattern="y-mm-dd", selectmode="day")
cale_1.place(x=300, y=180)

lb2 = Label(frm, text="ກະລຸນາເລືອກວັນທີ່ສິ້ນສຸດ", font=("Saysettha OT", 16),bg="#ECF8DC")
lb2.place(x=1000, y=100)

cale_2 = Calendar(frm, date_pattern="y-mm-dd", selectmode="day")
cale_2.place(x=1000, y=180)


bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=report_teacher_today,
    relief="flat",
)
button_5.place(x=1100, y=750)

bt4 = PhotoImage(file="ASP/Image/back.png")
button_4 = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)
button_4.place(x=300, y=750)


##############################################################################################
##############################################################################################


b = Tk()
b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.attributes("-fullscreen", True)
b.withdraw()

cbFont = tkFont.Font(family="Saysettha OT", size=18)

conn.execute("select cl_Name from tb_class;")
results = conn.fetchall()
combo_cl_name = [result[0] for result in results]


class_lb = Label(frm, text="ກະລຸນາເລືອກຊັ້ນຮຽນ : ", font=cbFont,bg="#ECF8DC")
class_lb.place(x=450, y=450)

cb_class = ttk.Combobox(frm, width=25, values=combo_cl_name)
cb_class.place(x=700, y=450)
cb_class.config(font=(cbFont), state="readonly")
cb_class.configure(font=("Saysettha OT", 16))
cb_class.option_add("*font", cbFont)
cb_class.current(0)

conn.execute("select s_Name from tb_subject")
results = conn.fetchall()
combo_s_name = [result[0] for result in results]

subject_lb = Label(frm, text="ກະລຸນາເລືອກວິຊາ : ", font=cbFont,bg="#ECF8DC")
subject_lb.place(x=450, y=600)

cb_Subject = ttk.Combobox(frm, width=25, values=combo_s_name)
cb_Subject.place(x=700, y=600)
cb_Subject.config(font=(cbFont), state="readonly")
cb_Subject.configure(font=("Saysettha OT", 16))
cb_Subject.option_add("*font", cbFont)
cb_Subject.current(0)

lbShow = Label(b, text="ລາຍງານຂໍ້ມູນນການຂາດນັກສຶກສາທ້າຍພາກ")
lbShow.pack(side="top", fill="x")
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")

frm.mainloop()

