import os
from tkinter import *
import math, random
from tkinter import messagebox

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = '#074463'
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman",30,"bold"), pady=2).pack(fill=X)

        # ======Cosmetics Variables
        self.soap = IntVar()
        self.cream = IntVar()
        self.wash = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()
        self.shampoo = IntVar()

        # ======Grocery Variables
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ======Drinks Variables
        self.maza = IntVar()
        self.cock = IntVar()
        self.thumbsup = IntVar()
        self.frooti = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ======Total Product Prices & Tax Variables======
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_drinks = StringVar()

        self.cosmetics_tax = StringVar()
        self.grocery_tax = StringVar()
        self.drinks_tax = StringVar()

        # ======Customer Details=======
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ==============Customer Details Frame===================
        f1 = LabelFrame(self.root,bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 18, "bold"), fg='gold', bg=bg_color)
        f1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(f1, text="Customer Name", bg=bg_color, fg='white', font=("times new roman", 18, 'bold')).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(f1,textvariable=self.c_name, bd=2, width=18, font=("arial 15"), relief=SUNKEN).grid(row=0, column=1, padx=5, pady=10)

        cphone_lbl = Label(f1, text="Phone Number", bg=bg_color, fg='white', font=("times new roman", 18, 'bold')).grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(f1,textvariable=self.c_phone, bd=2, width=18, font=("arial 15"), relief=SUNKEN).grid(row=0, column=3, padx=5, pady=10)

        cbill_lbl = Label(f1, text="Bill No.", bg=bg_color, fg='white', font=("times new roman", 18, 'bold')).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(f1,textvariable=self.search_bill, bd=2, width=18, font=("arial 15"), relief=SUNKEN).grid(row=0, column=5, padx=5, pady=10)

        bill_search_btn = Button(f1, command=self.search_saved_bill, text="Search",bd=2, font=("arial 10 bold")).grid(row=0, column=6, padx=7, pady=7)

        # ==============Cosmetics Frame====================
        f2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 18, "bold"), fg='gold', bg=bg_color)
        f2.place(x=5, y=180, width=325, height=380)

        bath_soap_lbl = Label(f2, text="Bath Soap", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        bath_soap_txt = Entry(f2, textvariable=self.soap, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(f2, text="Face Cream", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        face_cream_txt = Entry(f2,textvariable=self.cream, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        face_wash_lbl = Label(f2, text="Face Wash", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        face_wash_txt = Entry(f2,textvariable=self.wash, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        hair_gel_lbl = Label(f2, text="Hair Gel", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        hair_gel_txt = Entry(f2,textvariable=self.gel, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        body_lotion_lbl = Label(f2, text="Body Lotion", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        body_lotion_txt = Entry(f2,textvariable=self.lotion, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        shampoo_lbl = Label(f2, text="Shampoo", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        shampoo_txt = Entry(f2,textvariable=self.shampoo, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ==============Grocery Frame====================
        f3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 18, "bold"),
                        fg='gold', bg=bg_color)
        f3.place(x=325, y=180, width=325, height=380)

        rice_lbl = Label(f3, text="Rice", bg=bg_color, font=('times new roman', 16, 'bold'),
                              fg='lightgreen').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        rice_txt = Entry(f3,textvariable=self.rice, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                         pady=10)

        food_oil_lbl = Label(f3, text="Food Oil", bg=bg_color, font=('times new roman', 16, 'bold'),
                               fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        food_oil_txt = Entry(f3,textvariable=self.food_oil, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=1, column=1, padx=10,
                                                                                          pady=10)

        daal_lbl = Label(f3, text="Daal", bg=bg_color, font=('times new roman', 16, 'bold'),
                              fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        daal_txt = Entry(f3,textvariable=self.daal, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=2, column=1, padx=10,
                                                                                         pady=10)

        wheat_lbl = Label(f3, text="Wheat", bg=bg_color, font=('times new roman', 16, 'bold'),
                             fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        wheat_txt = Entry(f3,textvariable=self.wheat, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=3, column=1, padx=10,
                                                                                        pady=10)

        sugar_lbl = Label(f3, text="Sugar", bg=bg_color, font=('times new roman', 16, 'bold'),
                                fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        sugar_txt = Entry(f3, textvariable=self.sugar, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=4, column=1, padx=10,
                                                                                           pady=10)

        tea_lbl = Label(f3, text="Tea", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        tea_txt = Entry(f3,textvariable=self.tea, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ==============Cold Drinks Frame====================
        f4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks", font=("times new roman", 18, "bold"),
                        fg='gold', bg=bg_color)
        f4.place(x=645, y=180, width=325, height=380)

        maza_lbl = Label(f4, text="Maza", bg=bg_color, font=('times new roman', 16, 'bold'),
                              fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        maza_txt = Entry(f4,textvariable=self.maza, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                         pady=10)

        cock_lbl = Label(f4, text="Cock", bg=bg_color, font=('times new roman', 16, 'bold'),
                               fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        cock_txt = Entry(f4,textvariable=self.cock, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=1, column=1, padx=10,
                                                                                          pady=10)

        frooti_lbl = Label(f4, text="Frooti", bg=bg_color, font=('times new roman', 16, 'bold'),
                              fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        frooti_txt = Entry(f4,textvariable=self.frooti, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=2, column=1, padx=10,
                                                                                         pady=10)

        thumbs_up_lbl = Label(f4, text="Thumbs Up", bg=bg_color, font=('times new roman', 16, 'bold'),
                             fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        thumbs_up_txt = Entry(f4,textvariable=self.thumbsup, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=3, column=1, padx=10,
                                                                                        pady=10)

        limca_lbl = Label(f4, text="Limca", bg=bg_color, font=('times new roman', 16, 'bold'),
                                fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        limca_lotion_txt = Entry(f4,textvariable=self.limca, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=4, column=1, padx=10,
                                                                                           pady=10)

        sprite_lbl = Label(f4, text="Sprite", bg=bg_color, font=('times new roman', 16, 'bold'), fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        sprite_txt = Entry(f4,textvariable=self.sprite, bd=2, width=10, font=("arial 15"), relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===============Bill Area=================
        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=965, y=180, width=355, height=380)

        bill_lbl = Label(f5, text="Bill Area", bd=7, relief=GROOVE, font='arial 15 bold').pack(fill=X)
        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # =======Totals & Button Frames===================
        f6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 18, "bold"),
                        fg='gold', bg=bg_color)
        f6.place(x=0, y=560, relwidth=1, height=150)
        m1_lbl = Label(f6, text="Total Cosmetics Price", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0,column=0,padx=20,pady=2,sticky="w")
        m1_entry = Entry(f6,textvariable=self.total_cosmetics, bd=2, width=15, font=("arial 12 bold"), relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(f6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=1,column=0,padx=20,pady=2,sticky="w")
        m2_entry = Entry(f6,textvariable=self.total_grocery, bd=2, width=15, font=("arial 12 bold"), relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(f6, text="Total Drinks Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=2,column=0,padx=20,pady=2,sticky="w")
        m3_entry = Entry(f6,textvariable=self.total_drinks, bd=2, width=15, font=("arial 12 bold"), relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        # ===========Taxes========================
        c1_lbl = Label(f6, text="Cosmetics Tax", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_entry = Entry(f6,textvariable=self.cosmetics_tax, bd=2, width=15, font=("arial 12 bold"), relief=SUNKEN).grid(row=0, column=3, padx=10, pady=2)

        c2_lbl = Label(f6, text="Grocery Tax", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_entry = Entry(f6,textvariable=self.grocery_tax, bd=2, width=15, font=("arial 12 bold"), relief=SUNKEN).grid(row=1, column=3, padx=10, pady=2)

        c3_lbl = Label(f6, text="Drinks Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_entry = Entry(f6,textvariable=self.drinks_tax, bd=2, width=15, font=("arial 12 bold"), relief=SUNKEN).grid(row=2, column=3, padx=10, pady=2)

        btn_frame = Frame(f6, bd=7, relief=GROOVE)
        btn_frame.place(x=750, y=2, width=455, height=87)
        total_btn = Button(btn_frame,command=self.total, text="Total", bg="cadetblue", fg="white", bd=5, font=("arial 15 bold")).grid(row=0, column=0, padx=15, pady=12)
        gb_btn = Button(btn_frame,command=self.bill_area, text="Bill", bg="cadetblue", fg="white", bd=5, font=("arial 15 bold")).grid(row=0, column=1, padx=15, pady=12)
        clear_btn = Button(btn_frame,command=self.clear, text="Clear", bg="cadetblue", fg="white", bd=5, font=("arial 15 bold")).grid(row=0, column=2, padx=15, pady=12)
        exit_btn = Button(btn_frame, command=self.exit_app, text="Exit", bg="cadetblue", fg="white", bd=5, font=("arial 15 bold")).grid(row=0, column=3, padx=15, pady=12)
        self.welcome_bill()

    def total(self):
        # ======Total Cosmetics Prices ===============
        self.total_cosmetic_price = float(self.soap.get() * 40
                                        + self.shampoo.get() * 50
                                        + self.gel.get() * 80
                                        + self.lotion.get() * 60
                                        + self.wash.get() * 30
                                        + self.cream.get() * 100
                                     )
        self.total_cosmetics.set('Rs ' + str(self.total_cosmetic_price))
        self.cosmetics_tax.set('Rs ' + str(round(self.total_cosmetic_price*0.1,2)))
        # ======Total Grocery Prices ===============
        self.total_grocery_price = float(self.rice.get() * 40
                                     + self.daal.get() * 80
                                     + self.wheat.get() * 30
                                     + self.food_oil.get() * 125
                                     + self.sugar.get() * 30
                                     + self.tea.get() * 10
                                     )
        self.total_grocery.set('Rs ' + str(self.total_grocery_price))
        self.grocery_tax.set('Rs ' + str(round(self.total_grocery_price * 0.02, 2)))
        # ======Total Drinks Prices ===============
        self.total_drinks_price = float(self.maza.get() * 45
                                     + self.cock.get() * 50
                                     + self.frooti.get() * 10
                                     + self.sprite.get() * 45
                                     + self.thumbsup.get() * 30
                                     + self.limca.get() * 45
                                     )
        self.total_drinks.set(f"{'Rs '+ str(self.total_drinks_price)}")
        self.drinks_tax.set('Rs ' + str(round(self.total_drinks_price * 0.2, 2)))

    def welcome_bill(self):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "\tWelcome Khalid Retail\n")
        self.textarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone Number : {self.c_phone.get()}")
        self.textarea.insert(END, "\n=======================================")
        self.textarea.insert(END, "\nProducts\t\tQty\t\tPrice")
        self.textarea.insert(END, "\n=======================================")

    def bill_area(self):
        if(self.c_name.get()=="" or self.c_phone.get()==""):
            messagebox.showerror("Error", "Customer details are must!")
        elif self.total_grocery_price == 0 and self.total_drinks_price == 0 and self.total_cosmetic_price == 0:
            messagebox.showerror("Error", "No product has purchased!")
        else:
            self.welcome_bill()
            if (self.soap.get() != 0):
                self.textarea.insert(END, f"\n Soap\t\t {self.soap.get()}\t\t {self.soap.get() * 40}")
            if (self.shampoo.get() != 0):
                self.textarea.insert(END, f"\n Shampoo\t\t {self.shampoo.get()}\t\t {self.shampoo.get() * 50}")
            if (self.cream.get() != 0):
                self.textarea.insert(END, f"\n Cream\t\t {self.cream.get()}\t\t {self.cream.get() * 100}")
            if (self.gel.get() != 0):
                self.textarea.insert(END, f"\n Gel\t\t {self.gel.get()}\t\t {self.gel.get() * 80}")
            if (self.lotion.get() != 0):
                self.textarea.insert(END, f"\n Lotion\t\t {self.lotion.get()}\t\t {self.lotion.get() * 60}")
            if (self.wash.get() != 0):
                self.textarea.insert(END, f"\n Wash\t\t {self.wash.get()}\t\t {self.wash.get() * 30}")
            if (self.rice.get() != 0):
                self.textarea.insert(END, f"\n Rice\t\t {self.rice.get()}\t\t {self.rice.get() * 40}")
            if (self.daal.get() != 0):
                self.textarea.insert(END, f"\n Daal\t\t {self.daal.get()}\t\t {self.daal.get() * 80}")
            if (self.food_oil.get() != 0):
                self.textarea.insert(END, f"\n Food Oil\t\t {self.food_oil.get()}\t\t {self.food_oil.get() * 125}")
            if (self.sugar.get() != 0):
                self.textarea.insert(END, f"\n Sugar\t\t {self.sugar.get()}\t\t {self.sugar.get() * 30}")
            if (self.tea.get() != 0):
                self.textarea.insert(END, f"\n Tea\t\t {self.tea.get()}\t\t {self.tea.get() * 10}")
            if (self.wheat.get() != 0):
                self.textarea.insert(END, f"\n Wheat\t\t {self.wheat.get()}\t\t {self.wheat.get() * 30}")
            if (self.maza.get() != 0):
                self.textarea.insert(END, f"\n Maza\t\t {self.maza.get()}\t\t {self.maza.get() * 45}")
            if (self.frooti.get() != 0):
                self.textarea.insert(END, f"\n Frooti\t\t {self.frooti.get()}\t\t {self.frooti.get() * 10}")
            if (self.thumbsup.get() != 0):
                self.textarea.insert(END, f"\n Thumbsup\t\t {self.thumbsup.get()}\t\t {self.thumbsup.get() * 30}")
            if (self.sprite.get() != 0):
                self.textarea.insert(END, f"\n Sprite\t\t {self.sprite.get()}\t\t {self.sprite.get() * 45}")
            if (self.limca.get() != 0):
                self.textarea.insert(END, f"\n Limca\t\t {self.limca.get()}\t\t {self.limca.get() * 45}")
            if (self.cock.get() != 0):
                self.textarea.insert(END, f"\n Cock\t\t {self.cock.get()}\t\t {self.cock.get() * 50}")

            self.textarea.insert(END, "\n---------------------------------------")
            if(self.cosmetics_tax.get() != 'Rs 0.0' and self.cosmetics_tax.get() != ''):
                self.textarea.insert(END, f"\nCosmetics Tax\t\t{self.cosmetics_tax.get()}")
            if (self.grocery_tax.get() != 'Rs 0.0' and self.grocery_tax.get() != ''):
                self.textarea.insert(END, f"\nGrocery Tax\t\t{self.grocery_tax.get()}")
            if (self.drinks_tax.get() != 'Rs 0.0' and self.drinks_tax.get() != ''):
                self.textarea.insert(END, f"\nDrinks Tax\t\t{self.drinks_tax.get()}")

            self.total_bill_price = float(
                self.total_grocery_price +
                self.total_cosmetic_price +
                self.total_drinks_price +
                round(self.total_drinks_price * 0.2, 2) +
                round(self.total_cosmetic_price*0.1,2) +
                round(self.total_grocery_price * 0.02, 2)
            )

            self.textarea.insert(END,f"\nTotals\t\t{'Rs '+str(self.total_bill_price)}")
            self.textarea.insert(END, "\n---------------------------------------")
            self.save_bill()

    # =========Save Bill as .txt==========
    def save_bill(self):
        option = messagebox.askyesno("Save Bill", "Do you want save bill?")
        if option:
            bill_data = self.textarea.get("1.0", END)
            bill_file = open("savedBills/"+self.bill_no.get()+".txt", "w")
            bill_file.write(bill_data)
            bill_file.close()
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} saved successfully!")
        else:
            return

    def search_saved_bill(self):
        if self.search_bill.get() == "":
            messagebox.showerror("Error", "Please enter valid bill number!")
        elif not os.listdir("savedBills/"):
            messagebox.showerror("Error", "Bill data not available!")
        elif self.search_bill.get()+'.txt' not in os.listdir("savedBills/"):
            messagebox.showerror("Error", f"No Bill details found for bill no. {self.search_bill.get()}")
        else:
            for bill in os.listdir("savedBills/"):
                if str(bill.split('.')[0]) == self.search_bill.get():
                    bill_details = open(f"savedBills/{bill}", "r")
                    self.textarea.delete('1.0', END)

                    for details in bill_details:
                        self.textarea.insert(END, details)
                    bill_details.close()

    def clear(self):
        option = messagebox.askyesno("Exit", "Do you really want to clear data?")
        if option:
            # ======Cosmetics Variables
            self.soap.set(0)
            self.cream.set(0)
            self.wash.set(0)
            self.gel.set(0)
            self.lotion.set(0)
            self.shampoo.set(0)

            # ======Grocery Variables
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ======Drinks Variables
            self.maza.set(0)
            self.cock.set(0)
            self.thumbsup.set(0)
            self.frooti.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ======Total Product Prices & Tax Variables======
            self.total_cosmetics.set("")
            self.total_grocery.set("")
            self.total_drinks.set("")

            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")

            # ======Customer Details=======
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit?")
        if option:
            self.root.destroy()




root = Tk()
obj = BillApp(root)
root.mainloop()
