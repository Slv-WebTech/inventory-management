from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1065x500+200+110')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')
        self.root.focus_force()
        root.resizable(False, False)
        #variables

        self.cat_list=[]
        self.sup_list=[]
        self.get_cat_sup()
        self.var_pid=StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        # product frame=======================
        # col 1
        product_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_frame.place(x=0, y=10, width=450, height=480)

        title = Label(product_frame, text='Manage_Product_Details', font=('times of roman', 15, 'bold',), bg='darkblue',
                      fg='white').pack(side=TOP, fill=X)

        lbl_category = Label(product_frame, text='Category', font=('times of roman', 15, 'bold',), bg='white').place(
            x=30, y=60)
        lbl_supplier = Label(product_frame, text='Supplier', font=('times of roman', 15, 'bold',), bg='white').place(
            x=30, y=110)
        lbl_product_name = Label(product_frame, text='Name', font=('times of roman', 15, 'bold',), bg='white').place(
            x=30, y=160)
        lbl_price = Label(product_frame, text='Price', font=('times of roman', 15, 'bold',), bg='white').place(x=30,
                                                                                                               y=210)
        lbl_qty = Label(product_frame, text='Quantity', font=('times of roman', 15, 'bold',), bg='white').place(x=30,
                                                                                                                y=260)
        lbl_status = Label(product_frame, text='Status', font=('times of roman', 15, 'bold',), bg='white').place(x=30,
                                                                                                                 y=310)

        # col 2
        cmb_cat = ttk.Combobox(product_frame, value=self.cat_list, textvariable=self.var_cat,
                               font=('goudy font style', 10), state='readonly', justify=CENTER)
        cmb_cat.place(x=150, y=68, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_frame, value=self.sup_list, textvariable=self.var_sup,
                               font=('goudy font style', 10), state='readonly', justify=CENTER)
        cmb_sup.place(x=150, y=118, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_frame, textvariable=self.var_name, font=('goudy font style', 10),
                         bg="lightyellow").place(x=150, y=160, width=200, height=30)
        txt_price = Entry(product_frame, textvariable=self.var_price, font=('goudy font style', 10),
                          bg="lightyellow").place(x=150, y=210, width=200, height=30)
        txt_quantity = Entry(product_frame, textvariable=self.var_qty, font=('goudy font style', 10),
                             bg="lightyellow").place(x=150, y=260, width=200, height=30)

        cmb_status = ttk.Combobox(product_frame, value=('Active', 'Inactive'), textvariable=self.var_status,
                                  font=('goudy font style', 10), state='readonly', justify=CENTER)
        cmb_status.place(x=150, y=310, width=200, height=30)
        cmb_status.current(0)

        # ============buttons===============
        button_save = Button(self.root, text='Save', cursor='hand2', font=('gouldy old style', 15), command=self.add,
                             bg='#F0B27A')
        button_save.place(x=10, y=400, width=100, height=40)

        button_update = Button(self.root, text='Update', cursor='hand2', command=self.update,
                               font=('gouldy old style', 15),
                               bg='#DFFF00')
        button_update.place(x=120, y=400, width=100, height=40)

        button_delete = Button(self.root, text='Delete', command=self.delete, cursor='hand2',
                               font=('gouldy old style', 15),
                               bg='#DE3163')
        button_delete.place(x=230, y=400, width=100, height=40)

        button_clear = Button(self.root, text='Clear', cursor='hand2', command=self.clear,
                              font=('gouldy old style', 15),
                              bg='#6495ED')
        button_clear.place(x=340, y=400, width=100, height=40)

        # =======search--frame===========

        searchframe = LabelFrame(self.root, text='Search Product', font=('goudy old style', 12, 'bold'),
                                 bg='white')
        searchframe.place(x=480, y=10, width=600, height=80)
        # options

        cmb_search = ttk.Combobox(searchframe, value=('Select', 'Category', "Supplier", "Name"),
                                  textvariable=self.var_searchby,
                                  font=('goudy font style', 10), state='readonly', justify=CENTER)
        cmb_search.place(x=10, y=5, width=170, height=30)
        cmb_search.current(0)

        txt_search = Entry(searchframe, textvariable=self.var_searchtxt, font=('gouldy old style', 15),
                           bg='lightyellow')
        txt_search.place(x=190, y=4, width=170, height=30)
        button_search = Button(searchframe, text='Search', cursor='hand2', command=self.search,
                               font=('gouldy old style', 15),
                               bg='#F0B27A')
        button_search.place(x=370, y=3, width=170, height=28)

        # showing employee details
        P_frame = Frame(self.root, bd=2, relief=RIDGE)
        P_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(P_frame, orient=VERTICAL)
        scrollx = Scrollbar(P_frame, orient=HORIZONTAL)
        self.Product_table = ttk.Treeview(P_frame, columns=(
            'pid', 'Category', 'Supplier', 'name', 'price', 'qty', 'status'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Product_table.xview)
        scrolly.config(command=self.Product_table.yview)

        self.Product_table.heading('pid', text='Product ID')
        self.Product_table.heading('Category', text='Category')
        self.Product_table.heading('Supplier', text='Supplier')
        self.Product_table.heading('name', text='Name')
        self.Product_table.heading('price', text='Price')
        self.Product_table.heading('qty', text='Quantity')
        self.Product_table.heading('status', text='Status')

        self.Product_table['show'] = 'headings'

        self.Product_table.column('pid', width=90)
        self.Product_table.column('Category', width=90)
        self.Product_table.column('Supplier', width=150)
        self.Product_table.column('name', width=90)
        self.Product_table.column('price', width=90)
        self.Product_table.column('qty', width=90)
        self.Product_table.column('status', width=90)

        self.Product_table.pack(fill=BOTH, expand=1)
        self.Product_table.bind('<ButtonRelease-1>', self.getdata)
        self.show()

    # =========================
    def get_cat_sup(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            self.cat_list.append('Empty')
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append('Select')
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            self.sup_list.append('Empty')
            if len(sup)>0:
                del  self.sup_list[:]
                self.sup_list.append('Select')
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == 'Select' or self.var_cat.get() =='Empty' or self.var_sup.get() == 'Select' or self.var_sup.get() =='Empty':
                messagebox.showerror('Error', " This Field can't be blank", parent=root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'This Product ID already exist', parent=self.root)
                else:
                    cur.execute(
                        "Insert into product( Category, Supplier, name, price, qty, status) values(?,?,?,?,?,?)",
                        (
                         self.var_cat.get(),
                         self.var_sup.get(),
                         self.var_name.get(),
                         self.var_price.get(),
                         self.var_qty.get(),
                         self.var_status.get(),

                         ))
                    con.commit()
                    messagebox.showinfo("Sucess", 'Product added sucessfully', parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute('Select * from product')
            rows = cur.fetchall()
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def getdata(self, ev):
        f = self.Product_table.focus()
        content = (self.Product_table.item(f))
        row = content['values']

        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])


    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == 'Select' or self.var_cat.get() == 'Empty' or self.var_sup.get() == 'Select' or self.var_sup.get() == 'Empty':
                messagebox.showerror('Error', "This Fields can't be blank", parent=root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Name ID', parent=self.root)
                else:
                    cur.execute(
                        "Update product set Category=?, Supplier=?, name=?, price=?, qty=?, status=? where pid=?",
                        (
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get(),
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
            if self.var_cat.get() == 'Select' or self.var_cat.get() =='Empty' or self.var_sup.get() == 'Select' or self.var_sup.get() =='Empty':
                messagebox.showerror('Error', "Product id can't be blank", parent=root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Product Nmae', parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', 'Do you want to delete', parent=self.root)
                    if op == True:
                        cur.execute("delete from product where name=?", (self.var_name.get(),) )
                        con.commit()
                        messagebox.showinfo('Delete', 'Delete Sucessfully', parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def clear(self):
        self.var_pid.set('')
        self.var_name.set('')
        self.var_status.set('Active')
        self.var_cat.set("Select")
        self.var_sup.set('Select')
        self.var_price.set('')
        self.var_qty.set('')
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == 'Select':
                messagebox.showerror('Error', "Search box can't be blank", parent=self.root)
            elif self.var_searchtxt.get() == '':
                messagebox.showerror('Error', "Search input required", parent=self.root)
            else:
                se = r'''Select * from product where {} LIKE'%{}%' '''.format(self.var_searchby.get(),
                                                                               self.var_searchtxt.get())
                cur.execute(se)
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.Product_table.delete(*self.Product_table.get_children())
                    for row in rows:
                        self.Product_table.insert("", END, values=row)
                else:
                    messagebox.showerror('Error', "Record Not Found", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")


if __name__ == '__main__':
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
