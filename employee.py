from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class EmployeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1065x500+200+110')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')
        self.root.focus_force()
        root.resizable(False, False)
        # variable decelarition
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_salary = StringVar()
        self.var_empid = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_password = StringVar()
        self.var_usertype = StringVar()

        # search bar
        searchframe = LabelFrame(self.root, text='Search Employee', font=('goudy old style', 12, 'bold'),
                                 bg='white')
        searchframe.place(x=220, y=0, width=550, height=60)
        # options

        cmb_search = ttk.Combobox(searchframe, value=('Select', 'Email', 'Name', 'ID'), textvariable=self.var_searchby,
                                  font=('goudy font style', 10), state='readonly', justify=CENTER)
        cmb_search.place(x=10, y=5, width=170)
        cmb_search.current(0)

        txt_search = Entry(searchframe, textvariable=self.var_searchtxt, font=('gouldy old style', 15),
                           bg='lightyellow')
        txt_search.place(x=190, y=2, width=170)
        button_search = Button(searchframe, text='Search', cursor='hand2', command=self.search,
                               font=('gouldy old style', 15),
                               bg='#F0B27A')
        button_search.place(x=370, y=2, width=170, height=28)
        # tittle
        title = Label(self.root, text='Employee Details/Register', font=('times of roman', 15, 'bold',), bg='#F7DC6F',
                      fg='black').place(x=30, y=65, height=30, width=1000)
        # content
        lbl_empid = Label(self.root, text="Emp I'D", font=('times of roman', 15, 'bold')).place(x=40, y=100, width=90)
        lbl_name = Label(self.root, text="Name", font=('times of roman', 15, 'bold')).place(x=370, y=100, width=90)
        lbl_contact = Label(self.root, text="Contact", font=('times of roman', 15, 'bold')).place(x=700, y=100,
                                                                                                  width=90)

        en_empid = Entry(self.root, textvariable=self.var_empid, font=('times of roman', 15, 'bold'),
                         bg='lightyellow')
        en_empid.place(x=135, y=100)

        en_name = Entry(self.root, textvariable=self.var_name, font=('times of roman', 15, 'bold'),
                        bg='lightyellow')
        en_name.place(x=465, y=100)

        en_contact = Entry(self.root, textvariable=self.var_contact, font=('times of roman', 15, 'bold'),
                           bg='lightyellow')
        en_contact.place(x=795, y=100)

        lbl_email = Label(self.root, text="Email", font=('times of roman', 15, 'bold')).place(x=40, y=150, width=90)
        lbl_gender = Label(self.root, text="Gender", font=('times of roman', 15, 'bold')).place(x=370, y=150, width=90)
        lbl_dob = Label(self.root, text="D.O.B.", font=('times of roman', 15, 'bold')).place(x=700, y=150, width=90)

        en_email = Entry(self.root, textvariable=self.var_email, font=('times of roman', 15, 'bold'),
                         bg='lightyellow')
        en_email.place(x=135, y=150)
        cmb_gender = ttk.Combobox(self.root, value=('Select', 'Male', 'Female', 'Other'), textvariable=self.var_gender,
                                  font=('goudy font style', 15), state='readonly', justify=CENTER)
        cmb_gender.place(x=465, y=150, width=222, height=30)
        cmb_gender.current(0)
        en_dob = Entry(self.root, textvariable=self.var_dob, font=('times of roman', 15, 'bold'),
                       bg='lightyellow')
        en_dob.place(x=795, y=150)

        lbl_doj = Label(self.root, text="D.O.J.", font=('times of roman', 15, 'bold')).place(x=40, y=200, width=90)
        lbl_password = Label(self.root, text="Password", font=('times of roman', 15, 'bold')).place(x=370, y=200,
                                                                                                    width=90)
        lbl_usertype = Label(self.root, text="UserType", font=('times of roman', 15, 'bold')).place(x=700, y=200,
                                                                                                    width=90)

        en_doj = Entry(self.root, textvariable=self.var_doj, font=('times of roman', 15, 'bold'),
                       bg='lightyellow')
        en_doj.place(x=135, y=200)
        en_password = Entry(self.root, textvariable=self.var_password, font=('times of roman', 15, 'bold'),
                            bg='lightyellow')
        en_password.place(x=465, y=200)
        en_usertype = Entry(self.root, textvariable=self.var_usertype, font=('times of roman', 15, 'bold'),
                            bg='lightyellow').place(x=795, y=200)
        cmb_usertype = ttk.Combobox(self.root, value=('Select', 'Admin', 'Employee'), textvariable=self.var_usertype,
                                    font=('goudy font style', 15), state='readonly', justify=CENTER)
        cmb_usertype.place(x=795, y=200, width=222, height=30)
        cmb_usertype.current(0)

        lbl_address = Label(self.root, text="Address", font=('times of roman', 15, 'bold')).place(x=40, y=250, width=90)
        lbl_salary = Label(self.root, text="Salary", font=('times of roman', 15, 'bold')).place(x=465, y=250, width=90)

        self.en_address = Text(self.root, font=('times of roman', 15, 'bold'), bg='lightyellow')
        self.en_address.place(x=135, y=250, width=322, height=50)
        en_salary = Entry(self.root, textvariable=self.var_salary, font=('times of roman', 15, 'bold'),
                          bg='lightyellow')
        en_salary.place(x=560, y=250)

        # buttons
        button_save = Button(self.root, text='Save', cursor='hand2', font=('gouldy old style', 15), command=self.add,
                             bg='#F0B27A')
        button_save.place(x=465, y=285, width=120, height=28)
        button_update = Button(self.root, text='Update', cursor='hand2', command=self.update,
                               font=('gouldy old style', 15),
                               bg='#DFFF00')
        button_update.place(x=590, y=285, width=120, height=28)
        button_delete = Button(self.root, text='Delete', command=self.delete, cursor='hand2',
                               font=('gouldy old style', 15),
                               bg='#DE3163')
        button_delete.place(x=715, y=285, width=120, height=28)
        button_clear = Button(self.root, text='Clear', cursor='hand2', command=self.clear,
                              font=('gouldy old style', 15),
                              bg='#6495ED')
        button_clear.place(x=655 + 185, y=285, width=120, height=28)
        # showing employee details
        emp_frame = Frame(self.root, bd=2, relief=RIDGE)
        emp_frame.place(x=0, y=340, relwidth=1, height=159)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        self.emp_table = ttk.Treeview(emp_frame, columns=(
            'eid', 'name', 'email', 'gender', 'contact', 'dob', 'doj', 'password', 'usertype', 'address', 'salary'),
                                      yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.emp_table.xview)
        scrolly.config(command=self.emp_table.yview)

        self.emp_table.heading('eid', text='Emp ID')
        self.emp_table.heading('name', text='Name')
        self.emp_table.heading('email', text='Email ID')
        self.emp_table.heading('gender', text='Gender')
        self.emp_table.heading('contact', text='Contact No.')
        self.emp_table.heading('dob', text='DOB')
        self.emp_table.heading('doj', text='DOJ')
        self.emp_table.heading('password', text='Password')
        self.emp_table.heading('usertype', text='UserType')
        self.emp_table.heading('address', text='Address')
        self.emp_table.heading('salary', text='Salary')

        self.emp_table['show'] = 'headings'

        self.emp_table.column('eid', width=90)
        self.emp_table.column('name', width=90)
        self.emp_table.column('email', width=150)
        self.emp_table.column('gender', width=90)
        self.emp_table.column('contact', width=90)
        self.emp_table.column('dob', width=90)
        self.emp_table.column('doj', width=90)
        self.emp_table.column('password', width=90)
        self.emp_table.column('usertype', width=90)
        self.emp_table.column('address', width=200)
        self.emp_table.column('salary', width=90)

        self.emp_table.pack(fill=BOTH, expand=1)
        self.emp_table.bind('<ButtonRelease-1>', self.getdata)
        self.show()

    # functions of dbms
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_empid.get() == '':
                messagebox.showerror('Error', "Employee id can't be blank", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'This employee ID already exist', parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee(eid, name , email , gender , contact , dob , doj, password, usertype , address , salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                        (self.var_empid.get(),
                         self.var_name.get(),
                         self.var_email.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.var_dob.get(),
                         self.var_doj.get(),
                         self.var_password.get(),
                         self.var_usertype.get(),
                         self.en_address.get('1.0', END),
                         self.var_salary.get(),
                         ))
                    con.commit()
                    messagebox.showinfo("Sucess", 'Employee added sucessfully', parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute('Select * from employee')
            rows = cur.fetchall()
            self.emp_table.delete(*self.emp_table.get_children())
            for row in rows:
                self.emp_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def getdata(self, ev):
        f = self.emp_table.focus()
        content = (self.emp_table.item(f))
        row = content['values']

        self.var_empid.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_password.set(row[7])
        self.var_usertype.set(row[8])
        self.en_address.delete('1.0', END)
        self.en_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_empid.get() == '':
                messagebox.showerror('Error', "Employee id can't be blank", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Employee ID', parent=self.root)
                else:
                    cur.execute(
                        "Update employee set name=? , email=? , gender=? , contact=? , dob=? , doj=?, password=?, usertype=? , address=? , salary=? where eid=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_password.get(),
                            self.var_usertype.get(),
                            self.en_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_empid.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Sucess", 'Updated sucessfully', parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_empid.get() == '':
                messagebox.showerror('Error', "Employee id can't be blank", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Employee ID', parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', 'Do you want to delete', parent=self.root)
                    if op == True:
                        cur.execute("delete from employee where eid=?", (self.var_empid.get(),) )
                        con.commit()
                        messagebox.showinfo('Delete', 'Delete Successfully', parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def clear(self):
        self.var_empid.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set("Select")
        self.var_contact.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_password.set('')
        self.var_usertype.set('Select')
        self.en_address.delete('1.0', END)
        self.var_salary.set('')
        self.var_searchtxt.set('')
        self.var_searchby.set('Select')
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == 'Select':
                messagebox.showerror('Error', "Search box can't be blank", parent=self.root)
            elif self.var_searchtxt.get() == '':
                messagebox.showerror('Error', "Search input required", parent=self.root)
            else:
                se = r'''Select * from employee where {} LIKE'%{}%' '''.format(self.var_searchby.get(),
                                                                               self.var_searchtxt.get())
                cur.execute(se)
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.emp_table.delete(*self.emp_table.get_children())
                    for row in rows:
                        self.emp_table.insert("", END, values=row)
                else:
                    messagebox.showerror('Error', "Record Not Found", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")


if __name__ == '__main__':
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
