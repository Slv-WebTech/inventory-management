from tkinter import *
from PIL import Image, ImageTk
from login import Loginsystem

class welcome:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x500+100+100')
        self.root.title(' Inventory Management System | Developed by Vivek Sharma')
        self.root.config(bg='white')
        root.resizable(False, False)

        self.icon1 = Image.open('images/welcome.png')
        self.icon1 = self.icon1.resize((1100,500), Image.ANTIALIAS)
        self.icon1 = ImageTk.PhotoImage(self.icon1)
        self.lab_icon1 = Label(self.root, image=self.icon1, bd=2, relief=RAISED)
        self.lab_icon1.pack(fill=BOTH)

        log_button = Button(self.lab_icon1, text="Login", font=("times new roman", 15, "bold"), command=self.login
                            , bg="gray", fg="#fff",
                            cursor="hand2")
        log_button.place(x=750, y=300, width=150, height=35)
        exit_button = Button(self.lab_icon1, text="Exit", font=("times new roman", 15, "bold"), command=self.root.destroy
                            , bg="lightgray", fg="#00B0f0",
                            cursor="hand2")
        exit_button.place(x=750, y=340, width=250, height=50)

    def login(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Loginsystem(self.new_win)


if __name__ == '__main__':
    root = Tk()
    obj = welcome(root)
    root.mainloop()


