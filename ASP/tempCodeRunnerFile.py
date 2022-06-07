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