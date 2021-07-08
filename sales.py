from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os


class SalesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1065x500+200+110')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')
        self.root.focus_force()
        root.resizable(False, False)
        # variable
        self.var_invoice = StringVar()
        self.bill = []
        # title
        title = Label(self.root, text='View Coustomer bills', font=('times of roman', 25, 'bold',), bg='#F7DC6d',
                      bd=3, relief=RIDGE,
                      fg='black')
        title.pack(side=TOP, fill=X, padx=15, pady=10)
        invoice = Label(self.root, text='Invoice No.', font=('times of roman', 15, 'bold',),
                        bd=3, relief=RIDGE,
                        fg='black')
        invoice.place(x=15, y=70)
        en_invoice = Entry(self.root, textvariable=self.var_invoice, font=('times of roman', 15, 'bold',),
                           bg='lightyellow',
                           fg='black')
        en_invoice.place(x=140, y=72.5)
        # button
        button_search = Button(self.root, text='Search', command=self.search, cursor='hand2',
                               font=('gouldy old style', 15),
                               bg='lightblue')
        button_search.place(x=380, y=70, width=120, height=28)
        button_clear = Button(self.root,  text='Clear', cursor='hand2',command=self.clear,
                              font=('gouldy old style', 15),
                              bg='grey')
        button_clear.place(x=510, y=70, width=120, height=28)
        # frame
        sales_frame = Frame(self.root, bd=2, relief=RIDGE)
        sales_frame.place(x=15, y=120, width=210, height=350)
        scrolly = Scrollbar(sales_frame, orient=VERTICAL, bg='white')
        scrolly.pack(side=RIGHT, fill=Y)

        self.sales_list = Listbox(sales_frame, bd=3, font=('times of roman', 15, 'bold',), relief=RIDGE, fg='black',
                                  bg='white')
        self.sales_list.place(x=0, y=0, width=190, height=345)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.bind('<ButtonRelease>', self.getdata)

        bill_frame = Frame(self.root, bd=2, relief=RIDGE)
        bill_frame.place(x=15 + 226, y=120, width=400, height=350)
        bill_label = Label(bill_frame, text='Customer Billing', font=('times of roman', 15, 'bold',),
                           bd=3, relief=RIDGE,
                           fg='black', bg='lightpink')
        bill_label.pack(fill=X)
        self.bill_list = Text(bill_frame, bd=3,  relief=RIDGE, font=('times of roman', 10, 'bold',),fg='black',width=405)

        scrollX = Scrollbar(bill_frame, orient=HORIZONTAL)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollX.config(command=self.bill_list.xview)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_list.yview)

        self.bill_list.pack(fill=BOTH, expand=2)

        # image
        self.icon1 = Image.open('images/bg.png')
        self.icon1 = self.icon1.resize((400, 380), Image.ANTIALIAS)
        self.icon1 = ImageTk.PhotoImage(self.icon1)
        self.lab_icon1 = Label(self.root, image=self.icon1, bd=0, bg='white', relief=RAISED)
        self.lab_icon1.place(x=650, y=80)
        self.show()

    # function
    def show(self):
        del self.bill[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill.append(i.split('.')[0])

    def getdata(self, ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        self.bill_list.delete('1.0', END)
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_list.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == '':
            messagebox.showerror('Error', "Invoice No. Required", parent=self.root)
        else:
            if self.var_invoice.get in self.bill:
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_list.delete('1.0', END)
                for i in fp:
                    self.bill_list.insert(END, i)
                fp.close()
            else:
                messagebox.showerror('Error', "Invoice No. Not Found", parent=self.root)

    def clear(self):
        self.show()
        self.var_invoice.set('')
        self.bill_list.delete('1.0', END)


if __name__ == '__main__':
    root = Tk()
    obj = SalesClass(root)
    root.mainloop()
