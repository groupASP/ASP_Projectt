from tkinter import *
from tkinter import  messagebox
import  os
from tkinter import ttk
from tkinter.ttk import Treeview
from colorama import Style
import pymysql
import numpy as np
import cv2
from PIL import Image

# ຄຳສັ່ງເຊື່ອມຕໍ່
connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()

def trainImg():
    Recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = "ASP/ImageData"

    def getImagesID(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces=[]
        IDs=[]

        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert("L")
            faceNp = np.array(faceImg, "uint8")
            ID = int(os.path.split(imagePath)[-1].split(".")[2])
            faces.append(faceNp)
            print(ID)
            IDs.append(ID)
            cv2.imshow("Training", faceNp)
            cv2.waitKey(10)
        return IDs, faces
    Ids, faces = getImagesID(path)
    Recognizer.train(faces, np.array(Ids))
    Recognizer.save("ASP/Data/trainingImage.yml")
    cv2.destroyAllWindows()

def insert():
    window.withdraw()
    os.system("D:\ASP_Project\ASP\InsertOrUpdateFace.py")

def back():
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if(l == 'yes'):
        window.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")


window = Tk()
# window.geometry('1500x900')
window.attributes('-fullscreen', True)
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "ASP/Image/bg_face.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

bt1 = PhotoImage(file="ASP/Image/scan.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    command=insert,
    relief="flat")
button_1.place(
    x=1100,
    y=150,
    width=181,
    height=173)

bt2 = PhotoImage(file="ASP/Image/train.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    command=trainImg,
    relief="flat"
)
button_2.place(
    x=1100,
    y=450,
    width=181,
    height=172
)

bt3= PhotoImage(file="ASP/Image/back.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_3.place(
    x=100,y=720,
    width=246,
    height=90
)

bt4 = PhotoImage(file=f"ASP/Image/delete.png")
btDelete = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    # command=delete,
    relief="flat")
btDelete.place(
    x=450, y=720, )

bt5 = PhotoImage(file=f"ASP/Image/delete_img.png")
btDelete_img = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    # command=delete,
    relief="flat")
btDelete_img.place(
    x=800, y=720, )

Notification = Label(window, text="All things are good", bg="Green", fg="white", width=15,
                height=3, font=('times', 17, 'bold'))


st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
st.configure("Treeview", rowheight=53, font=("Saysettha OT", 14))

sql = "select* from tb_face"
conn.execute(sql)

tree =Treeview(window)
tree["columns"] = ("1", "2", "3", "4")
tree.column("#0", width=1)
tree.column("#1", width=100)
tree.column("#2", width=200)
tree.column("#3", width=200)
tree.column("#4", width=200)

tree.heading("#1", text="ລະຫັດ")
tree.heading("#2", text="ຊື່")
tree.heading("#3", text="ນາມສະກຸນ")
tree.heading("#4", text="ລະຫັດນັກສຶກສາ")

# ຄຳສັ່ງສະແດງຜົນ
i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3]))
    i = i + 1
tree.place(x=150, y=100)


window.resizable(False, False)
window.mainloop()