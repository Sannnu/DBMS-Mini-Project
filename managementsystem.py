from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1366x768+0+0")


        #====================================Variable====================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="red",bd=20,relief=RIDGE,font=("arial",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=2,bg="powder blue")
        frame.place(x=0,y=130,width=1366,height=400)
        

        #====================================DataFrame Left====================================
        DataFrameLeft=LabelFrame(frame,text="Librabry Membership Information",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameLeft.place(x=10,y=5,width=650,height=440)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN NO",font=("arial",12,"bold"),padx=2)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="ID No",bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="FirstName",bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="LastName",bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Address1",bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Address2",bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Post Code",bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Mobile",bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Book ID:",bg="powder blue")
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Book Title:",bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTile=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTile.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Author Name:",bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",13,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Date Borrowed:",bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Date Due:",bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Days On Book:",bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Late Return Fine:",bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDate=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Date Over Date:",bg="powder blue")
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,textvariable=self.dateoverdue,font=("arial",13,"bold"),width=29)
        txtDateOverDate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),padx=2,pady=4,text="Actual Price:",bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)


        #====================================DataFrameRight====================================
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=670,y=5,width=680,height=440)
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky='ns')

        listBooks=['Head First Book', 'Learn Python The Hard Way', 'Python Programming', "Secrete Rahshy", 
                   'Python CookBook','Into to Machine Learning','Fluent Python', 'Machine Tecno', 
                   'My Python', 'Joss Ellif guru','Elite Jungle python', 'Jungli Python', 'Mumbai Python', 
                   'Pune Python','Machine python', 'Advance Python', 'Inton Python', 'RedChilli Python']
        
        def SelectBook(event=""):
            if listBox.curselection():
                index = listBox.curselection()[0]
                value = str(listBox.get(index))
                x = value
                if x == "Head First Book":
                    self.bookid_var.set("BKID5454")
                    self.booktitle_var.set("Python Manual")
                    self.author_var.set("Paul Berry")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.latereturnfine_var.set("Rs.50")
                    self.dateoverdue.set("No")
                    self.finalprice.set("Rs.788")
                
                elif x == "Learn Python The Hard Way":
                    self.bookid_var.set("BKID8796")
                    self.booktitle_var.set("Basics of python")
                    self.author_var.set("Zed A.Shaw")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.latereturnfine_var.set("Rs.25")
                    self.dateoverdue.set("No")
                    self.finalprice.set("Rs.725")   

                elif x == "Python Programming":
                    self.bookid_var.set("BKID1245")
                    self.booktitle_var.set("Introduction to python")
                    self.author_var.set("Jhon Zelle")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.latereturnfine_var.set("Rs.25")
                    self.dateoverdue.set("No")
                    self.finalprice.set("Rs.500")

                elif x == "Secrete Rahshy":
                    self.bookid_var.set("BKID8796")
                    self.booktitle_var.set("Mysteries")
                    self.author_var.set("Kapil Kamble")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.latereturnfine_var.set("Rs.25")
                    self.dateoverdue.set("No")
                    self.finalprice.set("Rs.289")

            elif x == "Python CookBook":
                    self.bookid_var.set("BKID2546")
                    self.booktitle_var.set("Python CookBook")
                    self.author_var.set("Brian Jones")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.latereturnfine_var.set("Rs.25")
                    self.dateoverdue.set("No")
                    self.finalprice.set("Rs.354")

            elif x == "Into to Machine Learning":
                    self.bookid_var.set("BKID8567")
                    self.booktitle_var.set("Into to Machine Learning")
                    self.author_var.set("Sarah Guaido")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.latereturnfine_var.set("Rs.25")
                    self.dateoverdue.set("No")
                    self.finalprice.set("Rs.725")
                    
                    


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        #====================================Buttons Frame====================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=10,y=460,width=1346,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.show_data,text="Show Data",font=("arial",12,"bold"),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=5)


        #====================================Information Frame====================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=10,y=500,width=1346,height=250)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg='powder blue')
        Table_frame.place(x=0,y=2,width=1366,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=('member type', 'prnno', 'title', 'firstname',
                                                            'lastname','address1','address2','postid','mobile',
                                                            'bookid','booktitle','author','dateborrowed',
                                                            'datedue','days','latereturnfine','dateoverdate',
                                                            'finalprice'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)                                                                    
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("member type",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author Name")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdate",text="Date Over Date")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table['show']='headings'
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("member type",width=100)
        self.library_table.column("member type",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdate",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sanuu7262",database="managementsys")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),                                                                                               
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finalprice.get()
                                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Sucess","Member has been inserted sucessfully.")

    
    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="sanuu7262", database="managementsys")
        my_cursor = conn.cursor()
        query = "UPDATE library SET Members=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostID=%s, Mobile=%s, BookID=%s, BookTitle=%s, Author=%s, DateBorrowed=%s, DateDue=%s, daysofbook=%s, LateReturnFine=%s, DateOverDue=%s, FinalPrice=%s WHERE PRN_No=%s"
        values = (self.member_var.get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(), self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook.get(), self.latereturnfine_var.get(), self.dateoverdue.get(), self.finalprice.get(), self.prn_var.get())
        my_cursor.execute(query, values)
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo('Success', 'Member has been Updated.')


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="sanuu7262", database="managementsys")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])


    def show_data(self):
        self.txtBox.delete("1.0", END)
        data = "Member Type: {}\nPRN NO: {}\nID NO: {}\nFIRST NAME: {}\nLAST NAME: {}\nADDRESS 1: {}\nADDRESS 2: {}\nPOST ID: {}\nMOBILE NO: {}\nBOOK ID: {}\nAUTHOR: {}\nDATE BORROWED: {}\nDATE DUE: {}\nDAYS OF BOOK: {}\nLATE RETURN FINE: {}\nDATE OVER DUE: {}\nFINAL PRICE: {}".format(self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(), self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook.get(), self.latereturnfine_var.get(), self.dateoverdue.get(), self.finalprice.get())
        self.txtBox.insert(END, data)

    
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "First Select Member")

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="sanuu7262", database="managementsys")
            my_cursor = conn.cursor()
            query = "DELETE FROM library WHERE PRN_No=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "Member has been Deleted.")


         


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()  
