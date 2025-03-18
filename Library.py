from tkinter import *  # Importing Tkinter module
from tkinter import ttk
import mysql.connector as mysqlConn
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root  # Assigning the root window to the instance variable
        self.root.title("Library Management System")  # Setting the title of the window
        self.root.geometry("1550x800+0+0")  # Corrected the geometry string (used 'x' instead of '*' for dimensions)
        # Creating a label for the title of the system

        #===============Variable==========
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
        self.datedur_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        lbltitle = Label(
            root, 
           text="LIBRARY MANAGEMENT SYSTEM",  # Text to display on the label
           bg="powder blue",  # Background color of the label
            fg="green",  # Text color of the label
            bd=16,  # Border width
                         relief=RIDGE,  # Border relief style (Ridge gives a 3D effect)
            font=("times new roman", 30, "bold"),  # Font style, size, and weight
           padx=2,  # Padding for the label (horizontal)
            pady=6  # Padding for the label (vertical)
        )

        # Packing the label to the top and making it stretch across the window horizontally
        lbltitle.pack(side=TOP, fill=X)


        frame = Frame(self.root, bd=1, relief=RIDGE, padx=20, bg="blue")
        frame.place(x=2, y=90, width=1530, height=400)  # Correcting the placement syntax for the frame


#         #=================DataFrameLeft===================

        DataFrameLeft=LabelFrame(frame,
            text="Library Membership Information",  # Text to display on the label
            bg="powder blue",  # Background color of the label
             fg="green",  # Text color of the label
             bd=10,  # Border width
             relief=RIDGE,  # Border relief style (Ridge gives a 3D effect)
             font=("times new roman", 12, "bold"),  # Font style, size, and weight
             padx=2,  # Padding for the label (horizontal)
             pady=6  # Padding for the label (vertical)
         )


        DataFrameLeft.place(x=0,y=5,width=700,height=400)

        lblMember=Label(DataFrameLeft,text="Member Type:",bg="powder blue",font=("arial",10,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",10,"bold"),width=30,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)
        
        lblPRN_NO=Label(DataFrameLeft,textvariable=self.prn_var,text="PRN NO",bg="powder blue",font=("arial",10,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)

        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",10,"bold"),width=30)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,textvariable=self.id_var,font=("arial",10,"bold"),text="ID No:",padx=2,pady=4,bg="Powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",10,"bold"),width=30)
        txtTitle.grid(row=2,column=1)
                  
        
        lblFirstName=Label(DataFrameLeft,font=("arial",10,"bold"),text="Firstname:",padx=2,pady=4,bg="Powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",10,"bold"),width=30)
        txtFirstName.grid(row=3,column=1)
        

        lblLastName=Label(DataFrameLeft,font=("arial",10,"bold"),text="Lastname:",padx=2,pady=4,bg="Powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",10,"bold"),width=30)
        txtLastName.grid(row=4,column=1)
        

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=4,bg="Powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=38)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=4,bg="Powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=38)
        txtAddress2.grid(row=6,column=1)
        

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=4,bg="Powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=38)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=4,bg="Powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=38)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookId:",padx=2,pady=4,bg="Powder blue")
        lblBookId.grid(row=9,column=0,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=38)
        txtBookId.grid(row=9,column=1)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=4,bg="Powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=38)
        txtBookTitle.grid(row=1,column=3)


        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=4,bg="Powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",13,"bold"),width=38)
        txtAuthor.grid(row=2,column=3)
        

        lblDateborrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=4,bg="Powder blue")
        lblDateborrowed.grid(row=3,column=2,sticky=W)
        txtDateborrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=38)
        txtDateborrowed.grid(row=3,column=3)

        lblDatedue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=4,bg="Powder blue")
        lblDatedue.grid(row=4,column=2,sticky=W)
        txtDatedue=Entry(DataFrameLeft,textvariable=self.datedur_var,font=("arial",13,"bold"),width=38)
        txtDatedue.grid(row=4,column=3)
        

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days on books:",padx=2,pady=4,bg="Powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",13,"bold"),width=38)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=4,bg="Powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.lateratefine_var,font=("arial",13,"bold"),width=38)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=4,bg="Powder blue")
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",13,"bold"),width=38)
        txtDateOverDate.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=4,bg="Powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("arial",13,"bold"),width=38)
        txtActualPrice.grid(row=8,column=3)

         #============================DataFrameRight==========================
        
        DataFrameRight=LabelFrame(frame,
             text="Book Details",  # Text to display on the label
             bg="powder blue",  # Background color of the label
             fg="green",  # Text color of the label
             bd=12,  # Border width
             relief=RIDGE,  # Border relief style (Ridge gives a 3D effect)
             font=("times new roman", 12, "bold"),  # Font style, size, and weight
             padx=2,  # Padding for the label (horizontal)
             pady=6  # Padding for the label (vertical)
         )

        DataFrameRight.place(x=910,y=5,width=540,height=350)


        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)  #Creating textbox in right dataframe
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBoooks=["To Kill a Mockingbird",
                       "George Orwell",
                       "The Great Gatsby",
                        "Moby-Dick",
                        "Pride and Prejudice",
                        "The Catcher in the Rye",
                        "The Hobbit",
                        "Harry Potter and the Sorcerer's Stone",
                        "The Lord of the Rings",
                        "The Alchemist","The Da Vinci Code",
                        "The Hunger Games",
                        "The Odysse",
                        "Brave New World",
                        "Fahrenheit 451",
                        "The Chronicles of Narni",
                         "War and Peace",
                       "Crime and Punishment",
                      "Catch-22",
                       "The Picture of Dorian Gray",
                        "Wuthering Heights",
                        "The Kite Runner",
                         "The Shining",
                          "The Girl on the Train",
                         "The Fault in Our Stars",
                         "The Secret Garden",
                        "The Road",
                        "Little Women",
                     "The Book Thief",
                      "A Brief History of Time"] #making list of books
        
        def SelectBook(ZXevent=""):
             value=str(listBox.get(listBox.curselection()))
             x=value
             print()
             if(x == "To Kill a Mockingbird"):
                  self.bookid_var.set("BKID1")
                  self.booktitle_var.set("Python Manual")
                  self.author_var.set("PAul berry")
                  d1=datetime.datetime.today()
                  d2=datetime.timedelta(days=15)
                  d3=d1+d2
                  self.dateborrowed_var.set(d1)
                  self.datedur_var.set(d3)
                  self.daysonbook_var.set(15)
                  self.lateratefine_var.set("RS.50")
                  self.dateoverdue_var.set("No")
                  self.finalprice_var.set("RS.788")
             elif(x == "George Orwell"):
                  self.bookid_var.set("BKID2")
                  self.booktitle_var.set("ab Manual")
                  self.author_var.set("s.d.sharma")
                  d1=datetime.datetime.today()
                  d2=datetime.timedelta(days=15)
                  d3=d1+d2
                  self.dateborrowed_var.set(d1)
                  self.datedur_var.set(d3)
                  self.daysonbook_var.set(15)
                  self.lateratefine_var.set("RS.50")
                  self.dateoverdue_var.set("No")
                  self.finalprice_var.set("RS.788")
             elif(x == "The Great Gatsby"):
                  self.bookid_var.set("BKID3")
                  self.booktitle_var.set("yx Manual")
                  self.author_var.set("a.d.shinde")
                  d1=datetime.datetime.today()
                  d2=datetime.timedelta(days=15)
                  d3=d1+d2
                  self.dateborrowed_var.set(d1)
                  self.datedur_var.set(d3)
                  self.daysonbook_var.set(15)
                  self.lateratefine_var.set("RS.50")
                  self.dateoverdue_var.set("No")
                  self.finalprice_var.set("RS.1000")
             elif(x == "Moby-Dick"):
                  self.bookid_var.set("BKID4")
                  self.booktitle_var.set("rt Manual")
                  self.author_var.set("q.t.shinde")
                  d1=datetime.datetime.today()
                  d2=datetime.timedelta(days=15)
                  d3=d1+d2
                  self.dateborrowed_var.set(d1)
                  self.datedur_var.set(d3)
                  self.daysonbook_var.set(15)
                  self.lateratefine_var.set("RS.50")
                  self.dateoverdue_var.set("No")
                  self.finalprice_var.set("RS.300")
             elif(x == "Pride and Prejudice"):
                  self.bookid_var.set("BKID5")
                  self.booktitle_var.set("ps Manual")
                  self.author_var.set("D.A Sawant")
                  d1=datetime.datetime.today()
                  d2=datetime.timedelta(days=15)
                  d3=d1+d2
                  self.dateborrowed_var.set(d1)
                  self.datedur_var.set(d3)
                  self.daysonbook_var.set(15)
                  self.lateratefine_var.set("RS.50")
                  self.dateoverdue_var.set("No")
                  self.finalprice_var.set("RS.600")
                  







    
        listBox=Listbox(DataFrameRight,font=("aerial",12,"bold"),width=20,height=16)
        
        listBox.grid(row=0,column=0,padx=4)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        
        
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
             listBox.insert(END,item)
             #=============================Buttons Frame===================
        frameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frameButton.place(x=0, y=530, width=1530, height=70)  # Correcting the placement syntax for the frame
        
        btnAddData=Button(frameButton,command=self.adda_data,text="Add Data",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(frameButton,text="Show Data",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(frameButton,text="Update",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(frameButton,text="Delete",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(frameButton,text="Reset",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(frameButton,text="Exit",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
         #======================Information Frame===================

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)  # Correcting the placement syntax for the frame


        Table_frame = Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
           
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN no")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="Firstname")
        self.library_table.heading("lastname",text="Lastname")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="DateBorrowed")
        self.library_table.heading("datedue",text="DateDue")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"

        self.library_table.pack(fill=BOTH,expand=1)        
         
        self.library_table.column("membertype",width=80)
        self.library_table.column("prnno",width=80)
        self.library_table.column("title",width=80)
        self.library_table.column("firstname",width=80)
        self.library_table.column("lastname",width=80)
        self.library_table.column("address1",width=80)
        self.library_table.column("address2",width=80)
        self.library_table.column("postid",width=80)
        self.library_table.column("mobile",width=80)
        self.library_table.column("bookid",width=80)
        self.library_table.column("booktitle",width=80)
        self.library_table.column("author",width=80)
        self.library_table.column("dateborrowed",width=80)
        self.library_table.column("datedue",width=80)
        self.library_table.column("days",width=80)
        self.library_table.column("latereturnfine",width=80)
        self.library_table.column("dateoverdue",width=80)
        self.library_table.column("finalprice",width=80)


        self.fetch_data()
        self.library_table.bind("<<ButtonRelease-1>>",self.get_cursor)

    def adda_data(self):
         
         conn=mysqlConn.connect(host="localhost",username="root",password="sangola",database="LibraryManagementSystem")
         my_cursor=conn.cursor()
         my_cursor.execute("Insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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
                                      self.datedur_var.get(),
                                      self.daysonbook_var.get(),
                                      self.lateratefine_var.get(),
                                      self.dateoverdue_var.get()
         ))
         conn.commit()
         conn.close()

         messagebox.showinfo("Success","Mmber has been inserted successfully")

    def fetch_data(self):
         

         try:
             conn=mysqlConn.connect(host="localhost",username="root",password="sangola",database="LibraryManagementSystem")
         except Exception as e:
              print("EXCEPTION", e)
         print("hi")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from Library")
         rows=my_cursor.fetchall()
          
          
         if len(rows)!=0:
              self.library_table.delete(*self.library_table.get_children())
              for i in rows:
                   self.library_table.insert("",END,values=i)
              conn.commit()
         conn.close()
    
    def get_cursor(self):
         cursor_row=self.library_table.focus()
         content=self.library_table.item (cursor_row)
         row=content['values']


         self.member_var.set(row[0])

 # Main function to run the application
if __name__ == "__main__":
     root = Tk()  # Initializing Tkinter root window
     obj = LibraryManagementSystem(root)  # Creating an instance of the LibraryManagementSystem class
     root.mainloop()  # Running the Tkinter event loop to display the window

