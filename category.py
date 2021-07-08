from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class CategoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1065x500+200+110')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')
        self.root.focus_force()
        root.resizable(False, False)
        # variable
        self.var_catid=StringVar()
        self.var_name=StringVar()
        # title
        title = Label(self.root, text='Manage Product Category', font=('times of roman', 25, 'bold',), bg='#F7DC6F',
                      bd=3, relief=RIDGE,
                      fg='black')
        title.pack(side=TOP, fill=X, padx=15, pady=10)
        lbl_name = Label(self.root, text='Enter Category Name', font=('times of roman', 20, 'bold',), bg='white',
                         fg='black')
        lbl_name.place(x=40, y=70)

        en_name = Entry(self.root, textvariable=self.var_name, font=('times of roman', 15, 'bold',), bg='lightyellow',
                        fg='black')
        en_name.place(x=340, y=70,width=310)
        button_add = Button(self.root, text='Add', cursor='hand2', command=self.add,font=('gouldy old style', 15),
                             bg='#F0B27A')
        button_add.place(x=360, y=120, width=120, height=28)
        button_delete = Button(self.root, text='Delete', cursor='hand2',command=self.delete, font=('gouldy old style', 15),
                            bg='#F0B27c')
        button_delete.place(x=510, y=120, width=120, height=28)

        #Tree view or category details

        cat_frame = Frame(self.root, bd=2, relief=RIDGE)
        cat_frame.place(x=685,y=70,relwidth=0.35, height=100)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)
        self.cat_table = ttk.Treeview(cat_frame, columns=(
            'cid', 'name'),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cat_table.xview)
        scrolly.config(command=self.cat_table.yview)

        self.cat_table.heading('cid', text='Category ID')
        self.cat_table.heading('name', text='Name')


        self.cat_table['show'] = 'headings'

        self.cat_table.column('cid',  width=90)
        self.cat_table.column('name',width=90)

        self.cat_table.pack(fill=BOTH, expand=1)
        self.cat_table.bind('<ButtonRelease-1>', self.getdata)
        self.show()
        #images
        self.icon1 = Image.open('images/cat.jpg')
        self.icon1 = self.icon1.resize((500, 280), Image.ANTIALIAS)
        self.icon1 = ImageTk.PhotoImage(self.icon1)
        self.lab_icon1=Label(self.root,image=self.icon1,bd=2,relief=RAISED)
        self.lab_icon1.place(x=20,y=190)

        self.icon2 = Image.open('images/category.jpg')
        self.icon2 = self.icon2.resize((500, 280), Image.ANTIALIAS)
        self.icon2 = ImageTk.PhotoImage(self.icon2)
        self.lab_icon2 = Label(self.root, image=self.icon2, bd=2, relief=RAISED)
        self.lab_icon2.place(x=540, y=190)
    #function of database
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == '':
                messagebox.showerror('Error', "Category Name can't be blank", parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'Category already exist', parent=self.root)
                else:
                    cur.execute("Insert into category( name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Sucess",'category added Successfully', parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_catid.get() == '':
                messagebox.showerror('Error', "Category Name can't be blank", parent=self.root)
            else:
                cur.execute("Select * from category where name=?", (self.var_catid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Name not exist', parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', 'Do you want to delete', parent=self.root)
                    if op == True:
                        cur.execute("delete from category where name=?",(self.var_catid.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Delete Successfully', parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute('Select * from category')
            rows = cur.fetchall()
            self.cat_table.delete(*self.cat_table.get_children())
            for row in rows:
                self.cat_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def getdata(self, ev):
        f = self.cat_table.focus()
        content = (self.cat_table.item(f))
        row = content['values']
        self.var_catid.set(row[1])
        self.var_name.set(row[1])

if __name__ == '__main__':
    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()
