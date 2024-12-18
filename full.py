from tkinter import*
import math,random,os
import mysql.connector
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Electro Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==========variables===========
        #==========Laptops============
        self.hp_laptop=IntVar()
        self.dell_laptop=IntVar()
        self.lenovo_laptop=IntVar()
        self.asus_laptop=IntVar()
        self.apple_laptop=IntVar()
        self.acer_laptop=IntVar()
        #==========Phones============
        self.apple_iPhone=IntVar()
        self.samsungP=IntVar()
        self.oneplusP=IntVar()
        self.realmeP=IntVar()
        self.oppoP=IntVar()
        self.vivoP=IntVar()
        #===========LEDs=============
        self.sony=IntVar()
        self.samsung=IntVar()
        self.croma=IntVar()
        self.xiaomi=IntVar()
        self.toshiba=IntVar()
        self.panasonic=IntVar()

        #===========Total Product Price & Tax Variable==========
        self.laptops_price=StringVar()
        self.phones_price=StringVar()
        self.leds_price=StringVar()


        self.laptops_tax=StringVar()
        self.phones_tax=StringVar()
        self.leds_tax=StringVar()

        #==========Customer===========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        


        #============Customer Detail Frame===========
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("timesnew roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        #cbill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        #cphn_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        #bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #==========1st appliances========
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Laptops",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=10,y=180,width=330,height=380)

        hp_lbl=Label(F2,text="hp laptop",font=("times new roman"    ,16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        hp_txt=Entry(F2,width=10,textvariable=self.hp_laptop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        dell_lbl=Label(F2,text="DELL laptop",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        dell_txt=Entry(F2,width=10,textvariable=self.dell_laptop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        lenovo_lbl=Label(F2,text="lenovo laptop",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        lenovo_txt=Entry(F2,width=10,textvariable=self.lenovo_laptop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        asus_lbl=Label(F2,text="Asus laptop",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        asus_txt=Entry(F2,width=10,textvariable=self.asus_laptop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        apple_lbl=Label(F2,text="Apple laptop",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        apple_txt=Entry(F2,width=10,textvariable=self.apple_laptop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        acer_lbl=Label(F2,text="Acer laptop",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        acer_txt=Entry(F2,width=10,textvariable=self.acer_laptop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==========2st appliances========
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Phones",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=344,y=180,width=330,height=380)

        appleiphone_lbl=Label(F3,text="Apple iPhone",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        appleiphone_txt=Entry(F3,width=10,textvariable=self.apple_iPhone,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        samsung_lbl=Label(F3,text="Samsung Galaxy",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        samsung_txt=Entry(F3,width=10,textvariable=self.samsungP,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        oneplus_lbl=Label(F3,text="OnePlus",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        oneplus_txt=Entry(F3,width=10,textvariable=self.oneplusP,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        realme_lbl=Label(F3,text="Realme",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        realme_txt=Entry(F3,width=10,textvariable=self.realmeP,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        oppo_lbl=Label(F3,text="Oppo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        oppo_txt=Entry(F3,width=10,textvariable=self.oppoP,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        vivo_lbl=Label(F3,text="Vivo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        vivo_txt=Entry(F3,width=10,textvariable=self.vivoP,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==========3st appliances========
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="LEDs",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=678,y=180,width=325,height=380)

        sony_lbl=Label(F4,text="Sony",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sony_txt=Entry(F4,width=10,textvariable=self.sony,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        samsung_lbl=Label(F4,text="Samsung ",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        samsung_txt=Entry(F4,width=10,textvariable=self.samsung,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        croma_lbl=Label(F4,text="Croma",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        croma_txt=Entry(F4,width=10,textvariable=self.croma,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        xiaomi_lbl=Label(F4,text="Xiaomi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        xiaomi_txt=Entry(F4,width=10,textvariable=self.xiaomi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        toshiba_lbl=Label(F4,text="TOSHIBA",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        toshiba_txt=Entry(F4,width=10,textvariable=self.toshiba,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        panasonic_lbl=Label(F4,text="Panasonic",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        panasonic_txt=Entry(F4,width=10,textvariable=self.panasonic,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #=========Bill Area==========
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=400,height=380)
        bill_title=Label(F5,text=" Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #===========Button Frame==========
        
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=565,relwidth=1,height=190)
        m1_1b1=Label(F6,text="Total Laptops Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.laptops_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=12)
        
        m2_1b1=Label(F6,text="Total Phones Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.phones_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=15,pady=11)
        
        m3_1b1=Label(F6,text="Total LEDs Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.leds_price,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        
          
        c1_1b1=Label(F6,text=" Laptops Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.laptops_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=15)
        
        c2_1b1=Label(F6,text=" Phones Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.phones_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=20,pady=11)
        
        c3_1b1=Label(F6,text=" LEDs Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.leds_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=20,pady=10)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=760,width=650,height=160)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=20,width=10,font="arial 15 bold").grid(row=0,column=0,padx=15,pady=2)
        GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=20,width=10,font="arial 15 bold").grid(row=0,column=1,padx=10,pady=8)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=20,width=10,font="arial 15 bold").grid(row=0,column=2,padx=12,pady=14)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=20,width=10,font="arial 15 bold").grid(row=0,column=3,padx=13,pady=15)
        self.welcome_bill()

    def total(self):
        self.l_hp_laptop_p=self.hp_laptop.get()*40000
        self.l_dell_laptop_p=self.dell_laptop.get()*35000
        self.l_lenovo_laptop_p=self.lenovo_laptop.get()*43000
        self.l_asus_laptop_p=self.asus_laptop.get()*75000
        self.l_apple_laptop_p=self.apple_laptop.get()*90000
        self.l_acer_laptop_p=self.acer_laptop.get()*65000
        
        self.total_laptops_price=float(
                                                       self.l_hp_laptop_p+
                                                       self.l_dell_laptop_p+
                                                       self.l_lenovo_laptop_p+
                                                       self.l_asus_laptop_p+
                                                       self.l_apple_laptop_p+
                                                       self.l_acer_laptop_p
                                                      )
        self.laptops_price.set("Rs.    "+str(self.total_laptops_price))
        self.l_tax=round((self.total_laptops_price*0.05),2)
        self.laptops_tax.set("Rs.   "+str(self.l_tax))


        self.p_apple_iPhone_p=self.apple_iPhone.get()*50000
        self.p_samsungP_p=self.samsungP.get()*24000
        self.p_oneplusP_p=self.oneplusP.get()*35000
        self.p_realmeP_p=self.realmeP.get()*20000
        self.p_oppoP_p=self.oppoP.get()*150000
        self.p_vivoP_p=self.vivoP.get()*49000

        self.total_phones_price=float(
                                                       self.p_apple_iPhone_p+
                                                       self.p_samsungP_p+
                                                       self.p_oneplusP_p+
                                                       self.p_realmeP_p+
                                                       self.p_oppoP_p+
                                                       self.p_vivoP_p
                                                      )
        self.phones_price.set("Rs.    "+str(self.total_phones_price))
        self.p_tax=round((self.total_phones_price*0.1),2)
        self.phones_tax.set("Rs.   "+str(self.p_tax))

        
        self.leds_sony_p=self.sony.get()*30000
        self.leds_samsung_p=self.samsung.get()*29000
        self.leds_croma_p=self.croma.get()*15500
        self.leds_xiaomi_p=self.xiaomi.get()*20000
        self.leds_toshiba_p=self.toshiba.get()*13500
        self.leds_panasonic_p=self.panasonic.get()*25000

        self.total_leds_price=float(
                                                       self.leds_sony_p+
                                                       self.leds_samsung_p+
                                                       self.leds_croma_p+
                                                       self.leds_xiaomi_p+
                                                       self.leds_toshiba_p+
                                                       self.leds_panasonic_p
                                                      )
        self.leds_price.set("Rs.  "+str(self.total_leds_price))
        self.led_tax=round((self.total_leds_price*0.05),2)
        self.leds_tax.set("Rs.  "+str(self.led_tax))

        self.Total_bill=float(    self.total_laptops_price+
                                              self.total_phones_price+
                                              self.total_leds_price+
                                              self.l_tax+
                                              self.p_tax+
                                              self.led_tax
                                         )

        
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome Webcode Reatil \n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n============================================")
        self.txtarea.insert(END,f"\n Products\t\t QTY\t\t Price")
        self.txtarea.insert(END,f"\n============================================")
        
    def bill_area(self):
            if self.c_name.get()=="" or self.c_phon.get()=="":
                messagebox.showerror("Error","Customer details are must")
            elif    self.laptops_price.get()=="Rs.  0.0" and  self.phones_price.get()=="Rs.  0.0" and  self.leds_price.get()=="Rs.  0.0":
                messagebox.showerror("Error","No Product puchased")
            else:
                self.welcome_bill()

                myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "Mrunali*1811", database = "billingpy")
                cur=myconn.cursor()
                cur.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.bill_no.get(),
                                                                                              self.c_name.get(),
                                                                                              self.c_phon.get(),
                                                                                              self.total_laptops_price,
                                                                                              self.total_phones_price,
                                                                                              self.total_leds_price,
                                                                                              self.laptops_tax.get(),
                                                                                              self.phones_tax.get(),
                                                                                              self.leds_tax.get(),
                                                                                              self.Total_bill))
                
       
                cur.execute("insert into  Laptop values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.bill_no.get(),
                                                                                              self.c_name.get(),
                                                                                              self.c_phon.get(),
                                                                                              self.l_hp_laptop_p,
                                                                                              self.l_dell_laptop_p,
                                                                                              self.l_lenovo_laptop_p,
                                                                                              self.l_asus_laptop_p,
                                                                                              self.l_apple_laptop_p,
                                                                                              self.l_acer_laptop_p,
                                                                                              self.total_laptops_price,
                                                                                              self.laptops_tax.get(),
                                                                                              self.Total_bill))
                cur.execute("insert into Phones values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.bill_no.get(),
                                                                                              self.c_name.get(),
                                                                                              self.c_phon.get(),
                                                                                              self.p_apple_iPhone_p,
                                                                                              self.p_samsungP_p,
                                                                                              self.p_oneplusP_p,
                                                                                              self.p_realmeP_p,
                                                                                              self.p_oppoP_p,
                                                                                              self.p_vivoP_p,
                                                                                              self.total_phones_price,
                                                                                              self.leds_tax.get(),
                                                                                              self.Total_bill))
                cur.execute("insert into LEDs values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.bill_no.get(),
                                                                                              self.c_name.get(),
                                                                                              self.c_phon.get(),
                                                                                              self.leds_sony_p,
                                                                                              self.leds_samsung_p,
                                                                                              self.leds_croma_p,
                                                                                              self.leds_xiaomi_p,
                                                                                              self.leds_toshiba_p,
                                                                                              self.leds_panasonic_p,
                                                                                              self.total_leds_price,
                                                                                              self.phones_tax.get(),
                                                                                              self.Total_bill))
                myconn.commit()
                print(cur.rowcount,"record inserted!")
                myconn.close()

                
                
            #====Laptops====
            if self.hp_laptop.get()!=0:
                self.txtarea.insert(END,f"\n hp laptop\t\t{self.hp_laptop.get()}\t\t{self.l_hp_laptop_p}")
            if self.dell_laptop.get()!=0:
                self.txtarea.insert(END,f"\n dell laptop\t\t{self.dell_laptop.get()}\t\t{self.l_dell_laptop_p}")
            if self.lenovo_laptop.get()!=0:
                self.txtarea.insert(END,f"\n lenovo laptop\t\t{self.lenovo_laptop.get()}\t\t{self.l_lenovo_laptop_p}")
            if self.asus_laptop.get()!=0:
                self.txtarea.insert(END,f"\n asus laptop\t\t{self.asus_laptop.get()}\t\t{self.l_asus_laptop_p}")
            if self.apple_laptop.get()!=0:
                self.txtarea.insert(END,f"\n apple laptop\t\t{self.apple_laptop.get()}\t\t{self.l_apple_laptop_p}")
            if self.acer_laptop.get()!=0:
                self.txtarea.insert(END,f"\n acer laptop\t\t{self.acer_laptop.get()}\t\t{self.l_acer_laptop_p}")
            
                                 
              #====Phones====
            if self.apple_iPhone.get()!=0:
                self.txtarea.insert(END,f"\n apple iPhone\t\t{self.apple_iPhone.get()}\t\t{self.p_apple_iPhone_p}")
            if self.samsungP.get()!=0:
                self.txtarea.insert(END,f"\n samsungP\t\t{self.samsungP.get()}\t\t{self.p_samsungP_p}")
            if self.oneplusP.get()!=0:
                self.txtarea.insert(END,f"\n oneplusP\t\t{self.oneplusP.get()}\t\t{self.p_oneplusP_p}")
            if self.realmeP.get()!=0:
                self.txtarea.insert(END,f"\n realmeP\t\t{self.realmeP.get()}\t\t{self.p_realmeP_p}")
            if self.oppoP.get()!=0:
                self.txtarea.insert(END,f"\n oppoP\t\t{self.oppoP.get()}\t\t{self.p_oppoP_p}")
            if self.vivoP.get()!=0:
                self.txtarea.insert(END,f"\n vivoP\t\t{self.vivoP.get()}\t\t{self.p_vivoP_p}")
            
           #====LEDS====
            if self.sony.get()!=0:
                self.txtarea.insert(END,f"\n sony\t\t{self.sony.get()}\t\t{self.leds_sony_p}")
            if self.samsung.get()!=0:
                self.txtarea.insert(END,f"\n samsung\t\t{self.samsung.get()}\t\t{self.leds_samsung_p}")
            if self.croma.get()!=0:
                self.txtarea.insert(END,f"\n croma\t\t{self.croma.get()}\t\t{self.leds_croma_p}")
            if self.xiaomi.get()!=0:
                self.txtarea.insert(END,f"\n xiaomi\t\t{self.xiaomi.get()}\t\t{self.leds_xiaomi_p}")
            if self.toshiba.get()!=0:
                self.txtarea.insert(END,f"\n toshiba\t\t{self.toshiba.get()}\t\t{self.leds_toshiba_p}")
            if self.panasonic.get()!=0:
                self.txtarea.insert(END,f"\n panasonic\t\t{self.panasonic.get()}\t\t{self.leds_panasonic_p}")
            
                                 
            self.txtarea.insert(END,f"\n--------------------------------------------")
            if self.laptops_tax.get()!=" Rs. 0.0":
                self.txtarea.insert(END,f"\n Laptops Tax\t\t\t{self.laptops_tax.get()}")
                
            if self.phones_tax.get()!=" Rs. 0.0":
                self.txtarea.insert(END,f"\n Phones Tax\t\t\t{self.phones_tax.get()}")
                
            if self.leds_tax.get()!=" Rs. 0.0":
                self.txtarea.insert(END,f"\n LEDs Tax\t\t\t{self.leds_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill :  \t\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n--------------------------------------------")
            self.save_bill()
                                                  
    def save_bill(self):
        op=messagebox.askyesno("save Bill", "Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+" .txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved Successfully")
            
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):  
            if  i.split(' . ')[0]==self.search_bill.get():
                f1=open(f"bills/{i}", "r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            
        
             #==========Laptops============
            self.hp_laptop.set(0)
            self.dell_laptop.set(0)
            self.lenovo_laptop.set(0)
            self.asus_laptop.set(0)
            self.apple_laptop.set(0)
            self.acer_laptop.set(0)
            #==========Phones============
            self.apple_iPhone.set(0)
            self.samsungP.set(0)
            self.oneplusP.set(0)
            self.realmeP.set(0)
            self.oppoP.set(0)
            self.vivoP.set(0)
            #===========LEDs=============
            self.sony.set(0)
            self.samsung.set(0)
            self.croma.set(0)
            self.xiaomi.set(0)
            self.toshiba.set(0)
            self.panasonic.set(0)
            

            #===========Total Product Price & Tax Variable==========
            self.laptops_price.set(" ")
            self.phones_price.set(" ")
            self.leds_price.set(" ")


            self.laptops_tax.set(" ")
            self.phones_tax.set(" ")
            self.leds_tax.set(" ")

            #==========Customer===========
            self.c_name.set(" ")
            self.c_phon.set(" ")
            
            self.bill_no.set(" ")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set(" ")
            self.welcome_bill()
            
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

'''myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "Mrunali*1811", database = "billing")
cur=myconn.cursor()
try:
    dbs1=cur.execute("CREATE TABLE customers ( customer_id INT PRIMARY KEY AUTO_INCREMENT,customer_name VARCHAR(100),phone_number VARCHAR(20))")
    dbs2=cur.execute("CREATE TABLE products (product_id INT PRIMARY KEY AUTO_INCREMENT,product_name VARCHAR(100),price DECIMAL(10,2))")
    dbs3=cur.execute("CREATE TABLE orders (order_id INT PRIMARY KEY AUTO_INCREMENT,customer_id INT,order_date DATE,total_amount DECIMAL(10,2),FOREIGN KEY (customer_id) REFERENCES customers(customer_id))")
    dbs4=cur.execute("CREATE TABLE order_details (order_id INT,product_id INT,quantity INT,price DECIMAL(10,2),PRIMARY KEY (order_id, product_id),FOREIGN KEY (order_id) REFERENCES orders(order_id),FOREIGN KEY (product_id) REFERENCES products(product_id))")
except:
    myconn.rollback()


sql1="INSERT INTO customers (c_name, c_phon) VALUES (%s,%s)"
sql2=" INSERT INTO orders (bill_no, Total_bill) VALUES (%s,%s)"
sql3=" INSERT INTO order_details (quantity, price) VALUES (%s,%s,%s,%s)"


val1=(str(self.c_name.get()), str(self.c_phon.get()))
val2=(str(self.bill_no.get()), self.Total_bill)
val3=(quantity, price)



try:
    cur.execute(sql1,val1)
    cur.execute(sql2,val2)
    cur.execute(sql3,val3)
    cur.execute(sql4,val4)'

    myconn.commit()

except:
    myconn.rollback()

print(cur.rowcount,"record inserted!")
myconn.close()'''


if __name__ == "__main__":
    root=Tk()
    obj = Bill_App(root)
    root.mainloop()
