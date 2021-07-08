from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
import smtplib
import time


class Loginsystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x690+0+0")
        self.root.title(" Login System| IMS")
        self.root.config(bg="#fafafa")

        # ===================Images===============
        self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_image = Label(self.root, image=self.phone_image, bd=0)
        self.lbl_image.place(x=100, y=20)

        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_cngimage = Label(self.lbl_image, )
        self.lbl_cngimage.place(x=167, y=102, height=428, width=240)
        # variables
        self.empid = StringVar()
        self.password = StringVar()

        # ==================Login___Frame=================
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#fafafa")
        login_frame.place(x=600, y=60, width=350, height=460)
        # ===================Login_Title============
        title = Label(login_frame, text="Login System", font=('times new roman', 30 ,'bold'), bg="#fafafa").place(x=0, y=30,
                                                                                                     relwidth=1)
        #             line=Label(login_frame,bg="orange",font='Elephant 1 bold').place(x=0,y=90,relwidth=1)
        lbl_user = Label(login_frame, text="User I'D", font="Andalus 15", bg="#fafafa").place(x=50, y=100)
        Txt_user = Entry(login_frame, textvariable=self.empid, font=("times new roman", 15), bg="lightyellow").place(x=50,
                                                                                                                 y=140,
                                                                                                                 height=30,width=250)

        lbl_pass = Label(login_frame, text="Password", font="Andalus 15", bg="#fafafa").place(x=50, y=200)
        Txt_pass = Entry(login_frame, textvariable=self.password, font=("times new roman", 15), show='*',
                         bg="lightyellow").place(x=50, y=240, width=250,height=30)

        log_button = Button(login_frame, text="Login", font=("Arial Rounded MT", 15, "bold"), command=self.login
                            , bg="#00B0f0", fg="#fafafa", activebackground="#00B0f0", activeforeground="#fafafa",
                            cursor="hand2")
        log_button.place(x=50, y=300, width=250, height=35)

        hr = Label(login_frame, bg="lightgray").place(x=50, y=380, width=250, height=2)
        OR = Label(login_frame, text="OR", font=("times new roman", 15, "bold"), bg="#fafafa", fg="lightgray").place(
            x=150, y=365)

        forget_button = Button(login_frame, text="Forget Password?",command=self.forget, font=("times new roman", 13, "bold"),
                               cursor='hand2'
                               , bg="#fafafa", fg="#00759E", bd=0, activebackground="#fafafa",
                               activeforeground="#00759E").place(x=100, y=400)

        # =============Frame2================
        Register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#fafafa")
        Register_frame.place(x=600, y=460 + 80, width=350, height=60)

        register_lbl = Label(Register_frame, bg="#fafafa").place(x=30, y=20)
        Regiter_button = Button(Register_frame, text="IMS SYSTEM", font=("times new roman", 25, "bold")
                                , bg="#fafafa", fg="#00759E", bd=0, activebackground="#fafafa",
                                activeforeground="#00759E").pack(fill=BOTH)

        self.animate()
        #self.root.destory()
    # function
    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.empid.get() == '' or self.password.get() == '':
                messagebox.showerror('Error', "UserName And Password can't be blank", parent=self.root)
            else:
                cur.execute('select usertype from employee where eid=? AND password=?',
                            (self.empid.get(), self.password.get(),))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror('Error', "Invalid UserName Or Password", parent=self.root)

                else:
                    if user[0] == 'Admin':

                        os.system('Python dashbord.py')

                    else:

                        os.system('Python billing.py')



        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_cngimage.config(image=self.im)
        self.lbl_cngimage.after(1500, self.animate)

    def forget(self):
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            try:
                if self.empid.get() == '':
                    messagebox.showerror('Error', " Emp_id  can't be blank", parent=self.root)
                else:
                    cur.execute("select email from employee where eid=?", (self.empid.get(),))
                    email = cur.fetchone()
                    if email == None:
                        messagebox.showerror('Error', "Invalid Empolyee if try again", parent=self.root)
                    else:
                        self.var_otp = StringVar()
                        self.var_new_pass = StringVar()
                        self.var_conf_pass = StringVar()
                        # call send_email fucntion()
                        check = self.send_email(email[0])
                        if check != 's':
                            messagebox.showerror("Error", "connection Error try again ", parent=self.root)
                        else:
                            self.forget_win = Toplevel(self.root)
                            self.forget_win.title("Reset Password")
                            self.forget_win.geometry("400x350+500+100")
                            self.forget_win.focus_force()

                            title = Label(self.forget_win, text="Reset Password", font=('goudy old style', 15, "bold"),
                                          bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                            lbl_reset = Label(self.forget_win, text="Enter OTP sent on Registered email",
                                              font=("times new roman", 15)).place(x=20, y=60)
                            txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=("times new roman", 15),
                                              bg="lightyellow").place(x=20, y=100, width=250, height=30)

                            self.btn_reset = Button(self.forget_win, command=self.valiadate_otp, text="Submit",
                                                    font=("times new roman", 15), bg="lightblue")
                            self.btn_reset.place(x=280, y=100, width=100, height=30)

                            lbl_new_pass = Label(self.forget_win, text="New Password",
                                                 font=("times new roman", 15)).place(x=20, y=160)
                            txt_reset = Entry(self.forget_win, textvariable=self.var_new_pass,
                                              font=("times new roman", 15), bg="lightyellow").place(x=20, y=190,
                                                                                                    width=250,
                                                                                                    height=30)

                            lbl_confirm_pass = Label(self.forget_win, text="Confirm Password",
                                                     font=("times new roman", 15)).place(x=20, y=225)
                            txt_c_pass = Entry(self.forget_win, textvariable=self.var_conf_pass,
                                               font=("times new roman", 15), bg="lightyellow").place(x=20, y=255,
                                                                                                     width=250,
                                                                                                     height=30)

                            self.btn_Update = Button(self.forget_win, command=self.update, text="update",
                                                     state=DISABLED, font=("times new roman", 15), bg="lightblue")
                            self.btn_Update.place(x=150, y=300, width=100, height=30)


            except Exception as ex:
                messagebox.showerror('Error', f"Error due to:{str(ex)}", parent=self.root)

    def update(self):
            if self.var_new_pass.get() == "" or self.var_conf_pass.get() == "":
                messagebox.showerror("Error!!", "Password is Required", parent=self.forget_win)

            elif self.var_new_pass.get() != self.var_conf_pass.get():
                messagebox.showerror("Error!!", "Password must be same")
            else:
                con = sqlite3.connect(database=r'ims.db')
                cur = con.cursor()
                try:
                    cur.execute("update employee set password=? where eid=?",
                                (self.var_new_pass.get(), self.empid.get(),))
                    con.commit()
                    messagebox.showinfo("success", "Password Updated Successfully", parent=self.forget_win)
                    self.forget_win.destroy()


                except Exception as ex:
                    messagebox.showerror('Error', f"Error due to:{str(ex)},parent=self.root")

    def valiadate_otp(self):
            if int(self.otp) == int(self.var_otp.get()):
                self.btn_Update.config(state=NORMAL)
                self.btn_reset.config(state=DISABLED)
            else:
                messagebox.showerror("Error", "Invalid OTP Pls! Try again", parent=self.forget_win)

    def send_email(self, to):

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            email_ = "aijarivs587@gmail.com"
            pass_ = 'Vishal@07'

            server.login(email_, pass_)

            self.otp = int(time.strftime("%H%S%M")) + int(time.strftime("%S"))
            print(self.otp)

            subject = "IMS-Reset Password OTP"
            msg = f"Dear sir/Madam,\n\n your Reset OTP is {str(self.otp)}. \n\nWith Regards,\n IMS Team"
            content = "Subject:{}\n\n{}".format(subject, msg)
            server.sendmail(email_, to, content)
            check = server.ehlo()
            if (check[0] == 250):
                return 's'
            else:
                return 'f'
            server.close()




if __name__ == '__main__':
    root = Tk()
    obj = Loginsystem(root)
    root.mainloop()
    exit()

