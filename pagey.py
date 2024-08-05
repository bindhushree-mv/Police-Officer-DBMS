from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
global root
global root1
global root2
class police:
    def __init__(self,root1):
        self.root=root1
        self.root.title('police database')
        self.root.geometry('925x700+100+100')
        self.root.resizable(1,1)


        self.oid=StringVar()
        self.phone=StringVar()
        self.fname=StringVar()
        self.mname=StringVar()
        self.lname=StringVar()
        self.address=StringVar()
        self.age=StringVar()
        
        self.did=StringVar()
        self.cno=StringVar()
        self.plaintiff=StringVar()
        self.defendent=StringVar()
        self.ci=StringVar()
        self.cn = StringVar()
        self.cs = StringVar()
        self.del_id=StringVar()
        self.ser_id=StringVar() 

        lbltitle = Label(self.root, bd=0, relief=GROOVE, text="POLICE DATABASE MANAGEMENT", fg='#CD8C95', bg="white", font=("times new roman", 30, "bold"),height=2)
        lbltitle.pack(side=TOP, fill=BOTH, padx=0, pady=0)

    #=================button frame==================
        buttonframe=Frame(self.root,bd=0,bg='#EED5D2',relief=GROOVE)
        buttonframe.place(x=0,y=69,width=1535,height=60)

        #========DATAFRAME===========
        
        dataframe=Frame(self.root,bd=0,bg='#CD8C95',relief=GROOVE)
        dataframe.place(x=0,y=130,width=1535,height=400)

        dataframe2=LabelFrame(dataframe,bd=5,bg='#EED5D2',relief=GROOVE,padx=10,
                                                           font=("times new roman", 12, "bold"),text="Officer_Information" )
        dataframe2.place(x=20,y=15,width=485,height=368)

        dataframe3=LabelFrame(dataframe,bd=5,relief=GROOVE,bg='#EED5D2',padx=10,
                                                           font=("times new roman", 12, "bold"),text="Case_Information" )
        dataframe3.place(x=527,y=15,width=485,height=368)

        dataframe4=Frame(dataframe,bd=5,relief=GROOVE,bg='#EED5D2',padx=10)
                                                          
        dataframe4.place(x=1035,y=15,width=485,height=368)


        #====================display_frame============
        displayframe=Frame(self.root,bd=5,bg='light pink',relief=GROOVE)
        displayframe.place(x=0,y=530,width=900,height=270)

        displayf_case=Frame(self.root,bd=5,bg='light pink',relief=GROOVE)
        displayf_case.place(x=900,y=530,width=630,height=270)

        #----------------------entryfields---------------------
        
        officerid=Label(dataframe2,text="Officer_ID: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=15,pady=12)
        officerid.grid(row=0,column=0)
        e_officerid=Entry(dataframe2,textvariable=self.oid,font=("times new roman", 12, "bold"),width=30)
        e_officerid.grid(row=0,column=1)

        fname=Label(dataframe2,text="Phone_num: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=15,pady=8)
        fname.grid(row=1,column=0)
        e_fname=Entry(dataframe2,textvariable=self.phone,font=("times new roman", 12, "bold"),width=30)
        e_fname.grid(row=1,column=1)
        
        mname=Label(dataframe2,text="First_Name: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=15,pady=8)
        mname.grid(row=2,column=0)
        e_mname=Entry(dataframe2,textvariable=self.fname,font=("times new roman", 12, "bold"),width=30)
        e_mname.grid(row=2,column=1)

        mname=Label(dataframe2,text="Middle_Name: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=15,pady=8)
        mname.grid(row=3,column=0)
        e_mname=Entry(dataframe2,textvariable=self.mname,font=("times new roman", 12, "bold"),width=30)
        e_mname.grid(row=3,column=1)

        ophone=Label(dataframe2,text="Last_Name: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=15,pady=8)
        ophone.grid(row=4,column=0)
        e_ophone=Entry(dataframe2,textvariable=self.lname,font=("times new roman", 12, "bold"),width=30)
        e_ophone.grid(row=4,column=1)

        oage=Label(dataframe2,text="Age: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=25,pady=8)
        oage.grid(row=5,column=0)
        e_oage=Entry(dataframe2,textvariable=self.age,font=("times new roman", 12, "bold"),width=30)
        e_oage.grid(row=5,column=1)

        oaddress=Label(dataframe2,text="Address: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=15,pady=8)
        oaddress.grid(row=6,column=0)
        e_oaddress=Entry(dataframe2,textvariable=self.address,font=("times new roman", 12, "bold"),width=30)
        e_oaddress.grid(row=6,column=1)

        did=Label(dataframe2,text="Department_ID: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=8)
        did.grid(row=7,column=0)
        e_did=Entry(dataframe2,textvariable=self.did,font=("times new roman", 12, "bold"),width=30)
        e_did.grid(row=7,column=1)
        

        cno=Label(dataframe3,text="Case_No: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=10)
        cno.grid(row=0,column=0)
        e_cno=Entry(dataframe3,textvariable=self.cno,font=("times new roman", 12, "bold"),width=30)
        e_cno.grid(row=0,column=1)

        plaintiff=Label(dataframe3,text="Plaintiff: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=10)
        plaintiff.grid(row=1,column=0)
        e_plaintiff=Entry(dataframe3,textvariable=self.plaintiff,font=("times new roman", 12, "bold"),width=30)
        e_plaintiff.grid(row=1,column=1)

        defendant=Label(dataframe3,text="Defendant: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=10)
        defendant.grid(row=2,column=0)
        e_defendent=Entry(dataframe3,textvariable=self.defendent,font=("times new roman", 12, "bold"),width=30)
        e_defendent.grid(row=2,column=1)

        ci=Label(dataframe3,text="Ci_Penology: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=10)
        ci.grid(row=3,column=0)
        e_ci=Entry(dataframe3,textvariable=self.ci,font=("times new roman", 12, "bold"),width=30)
        e_ci.grid(row=3,column=1)

        cn=Label(dataframe3,text="Case_Number: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=10)
        cn.grid(row=4,column=0)
        e_cn=Entry(dataframe3,textvariable=self.cn,font=("times new roman", 12, "bold"),width=30)
        e_cn.grid(row=4,column=1)

        cs=Label(dataframe3,text="Case_status: ",bg='#EED5D2',font=("times new roman", 12, "bold"),padx=5,pady=10)
        cs.grid(row=5,column=0)
        e_cs=Entry(dataframe3,textvariable=self.cs,font=("times new roman", 12, "bold"),width=30)
        e_cs.grid(row=5,column=1)

        #-------------------buttons---------------------
        insertbutton=Button(buttonframe,bg='#CD8C95',command=self.iinsert,fg='white',text="INSERT",font=("times new roman", 12, "bold"))
        insertbutton.place(x=200,y=12,width=160)

        insertcase=Button(buttonframe,bg='#CD8C95',fg='white',command=self.insert_case,text="INSERT_CASE",font=("times new roman", 12, "bold"))
        insertcase.place(x=400,y=12,width=160)

        updatebutton=Button(buttonframe,bg='#CD8C95',fg='white',command=self.update_o,text="UPDATE_OFFICER",font=("times new roman", 12, "bold"))
        updatebutton.place(x=600,y=12,width=200)

        searchbutton=Button(buttonframe,bg='#CD8C95',fg='white',command=self.search_data,text="SEARCH",font=("times new roman", 12, "bold"))
        searchbutton.place(x=830,y=12,width=160)

        dbutton=Button(buttonframe,bg='#CD8C95',fg='white',command=self.delete_data,text="DELETE",font=("times new roman", 12, "bold"))
        dbutton.place(x=1030,y=12,width=160)

        re_button=Button(dataframe4,bg='#CD8C95',fg='white',command=self.fatch_data,text="REFRESH",font=("times new roman", 12, "bold"),width=25,padx=8,pady=5)
        re_button.grid(row=17,column=1)

        searchhh=Label(dataframe4,bg='#EED5D2',text="",font=("times new roman", 12, "bold"),padx=15,pady=3)
        searchhh.grid(row=18,column=0)

        clear=Button(dataframe4,bg='#CD8C95',fg='white',command=self.clear_data,text="CLEAR",font=("times new roman", 12, "bold"),width=25,padx=8,pady=5)
        clear.grid(row=19,column=1)

        update_case=Button(dataframe3,bg='#CD8C95',fg='white',command=self.update_c,text="UPDATE_CASE",font=("times new roman", 12, "bold"),width=25,padx=5,pady=5)
        update_case.grid(row=13,column=1)


        #================table================
        #-------------------------scroller-----------------
        scroll_x=ttk.Scrollbar(displayframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(displayframe,orient=VERTICAL)
        self.display_table=ttk.Treeview(displayframe,column=("officer_id","officer_phone","first_name","middle_name","last_name","age","address","d_id"
                                                       ),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_xx=ttk.Scrollbar(displayf_case,orient=HORIZONTAL)
        scroll_yy=ttk.Scrollbar(displayf_case,orient=VERTICAL)
        self.display_case=ttk.Treeview(displayf_case,column=("ci_number","plaintiff",
                                                       "defendant","ci_penology" ,"case_num","case_status"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set) 
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.display_table.xview)
        scroll_y=ttk.Scrollbar(command=self.display_table.yview)

                
        scroll_xx.pack(side=BOTTOM,fill=X)
        scroll_yy.pack(side=RIGHT,fill=Y)

        scroll_xx=ttk.Scrollbar(command=self.display_case.xview)
        scroll_yy=ttk.Scrollbar(command=self.display_case.yview)

        self.display_table.heading("officer_id",text="Officer ID")
        self.display_table.heading("officer_phone",text="Phone No")
        self.display_table.heading("first_name",text="First Name")
        self.display_table.heading("middle_name",text="Middle Name")
        self.display_table.heading("last_name",text="Last Name")
        self.display_table.heading("age",text="Age") 
        self.display_table.heading("address",text="Address")
        
        self.display_table.heading("d_id",text="Department ID")

        self.display_case.heading("ci_number",text="Case No")
        self.display_case.heading("plaintiff",text="Plaintiff")
        self.display_case.heading("defendant",text="Defendant")
        self.display_case.heading("ci_penology",text="Ci_Penology")
        self.display_case.heading("case_num",text="Case_number")
        self.display_case.heading("case_status",text="Case_status")
        self.display_table["show"]="headings"
        self.display_case["show"]="headings" 


        self.display_table.pack(fill=BOTH,expand=1)
        self.display_table.column("officer_id",width=100)
        self.display_table.column("officer_phone",width=100)
        self.display_table.column("first_name",width=100)
        self.display_table.column("middle_name",width=100)
        self.display_table.column("last_name",width=100)
        self.display_table.column("age",width=100)
        self.display_table.column("address",width=100)       
        self.display_table.column("d_id",width=100)
        
        self.display_case.column("ci_number",width=100)
        self.display_case.column("plaintiff",width=100)
        self.display_case.column("defendant",width=100)
        self.display_case.column("ci_penology",width=100)
        self.display_case.column("case_num",width=100)
        self.display_case.column("case_status",width=100)

        self.display_table.pack(fill=BOTH,expand=1)
        self.display_table.bind("<ButtonRelease-1>",self.get_cursor1)

        self.display_case.pack(fill=BOTH,expand=1)
        self.display_case.bind("<ButtonRelease-1>",self.get_cursor2)

        delete=Label(dataframe4,bg='#EED5D2',text="",font=("times new roman", 12, "bold"),padx=15,pady=4)
        delete.grid(row=0,column=0)

        delete=Label(dataframe4,bg='#EED5D2',text="Delete: ",font=("times new roman", 12, "bold"),padx=15,pady=8)
        delete.grid(row=3,column=0)
        e_mname=Entry(dataframe4,textvariable=self.del_id,font=("times new roman", 12, "bold"),width=30)
        e_mname.grid(row=3,column=1)

        search=Label(dataframe4,bg='#EED5D2',text="Search: ",font=("times new roman", 12, "bold"),padx=15,pady=8)
        search.grid(row=15,column=0)
        e_search=Entry(dataframe4,textvariable=self.ser_id,font=("times new roman", 12, "bold"),width=30)
        e_search.grid(row=15,column=1)

        searchh=Label(dataframe4,bg='#EED5D2',text="",font=("times new roman", 12, "bold"),padx=15,pady=3)
        searchh.grid(row=16,column=0)

        self.fatch_data()
       #___________________________________functinality______________________________
    def iinsert(self):
        if self.oid.get()=="":
            messagebox.showerror("Error","Officer_ID should not be empty.")
        
        else:           
            conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM officer WHERE officer_id = %s", (self.oid.get(),))
            existing_record = my_cursor.fetchone()
            if existing_record:
                messagebox.showerror("Error", "Officer_ID already present.")
            else:
                my_cursor.execute("INSERT INTO officer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                              (self.oid.get(), self.phone.get(), self.fname.get(), self.mname.get(),
                               self.lname.get(), self.age.get(), self.address.get(), self.did.get()))
                messagebox.showinfo("success","Record has been inserted successfully")
            conn.commit()   
            self.fatch_data()
            conn.close()

            #`````````````````````````````````````````````````````````
    def insert_case(self):
        if self.cno.get()=="" :
            messagebox.showerror("Error","ci_number should not be empty.")
        else:           
            conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM case_information WHERE ci_number = %s", (self.cno.get(),))
            existing_record = my_cursor.fetchone()
            if existing_record:
                messagebox.showerror("Error", "Officer_ID already present.")
            else:
                my_cursor.execute("insert into case_information values(%s,%s,%s,%s,%s,%s)",(
                                self.cno.get(),
                                self.plaintiff.get(),
                                self.defendent.get(),
                                self.ci.get(),
                                self.cn.get(),
                                self.cs.get()))
                messagebox.showinfo("success","Record has been inserted successfully")
                
            conn.commit()
            self.fatch_data()
            conn.close()
            #messagebox.showinfo("success","Record has been inserted successfully")
    def update_o(self):
        officer_id = self.oid.get()
        
        officer_phone =self.phone.get()
        first_name=self.fname.get()
        middle_name =self.mname.get()
        last_name =self.lname.get()    
        age=self.age.get()                                   
        address=self.address.get()
           
        if self.oid.get()=="":           
            messagebox.showerror("Error","Officer_ID should not be empty.00 ")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE `officer` SET `officer_phone` = %s, `first_name` = %s, `middle_name` = %s, `last_name` = %s, `address` = %s, `age` = %s WHERE `officer_id` = %s", (officer_phone, first_name, middle_name, last_name, address, age, officer_id))
            my_cursor.execute("commit")
            #self.fatch_data()
            conn.close()
            messagebox.showinfo("success","Record has been updated successfully")

    def update_c(self):
        ci_number=self.cno.get()
        plaintiff=self.plaintiff.get()
        defendant=self.defendent.get()
        ci_penology= self.ci.get()
        case_num = self.cn.get()
        case_status = self.cs.get()
        officer_id = self.oid.get()

        if self.cno.get()=="" :
            messagebox.showerror("Error","case_id should not be empty.")
        else:
            
            conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE `case_information` SET `plaintiff` = %s, `defendant` = %s, `ci_penology` = %s, `case_num` = %s, `case_status` = %s WHERE `ci_number` = %s", (plaintiff, defendant, ci_penology, case_num, case_status, ci_number))
            my_cursor.execute("commit")
            #conn.commit()
            #self.fatch_data()
            conn.close()
            messagebox.showinfo("success","Record has been updated successfully")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
        my_cursor1=conn.cursor()
        my_cursor1.execute("select * from officer")
        rows=my_cursor1.fetchall()
        print(len(rows))
        if len(rows)!=0:
            self.display_table.delete(*self.display_table.get_children())           
            #self.case_information.delete(*self.case_information.get_children())
            for i in rows:
                self.display_table.insert("",END,values=i)
                #self.officer.insert("",END,values=i)
            conn.commit()
        #conn.close()
        my_cursor2=conn.cursor()
        my_cursor2.execute("select * from case_information")
        rows=my_cursor2.fetchall()
        print(len(rows))
        if len(rows)!=0:
            self.display_case.delete(*self.display_case.get_children())           
            #self.case_information.delete(*self.case_information.get_children())
            for i in rows:
                self.display_case.insert("",END,values=i)
                #self.officer.insert("",END,values=i)
            conn.commit()
        conn.close()
###############################################

    def fatch_data_search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM case_information ci,worked_on w WHERE w.c_num = ci.case_num and w.officer_idd = %s", (self.ser_id.get(),))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.display_case.delete(*self.display_case.get_children())
            #self.case_information.delete(*self.case_information.get_children())
            for i in rows:
                self.display_case.insert("",END,values=i)
                #self.officer.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def clear_data(self):
            
        self.oid.set("")
        self.phone.set("")
        self.fname.set("")
        self.mname.set("")
        self.lname.set("")
        self.address.set("")
        self.age.set("")
        
        self.did.set("")
        self.cno.set("")
        self.plaintiff.set("")
        self.defendent.set("")
        self.ci.set("")
        self.cn.set("")
        self.cs.set("")

        self.del_id.set("")
        self.ser_id.set("")

    def delete_data(self):
        if self.del_id.get()=="":
            messagebox.showerror("Error","enter some valid id.")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bindhu@0103",database="police")
            my_cursor=conn.cursor()
            my_cursor.execute("delete from officer where officer_id ='"+ self.del_id.get()+"'")
            conn.commit()
            self.fatch_data()
        conn.close()
        messagebox.showinfo("DELETE","ts deleted successfully")

    def search_data(self):
        
        if self.ser_id.get() == "":
            messagebox.showerror("Error", "Enter some valid id.")
        else:
            self.fatch_data_search()

    def get_cursor1(self,event=""):
        cursor_row=self.display_table.focus()
        content=self.display_table.item(cursor_row)
        row=content["values"]
        self.oid.set(row[0])
        self.phone.set(row[1])
        self.fname.set(row[2])
        self.mname.set(row[3])
        self.lname.set(row[4]) 
        self.age.set(row[5])     
        self.address.set(row[6]) 
        self.did.set(row[7])
        
    
    def get_cursor2(self,event=""):
        cursor_row=self.display_case.focus()
        content=self.display_case.item(cursor_row)
        row=content["values"]
    
        self.cno.set(row[0])
        self.plaintiff.set(row[1])
        self.defendent.set(row[2])
        self.ci.set(row[3])
        self.cn.set(row[4])
        self.cs.set(row[5])

if __name__ == "__main__":
    root1 = Tk()
    police(root1)
    root1.mainloop()



