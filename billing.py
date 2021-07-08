from tkinter import *
from tkinter import ttk, messagebox
import os
import tempfile
import sqlite3
import time

class BillClass:


    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x700+0+0")
        self.root.title("Inventory management system | Billing Page")
        self.root.config(bg="white")

        self.cart_list=[]
        self.chk_print=0

        # ===title===
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory management system ", image=self.icon_title,
                      compound=LEFT, font=("times new roman", 30, "bold"),
                      bg="darkblue", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=60)
        # ===now we will create logout button==
        btn_logout = Button(self.root, text="LOGOUT", font=("Helveticaa", 15, "bold"),command=self.root.destroy,
                            bg="white", cursor="hand2").place(x=1100, y=10, height=40, width=100)

        # CLOCK
        self.lbl_clk = Label(self.root,
                             text='''Welcome to Inventory management system\t\t DATE:DD-MM-YY\t\t TIME:HH-MM-SS''',
                             font=("times new roman", 13),  anchor="w",padx="200",
                             bg="#F7DC6d", fg="black")
        self.lbl_clk.place(x=0, y=60, relwidth=1, height=30)
        # Product---Frame


        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=1, y=92, width=361, height=560)
        pTitle = Label(ProductFrame1, text="All Products", font=("goudy old style", 15, " bold"), bg="#262626",
                       fg="white").pack(side=TOP, fill=X)

        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=32, width=350, height=100)

        lbl_search = Label(ProductFrame2, text="Search Product", font=("times new roman", 19, "bold"),
                           bg="white", fg="green").place(x=0, y=0,width=200)
        lbl_search = Label(ProductFrame2, text="Product name", font=("times new roman", 19, "bold"), bg="white").place(
            x=12, y=30)

        self.var_search = StringVar()
        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 19, "bold"),
                           bg="lightyellow").place(x=12, y=63, width=200, height=29)
        button_search = Button(ProductFrame2, text="Search", font=("times new roman", 19, "bold"), bg="grey",command=self.search,
                               fg="white", cursor="hand2").place(x=218, y=58, width=120, height=30)
        button_show_all = Button(ProductFrame2, text="Show All", font=("times new roman", 19, "bold"), bg="grey",command=self.show,
                                 fg="white", cursor="hand2").place(x=218, y=15, width=120, height=30)
      #======Product Deatils frame===============

        Product_frame = Frame(ProductFrame1, bd=2, relief=RIDGE)
        Product_frame.place(x=2, y=134, width=350, height=390)

        scrolly = Scrollbar(Product_frame, orient=VERTICAL)
        scrollx = Scrollbar(Product_frame, orient=HORIZONTAL)
        self.Product_table = ttk.Treeview(Product_frame, columns=(
            'pid', 'name', 'price', 'qty', 'status'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Product_table.xview)
        scrolly.config(command=self.Product_table.yview)

        self.Product_table.heading('pid', text='Product_id')
        self.Product_table.heading('name', text='Name')
        self.Product_table.heading('price', text='price')
        self.Product_table.heading('qty', text='Quantity')
        self.Product_table.heading('status', text='Status')

        self.Product_table['show'] = 'headings'

        self.Product_table.column('pid', width=30)
        self.Product_table.column('name', width=90)
        self.Product_table.column('price', width=40)
        self.Product_table.column('qty', width=40)
        self.Product_table.column('status', width=50)

        self.Product_table.pack(fill=BOTH, expand=1)
        self. Product_table.bind('<ButtonRelease-1>', self.getdata)

        lbl_note = Label(ProductFrame1, text="   Note: 'Enter 0 quantity  to remove product from the cart",
                         font=("goudy old style", 11), bg="black", fg="red", anchor="w").pack(side=BOTTOM, fill=X)

        # =======customer---------Frame=================
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=362, y=92, width=500, height=120)

        Customer_title = Label(CustomerFrame, text="Customer_Details", font=("goudy old style", 20, " bold"),
                               bg="lightgrey").pack(side=TOP, fill=BOTH)

        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 19), bg="white").place(x=0, y=40)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("times new roman", 19, "bold"),
                         bg="lightyellow").place(x=130, y=45, width=250, height=30)

        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("times new roman", 19), bg="white").place(x=0,
                                                                                                               y=78)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 19, "bold"),
                        bg="lightyellow").place(x=130, y=78, width=250, height=30)
        # ============cal_cart_Frame===========

        Cal_cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_cart_Frame.place(x=362, y=92+122, width=500, height=430)

        # =============Calculator -------Frame ============
        self.var_cal_input = StringVar()
        Cal_Frame = Frame(Cal_cart_Frame, bd=4, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=5, width=282, height=338)

        txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input,
                              font=("arial", 15, "bold"), width=23, bd=10, relief=GROOVE,justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(Cal_Frame, text="7", font=("arial", 15, "bold"), command=lambda: self.get_input(7), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text="8", font=("arial", 15, "bold"), command=lambda: self.get_input(8), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text="9", font=("arial", 15, "bold"), command=lambda: self.get_input(9), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text="+", font=("arial", 15, "bold"), command=lambda: self.get_input("+"), width=4,
                         bd=5, pady=10, cursor="hand2").grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text="4", font=("arial", 15, "bold"), command=lambda: self.get_input(4), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text="5", font=("arial", 15, "bold"), command=lambda: self.get_input(5), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text="6", font=("arial", 15, "bold"), command=lambda: self.get_input(6), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=2, column=2)
        btn_subtract = Button(Cal_Frame, text="-", font=("arial", 15, "bold"), command=lambda: self.get_input("-"),
                              width=4, bd=5, pady=10, cursor="hand2").grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text="1", font=("arial", 15, "bold"), command=lambda: self.get_input(1), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text="2", font=("arial", 15, "bold"), command=lambda: self.get_input(2), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text="3", font=("arial", 15, "bold"), command=lambda: self.get_input(3), width=4,
                       bd=5, pady=10, cursor="hand2").grid(row=3, column=2)
        btn_multiply = Button(Cal_Frame, text="*", font=("arial", 15, "bold"), command=lambda: self.get_input("*"),
                              width=4, bd=5, pady=10, cursor="hand2").grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text="0", font=("arial", 15, "bold"), command=lambda: self.get_input(0), width=4,
                       bd=5, pady=20, cursor="hand2").grid(row=4, column=0)
        btn_c = Button(Cal_Frame, text="c", font=("arial", 15, "bold"), width=4, bd=5, pady=20,command=self.clear_cal,
                       cursor="hand2").grid(row=4, column=1)
        btn_equal = Button(Cal_Frame, text="=", font=("arial", 15, "bold"), width=4, bd=5,command=self.perform_cal,
                           pady=20, cursor="hand2").grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text="/", font=("arial", 15, "bold"), command=lambda: self.get_input('/'), width=4,
                         bd=5, pady=20, cursor="hand2").grid(row=4, column=3)

        Cart_frame = Frame(Cal_cart_Frame, bd=2, relief=RIDGE)
        Cart_frame.place(x=282+7, y=5, width=208, height=338)
        self.cal_title = Label(Cart_frame, text=" Cart Product:[0]", font=("times new roman", 19), bg="white",
                          fg="black")
        self.cal_title.pack(side=TOP, fill=X)

        scrolly = Scrollbar(Cart_frame, orient=VERTICAL)
        scrollx = Scrollbar(Cart_frame, orient=HORIZONTAL)
        self.Cart_table = ttk.Treeview(Cart_frame, columns=('pid', 'name', 'price', 'qty','stock'),
                                       yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Cart_table.xview)
        scrolly.config(command=self.Cart_table.yview)

        self.Cart_table.heading('pid', text='Product id')
        self.Cart_table.heading('name', text='Name')
        self.Cart_table.heading('price', text='Price')
        self.Cart_table.heading('qty', text='Quantity')
        self.Cart_table.heading('stock', text='Stock')

        self.Cart_table['show'] = 'headings'

        self.Cart_table.column('pid', width=80)
        self.Cart_table.column('name', width=100)
        self.Cart_table.column('price', width=90)
        self.Cart_table.column('qty', width=90)
        self.Cart_table.column('stock', width=90)


        self.Cart_table.pack(fill=BOTH, expand=1)
        self.  Cart_table.bind('<ButtonRelease-1>', self.getdata)

        # ==============Add cart widget Frame===========
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        Add_cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Add_cart_Frame.place(x=362, y=559, width=500, height=92)

        lbl_p_name = Label(Add_cart_Frame, text="Product Name", font=("times new roman", 15), bg="white").place(x=0,
                                                                                                                y=0)
        txt_p_name = Entry(Add_cart_Frame, textvariable=self.var_pname, font=("times new roman", 15, "bold"),
                           bg="lightyellow").place(x=0, y=30, width=150, height=22)

        lbl_p_price_ = Label(Add_cart_Frame, text="Price per Quantity", font=("times new roman", 15), bg="white").place(
            x=155, y=0)
        txt_p_price = Entry(Add_cart_Frame, textvariable=self.var_price, font=("times new r oman", 14, "bold"),
                            bg="lightyellow").place(x=155, y=30, width=180, height=22)

        lbl_p_qty = Label(Add_cart_Frame, text="   Quantity", font=("times new roman", 15), bg="white").place(x=155+185, y=0)
        txt_p_qty = Entry(Add_cart_Frame, textvariable=self.var_qty, font=("times new roman", 14, "bold"),
                          bg="lightyellow").place(x=155+185, y=30, width=140, height=22)

        self.lbl_instock = Label(Add_cart_Frame, text="In Stock", font=("times new roman", 15), bg="white")
        self.lbl_instock.place(x=0, y=55)

        # =====Button=====

        Button_clear_cart = Button(Add_cart_Frame, text="Clear", font=("times new roman", 19), bg="lightgray",command=self.clear_cart,
                                   cursor="hand2").place(x=140, y=55, width=150, height=30)
        Button_Add_update_cart = Button(Add_cart_Frame, text="Add/Update", font=("times new roman", 19),command=self.update_cart,
                                        bg="orange", cursor="hand2").place(x=300, y=55, width=150, height=30)

        # ===============Billing Frame or area ================

        Bill_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Bill_Frame.place(x=865, y=92, width=405, height=405)

        BTitle = Label(Bill_Frame, text="Customer Bill", font=("goudy old style", 20, " bold"), bg="#262626",
                       fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(Bill_Frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(Bill_Frame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # ==================Billing_frame and button==================
        Bill_menu_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Bill_menu_frame.place(x=865, y=500, width=405, height=145)

        self.lbl_amt = Label(Bill_menu_frame, text=" BillAmt\n[0]", font=("times new roman", 19), bg="#3f51b5",
                             fg="white")
        self.lbl_amt.place(x=2, y=5, width=124, height=60)

        self.lbl_discount = Label(Bill_menu_frame, text="Discount\n[5%]", font=("times new roman", 19), bg="#8bc34a",
                                  fg="white")
        self.lbl_discount.place(x=130, y=5, width=120, height=60)

        self.lbl_net_pay = Label(Bill_menu_frame, text="Net Pay\n[0]", font=("times new roman", 19), bg="#607d8b",
                                 fg="white")
        self.lbl_net_pay.place(x=256, y=5, width=140, height=60)

        button_print = Button(Bill_menu_frame, text="Print", font=("times new roman", 19), bg="#3f51b5",command=self.print, fg="white")
        button_print.place(x=2, y=66, width=124, height=70)

        button_clearall = Button(Bill_menu_frame, text="Clear all", font=("times new roman", 19), bg="#8bc34a",command=self.clear_all,
                                 fg="white")
        button_clearall.place(x=130, y=66, width=120, height=70)

        button_generate = Button(Bill_menu_frame, text="Generate/Save",command=self.gernate_bill, font=("times new roman", 15), bg="#607d8b",
                                 fg="white")
        button_generate.place(x=256, y=66, width=140, height=70)

        self.show()
        self.time()


#function
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            cur.execute("Select pid,name,price,qty,status from product where status='Active'")
            rows = cur.fetchall()
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == '':
                messagebox.showerror('Error', "Search input required", parent=self.root)
            else:
                se = r'''Select pid,name,price,qty,status from product where name LIKE'%{}%' '''.format(
                                                                               self.var_search.get())
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

    def getdata(self, ev):
        f = self.Product_table.focus()
        content = (self.Product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_stock.set(row[3])
        self.lbl_instock.config(text=f"In Stock[{str(row[3])}]")
        self.var_qty.set('1')
    def billupdate(self):
        self.bill_amt=0
        self.net_pay=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))

        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount


        self.lbl_amt.config(text=f'Bill Amt(Rs)\n[{str(self.bill_amt)}]')
        self.lbl_net_pay.config(text=f'Net Amt(Rs)\n[{str(self.net_pay)}]')
        a=len(self.cart_list)
        self.cal_title.config(text=f'Total Product:[{str(a)}]')

    def update_cart(self):
        if self.var_pname.get() == '':
            messagebox.showerror("Error", "Product Name  and Quantity Can't be blank", parent=self.root)

        elif int(self.var_qty.get())>int(self.var_stock.get()):

            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)

        else:
            if self.var_qty.get() == '':
                messagebox.showerror("Error", "Quantity Can't be blank", parent=self.root)

            else:
                # price_cal = float(int(self.var_qty.get())*float(self.var_price.get()))
                price_cal = self.var_price.get()
                cartdata=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]

                #update cart
                present='no'
                index_=0
                for row in self.cart_list:
                    if self.var_pid.get()==row[0]:
                        present='yes'
                        break
                    index_+=1
                if present=='yes':
                    op=messagebox.askyesno('Confirm',"product already exist\nDo you want to update or remove",parent=self.root)
                    if op==True:
                        if self.var_qty.get()=='0':
                            self.cart_list.pop(index_)
                        else:
                            # self.cart_list[index_][2]=price_cal
                            self.cart_list[index_][3]=self.var_qty.get()
                else:
                    self.cart_list.append(cartdata)

                self.showcart()
                self.billupdate()

    def showcart(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            self.Cart_table.delete(*self.Cart_table.get_children())
            for row in self.cart_list:
                self.Cart_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")


    def gernate_bill(self):
        if len(self.cart_list)<=0:
            messagebox.showerror("Error", "Cart is empty", parent=self.root)
        elif self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error", "Customer Name and Number are required", parent=self.root)
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved','Bill Saved Successfully',parent=self.root)
            self.chk_print=1
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top=f'''
\t\tInventory Billing
   Phone No. :- 95221*****, Gwalior-474001
{str('='*46)}
Customer Name: {self.var_cname.get()}
Ph No.: {self.var_contact.get()}
Bill No. {str(self.invoice)}\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str('='*46)}
Product Name\t\t\tQty\tPrice
{str('='*46)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top)


    def bill_middle(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                q=row[3]
                qty=(int(row[4]) - int(row[3]))
                price=float(int(row[2])*int(row[3]))
                price=str(price)

                if int(q) == int(row[4]):
                    status = 'Inactive'

                if int(q) != int(row[4]):
                    status = 'Active'
                cur.execute(
                    "Update product set qty=?, status=? where pid=?", (qty,status, pid,))
                con.commit()

                self.txt_bill_area.insert(END,'\n'+name+'\t\t\t'+q+"\tRs."+price)

            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to:{str(ex)}")

    def bill_bottom(self):
        bill_bottom=f'''
{str('='*46)}
Bill Amt\t\t\tRs{self.bill_amt}
Discount\t\t\tRs{self.discount}
Net Amt\t\t\tRs{self.net_pay}
{str('='*46)}
        '''

        self.txt_bill_area.insert(END, bill_bottom)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_stock.set('')
        self.lbl_instock.config(text=f"In Stock")
        self.var_qty.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cal_title.config(text=f'Total Product')
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.showcart()
        self.chk_print=0


    def time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clk.config(text=f'''Welcome to Inventory management system\t\t DATE:{str(date_)}\t\t TIME:{str(time_)}''')
        self.lbl_clk.after(200,self.time)

    def print(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Printing...",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print", "Plese generate bill to print", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()