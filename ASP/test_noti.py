import tkinter as tk


class RoundedButton(tk.Canvas):
        
    def border(self, event):
        if event.type == "4":
            self.itemconfig(self.rect, fill="#d2d6d3")

        else:
            self.itemconfig(self.rect, fill=self.btnbackground)

def func():
    print("Button pressed")

root = tk.Tk()
btn = RoundedButton(text="This is a \n rounded button", radius=100, btnbackground="#0078ff", btnforeground="#ffffff", clicked=func)
btn.pack(expand=True, fill="both")
root.mainloop()