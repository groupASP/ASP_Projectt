
from tkinter import *
from tkinter import font as tkFont
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *
import pandas as pd
import tkinter.filedialog as fd

a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()


def report_today():
    a.withdraw()
    b.deiconify()
    st = ttk.Style(b)
    st.theme_use("clam")
    st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
    st.configure("Treeview", rowheight=60, font=("Saysettha OT", 12))
    cl_Name = cb_class.get()
    s_Name = cb_subject.get()
    today = datetime.now().strftime("%Y-%m-%d")
    sql = (
        "select st_Id, Name, Surname, d_Name, s_Name, cl_Name, sc_Period, sc_Year, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where cl_Name = '"
        + cl_Name
        + "' and s_Name='"
        + s_Name
        + "' and date = '"
        + today
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
        "9",
        "10",
        "11",
        "12",
        "13",
    )

    tree.column("#0", width=5)
    tree.column("#1", width=140, anchor="center")
    tree.column("#2", width=100, anchor="center")
    tree.column("#3", width=100, anchor="center")
    tree.column("#4", width=120, anchor="center")
    tree.column("#5", width=150, anchor="center")
    tree.column("#6", width=100, anchor="center")
    tree.column("#7", width=120, anchor="center")
    tree.column("#8", width=120, anchor="center")
    tree.column("#9", width=150, anchor="center")
    tree.column("#10", width=120, anchor="center")
    tree.column("#11", width=100, anchor="center")
    tree.column("#12", width=100, anchor="center")
    tree.column("#13", width=130, anchor="center")

    tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
    tree.heading("#2", text="ຊື່")
    tree.heading("#3", text="ນາມສະກຸນ")
    tree.heading("#4", text="ມື້ຮຽນ")
    tree.heading("#5", text="ວິຊາ")
    tree.heading("#6", text="ຊັ້ນຮຽນ")
    tree.heading("#7", text="ພາກ")
    tree.heading("#8", text="ສົກຮຽນ")
    tree.heading("#9", text="ເວລາເຂົ້າຮຽນ")
    tree.heading("#10", text="ເວລາອອກຮຽນ")
    tree.heading("#11", text="ໝາຍເຂົ້າຮຽນ")
    tree.heading("#12", text="ໝາຍອອກຮຽນ")
    tree.heading("#13", text="ວັນທີ")

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
                row[9],
                row[10],
                row[11],
                row[12],
            ),
        )
        i = i + 1
    tree.place(x=-15, y=80)

    def export_data():
        sql = (
            "select st_Id, Name, Surname, d_Name, s_Name, cl_Name, sc_Period, sc_Year, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where cl_Name = '"
            + cl_Name
            + "' and s_Name='"
            + s_Name
            + "' and date = '"
            + today
            + "';"
        )
        df = pd.read_sql(sql, connection)
        header = [
            "ລະຫັດນັກສຶກສາ",
            "ຊື່",
            "ນາມສະກຸນ",
            "ມື້ຮຽນ",
            "ວິຊາ",
            "ຫ້ອງ",
            "ພາກ",
            "ສົກຮຽນ",
            "ເວລາເຂົ້າຮຽນ",
            "ເວລາອອກຮຽນ",
            "ໝາຍເຂົ້າຮຽນ",
            "ໝາຍອອກຮຽນ",
            "ວັນທີ",
        ]
        file_name = fd.asksaveasfilename(
            filetypes=[("excel file", "*.xlsx")], defaultextension=".xlsx"
        )
        df.to_excel(file_name, index=False, header=header, encoding="utf-8")

    bt_export = tkinter.Button(b, text="Export", command=export_data, width=16)
    bt_export.place(x=900, y=750)
    bt_export.configure(font=("Times New Roman", 25), bg="green", fg="white")


def back():
    b.withdraw()
    a.deiconify()


def back1():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\report.py")


# button
canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report_today.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

################################################################################
################################################################################


b = Tk()
b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.attributes("-fullscreen", True)
b.withdraw()

lbShow = tkinter.Label(b, text="ລາຍງານຂໍ້ມູນການຂາດນັກສຶກສາປະຈຳວັນ")
lbShow.pack(side="top", fill="x")
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")


cbFont = tkFont.Font(family="Saysettha OT", size=16)

cb_Style = ttk.Style()
cb_Style.theme_use("default")
cb_Style.configure("TCombobox", fieldbackground="orange", background="white")

label = Label(
    a,
    text="ກະລຸນາເລືອກຫ້ອງຂອງທ່ານ : ",
    font=("Phetsarath OT", 20, "bold"),
    bg="#ECF8DC",
    fg="black",
)
label.place(x=300, y=200)

conn.execute("select cl_Name from tb_class;")
results = conn.fetchall()
combo_cl_name = [result[0] for result in results]

cb_class = ttk.Combobox(a, width=25, values=combo_cl_name)
cb_class.place(x=700, y=200)
cb_class.config(font=(cbFont), state="readonly")
cb_class.configure(font=("Saysettha OT", 20), state="readonly")
cb_class.option_add("*font", cbFont)
cb_class.current(0)

label = Label(
    a,
    text="ກະລຸນາເລືອກວິຊາຂອງທ່ານ : ",
    font=("Phetsarath OT", 20, "bold"),
    bg="#ECF8DC",
    fg="black",
)
label.place(x=300, y=450)

conn.execute("select s_Name from tb_subject;")
results = conn.fetchall()
combo_s_name = [result[0] for result in results]

cb_subject = ttk.Combobox(a, width=25, values=combo_s_name)
cb_subject.place(x=700, y=450)
cb_subject.config(font=(cbFont), state="readonly")
cb_subject.configure(font=("Saysettha OT", 20), state="readonly")
cb_subject.option_add("*font", cbFont)
cb_subject.current(0)

bts = tkinter.Button(b, text="Back", command=back, width=16)
bts.place(x=300, y=750)
bts.configure(font=("Times New Roman", 25), bg="#CEC2C2", fg="black")

img0 = PhotoImage(file=f"ASP/Image/back.png")
b0 = Button(
    image=img0, borderwidth=0, highlightthickness=0, command=back1, relief="flat"
)

b0.place(x=400, y=700)


bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=report_today,
    relief="flat",
)
button_5.place(x=900, y=700)


a.mainloop()
