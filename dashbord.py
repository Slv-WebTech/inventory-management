from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from employee import EmployeeClass
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass
from sales import SalesClass
import sqlite3
import os
import time

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1290x700+0+0')
        self.root.title(' Inventory Management System | Developed by GROUP 22')
        self.root.config(bg='white')

        # title
        self.icon_title = PhotoImage(file='images/logo1.png')
        title = Label(self.root, text='Welcome to Inventory Management System', image=self.icon_title, compound=LEFT,
                      font=('times new roman', 25, 'bold'), bg='grey', fg='white', anchor='w', padx=20).place(x=0,y=0,relwidth=1,height=60)
        # button
        btn_logout = Button(self.root, text="Logout", font=("Times new roman", 15, 'bold'), cursor='hand2',command=self.root.destroy).place(
            x=1100, y=10, height=40, width=100)
        # clock
        self.lbl_clock = Label(self.root,text='''Date:DD-MM-YYYY\t\t\t\t\t\t\t\t\t\t\tTime:HH:MM:SS''',
                               font=('times new roman', 15, 'bold'), bg='skyblue', fg='white')

        self.lbl_clock.place(x=0, y=60,relwidth=1,height=30)
        # left menu

        self.left_menu_icon = Image.open('images/ims1.png')
        self.left_menu_icon = self.left_menu_icon.resize((200, 200), Image.ANTIALIAS)
        self.left_menu_icon = ImageTk.PhotoImage(self.left_menu_icon)
        Leftmenu = Frame(self.root, bg='White', bd=2, relief=RIDGE).place(x=0, y=90, width=221, height=565)
        lbl_menulogo = Label(Leftmenu,bg='white', image=self.left_menu_icon)
        lbl_menulogo.place(x=0, y=90, width=220, height=230)

        labelmenu = Label(Leftmenu, text='   MENU', font=('times new roman', 25, 'bold'), bg='red', fg='white',
                          anchor='w', padx=20).place(x=0, y=320, width=220, height=40)
        self.icon_employee = PhotoImage(file='images/side.png')
        btn_employee = Button(Leftmenu, text="Employee", image=self.icon_employee, command=self.employee, compound=LEFT,
                              padx=10, anchor='w', font=("Times new roman", 15, 'bold'), cursor='hand2').place(x=0,
                                                                                                               y=362,
                                                                                                               height=40,
                                                                                                               width=220)
        btn_category = Button(Leftmenu, text="Category",command=self.category, image=self.icon_employee, compound=LEFT, padx=10, anchor='w',
                               font=("Times new roman", 15, 'bold'), cursor='hand2').place(x=0, y=407, height=40,
                                                                                           width=220)
        btn_product = Button(Leftmenu, text="Product",command=self.product, image=self.icon_employee, compound=LEFT, padx=10, anchor='w',
                             font=("Times new roman", 15, 'bold'), cursor='hand2').place(x=0, y=452, height=40,
                                                                                         width=220)
        btn_sales = Button(Leftmenu, text="Sales",command=self.sales, image=self.icon_employee, compound=LEFT, padx=10, anchor='w',
                           font=("Times new roman", 15, 'bold'), cursor='hand2').place(x=0, y=497, height=40, width=220)
        btn_supplier = Button(Leftmenu, text="Supplier",command=self.supplier, image=self.icon_employee,compound=LEFT,
                              padx=10, anchor='w', font=("Times new roman", 15, 'bold'), cursor='hand2').place(x=0,y=542,height=40, width=220)
        btn_exit = Button(Leftmenu, text="Exit", image=self.icon_employee, compound=LEFT,command=self.root.destroy, padx=10, anchor='w',
                          font=("Times new roman", 15, 'bold'), cursor='hand2').place(x=0, y=587, height=40, width=220)

        # content
        self.lbl_employee = Label(self.root, text='Total Employee\n[0]', bg='blue', fg='white',
                                  font=('goldy old style', 20, 'bold'))
        self.lbl_employee.place(x=250, y=150, height=150, width=300)
        self.lbl_category = Label(self.root, text='Total category\n[0]', bg='indigo', fg='white',
                                   font=('goldy old style', 20, 'bold'))
        self.lbl_category.place(x=580, y=150, height=150, width=300)
        self.lbl_product = Label(self.root, text='Total Product\n[0]', bg='violet', fg='white',
                                 font=('goldy old style', 20, 'bold'))
        self.lbl_product.place(x=910, y=150, height=150, width=300)
        self.lbl_sales = Label(self.root, text='Total Sales\n[0]', bg='orange', fg='white',
                               font=('goldy old style', 20, 'bold'))
        self.lbl_sales.place(x=250, y=330, height=150, width=300)
        self.lbl_supplier = Label(self.root, text='Supplier\n[0]', bg='pink', fg='white',
                                  font=('goldy old style', 20, 'bold'))
        self.lbl_supplier.place(x=580, y=330, height=150, width=300)

        # footer
        lbl_footer = Label(text='IMS | FOR TECHNICAL HELP CONTACT:******1234', bg='BLACK',
                           fg='white', font=('times of roman', 12, 'bold')).place(x=0, y=627, height=30, relwidth=1)
        self.update()
        self.time()

#animaton


    # linking employee page
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_win)
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_win)
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SalesClass(self.new_win)

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute('select * from product')
            produt=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(produt))}]')

            cur.execute('select * from category')
            cat = cur.fetchall()
            self.lbl_category.config(text=f'Total category\n[{str(len(cat))}]')

            cur.execute('select * from supplier')
            sup= cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(sup))}]')

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            cur.execute('select * from employee')
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')



        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}",parent=self.root)

    def time(self):
            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(
                text=f'''Inventory management system\t\t DATE:{str(date_)}\t\t TIME:{str(time_)}''')
            self.lbl_clock.after(200, self.time)


if __name__ == '__main__':
    root = Tk()
    obj = IMS(root)
    root.mainloop()
