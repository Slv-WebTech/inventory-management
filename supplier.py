from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1065x500+200+110')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')
        self.root.focus_force()
        root.resizable(False, False)
        # variable deceleration
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # search bar
        # searchframe = LabelFrame(self.root, text='Search supplier', font=('goudy old style', 12, 'bold'),
        #                          bg='white')
        # searchframe.place(x=220, y=0, width=550, height=60)
        # options
        lbl_search = Label(self.root, text='Invoice No.',bg='white',
                                  font=('goudy font style', 20))
        lbl_search.place(x=200, y=0, width=170)
        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=('gouldy old style', 15),
                           bg='lightyellow')
        txt_search.place(x=390, y=2, width=170)
        button_search = Button(self.root, text='Search', cursor='hand2', command=self.search,
                               font=('gouldy old style', 15),
                               bg='#F0B27A')
        button_search.place(x=590, y=2, width=170, height=28)
        # tittle
        title = Label(self.root, text='Supplier Details', font=('times of roman', 15, 'bold',), bg='#F7DC6F',
                      fg='black').place(x=30, y=65, height=30, width=1000)
        # content
        lbl_supplier_invoice = Label(self.root, text="Invoice No.",bg='white', font=('times of roman', 15, 'bold')).place(x=40,
                                                                                                               y=100,
                                                                                                               width=120)
        lbl_name = Label(self.root, text="Name", font=('times of roman', 15, 'bold'),bg='white').place(x=30, y=150, width=90)
        lbl_contact = Label(self.root, text="Contact", font=('times of roman', 15, 'bold'),bg='white').place(x=40, y=200,
                                                                                                  width=90)

        en_supplier_invoice = Entry(self.root, textvariable=self.sup_invoice, font=('times of roman', 15, 'bold'),
                                    bg='lightyellow')
        en_supplier_invoice.place(x=188, y=100)

        en_name = Entry(self.root, textvariable=self.var_name, font=('times of roman', 15, 'bold'),
                        bg='lightyellow')
        en_name.place(x=188, y=150)

        en_contact = Entry(self.root, textvariable=self.var_contact, font=('times of roman', 15, 'bold'),
                           bg='lightyellow')
        en_contact.place(x=188, y=200)

        lbl_discription = Label(self.root, text="Description", font=('times of roman', 15, 'bold'),bg='white').place(x=40, y=250,
                                                                                                          width=120)

        self.discription = Text(self.root, font=('times of roman', 15, 'bold'), bg='lightyellow')
        self.discription.place(x=188, y=250, width=250, height=50)

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
        # showing supplier details or TreeView

        sup_frame = Frame(self.root, bd=2, relief=RIDGE)
        sup_frame.place(x=0, y=340, relwidth=1, height=159)

        scrolly = Scrollbar(sup_frame, orient=VERTICAL)
        scrollx = Scrollbar(sup_frame, orient=HORIZONTAL)
        self.sup_table = ttk.Treeview(sup_frame, columns=(
            'invoice', 'name', 'contact', 'discription'),
                                      yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.sup_table.xview)
        scrolly.config(command=self.sup_table.yview)

        self.sup_table.heading('invoice', text='Invoice No.')
        self.sup_table.heading('name', text='Name')
        self.sup_table.heading('contact', text='Contact No.')
        self.sup_table.heading('discription', text='Discription')

        self.sup_table['show'] = 'headings'

        self.sup_table.column('invoice',  width=90)
        self.sup_table.column('name',width=90)
        self.sup_table.column('contact',width=90)
        self.sup_table.column('discription',width=90)

        self.sup_table.pack(fill=BOTH, expand=1)
        self.sup_table.bind('<ButtonRelease-1>', self.getdata)
        self.show()

    # functions of dbms
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.sup_invoice.get() == '':
                messagebox.showerror('Error', "Invoice can't be blank", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'This Invoice ID already exist', parent=self.root)
                else:
                    cur.execute(
                        "Insert into supplier(invoice, name , contact,discription) values(?,?,?,?)",
                        (self.sup_invoice.get(),
                         self.var_name.get(),
                         self.var_contact.get(),
                         self.discription.get('1.0', END),
                         ))
                    con.commit()
                    messagebox.showinfo("Sucess", 'Supplier added sucessfully', parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute('Select * from supplier')
            rows = cur.fetchall()
            self.sup_table.delete(*self.sup_table.get_children())
            for row in rows:
                self.sup_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def getdata(self, ev):
        f = self.sup_table.focus()
        content = (self.sup_table.item(f))
        row = content['values']

        self.sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.discription.delete('1.0', END)
        self.discription.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.sup_invoice.get() == '':
                messagebox.showerror('Error', "Invoivce No. can't be blank", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Invoice', parent=self.root)
                else:
                    cur.execute("Update supplier set name=? ,contact=?,discription=? where invoice=?",
                                (self.var_name.get(),self.var_contact.get(),self.discription.insert('1.0',END, row[3]), self.sup_invoice.get(),

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
            if self.sup_invoice.get() == '':
                messagebox.showerror('Error', "Invoice can't be blank", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Invoice No.', parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', 'Do you want to delete', parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?", (self.sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Delete Successfully', parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def clear(self):
        self.sup_invoice.set('')
        self.var_name.set('')
        self.var_contact.set('')
        self.discription.delete('1.0', END)
        self.var_searchtxt.set('')
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == '':
                messagebox.showerror('Error', "Invoice no. required", parent=self.root)
            else:
                cur.execute('Select * from supplier where invoice=?', (self.var_searchtxt.get(),))
                rows = cur.fetchone()
                if rows != None:
                    self.sup_table.delete(*self.sup_table.get_children())
                    for row in rows:
                        self.sup_table.insert("", END, values=row)
                else:
                    messagebox.showerror('Error', "Invalid Invoice Number", parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")


if __name__ == '__main__':
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
