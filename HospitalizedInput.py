from tkinter import *
from tkinter import ttk
import pymysql
import mysql.connector

class Hospitalized:

    def __init__(self,root):
        def sel(self):
            print("baby")
        self.root=root
        self.root.title("Covid Cases Management System")
        self.root.geometry("1350x700+0+0")

        self.Spl_Id=StringVar()
        self.startDate=StringVar()
        self.endDate=StringVar()
        self.hosId=StringVar()
        self.docId=StringVar()

        self.Recovery_status=StringVar()
        self.search_value=StringVar()
        self.search_text=StringVar()

        title=Label(self.root,text="hospitalized",bd=10,relief=GROOVE,font=("roboto",35,"bold"))
        title.pack(side=TOP,fill=X)

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_frame.place(x=850,y=100,width=450,height=600)

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE)
        Detail_frame.place(x=20, y=100, width=800, height=560)

        m_title=Label(Manage_frame,text="Manage Patients",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lb1_splid=Label(Manage_frame,text="Spl Id",font=("times new roman",20))
        lb1_splid.grid(row=1, columnspan=1, pady=10,sticky="w")

        txt_Spl_id = Entry(Manage_frame,textvariable=self.Spl_Id, font=("times new roman", 15),)

        txt_Spl_id.grid(row=1, column=1, pady=10, sticky="w")

        lb1_Name = Label(Manage_frame, text="start Date", font=("times new roman", 20))
        lb1_Name.grid(row=2, columnspan=1, pady=10, sticky="w")

        txt_startDate = Entry(Manage_frame,textvariable=self.startDate, font=("times new roman", 15))
        txt_startDate.grid(row=2, column=1, pady=10, sticky="w")

        lb2_gender = Label(Manage_frame, text="enddate", font=("times new roman", 20))
        lb2_gender.grid(row=3, columnspan=1, pady=10, sticky="w")

        txt_endDate = Entry(Manage_frame, textvariable=self.endDate, font=("times new roman", 15))
        txt_endDate.grid(row=3, column=1, pady=10, sticky="w")

        lb2_Status = Label(Manage_frame, text="Doctor id", font=("times new roman", 20))
        lb2_Status.grid(row=4, columnspan=1, pady=10, sticky="w")

        txt_docId = Entry(Manage_frame, textvariable=self.docId, font=("times new roman", 15))
        txt_docId.grid(row=4, column=1, pady=10, sticky="w")

        Hos_id_Label = Label(Manage_frame, text="HospitalId", font=("times new roman", 20))
        Hos_id_Label.grid(row=5, columnspan=1, pady=10, sticky="w")

        txt_fam = Entry(Manage_frame,textvariable=self.hosId, font=("times new roman", 15))
        txt_fam.grid(row=5, column=1, pady=10, sticky="w")

        lb2_Status = Label(Manage_frame, text="Covid Status", font=("times new roman", 20))
        lb2_Status.grid(row=6, columnspan=1, pady=10, sticky="w")

        status_combo = ttk.Combobox(Manage_frame,textvariable=self.Recovery_status , font=("times new roman", 20),
                                    state="readonly", width=13)
        status_combo['values'] = ("Dead", "Under Recovery","Recovered")
        status_combo.grid(row=6, column=1, pady=10, sticky="w")

        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=10,y=500,width=420)

        add_btn=Button(btn_frame,command=self.add_hospitalizedResidents,text="Add",width=15).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_frame,command=self.update_data, text="Update", width=15).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=15).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame,command=self.Clear, text="Clear", width=15).grid(row=1, column=0, padx=10, pady=10)

        lb1_search=Label(Manage_frame ,text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=7, column=0, pady=10, sticky="w")

        search_combo = ttk.Combobox(Manage_frame,textvariable=self.search_value ,font=("times new roman", 20), state="readonly", width=10)
        search_combo['values'] = ("SplId", "Name")
        search_combo.grid(row=7, column=1, pady=10, sticky="w")

        txt_Search = Entry(Manage_frame, textvariable=self.search_text,font=("times new roman", 15))
        txt_Search.grid(row=8, column=1,padx=0, pady=10, sticky="w")

        search_btn = Button(btn_frame, command=self.search_data,text="Search", width=15).grid(row=1, column=1, padx=10, pady=10)
        show_btn = Button(btn_frame, command=self.fetch_data,text="Show_all", width=15).grid(row=1, column=2, padx=10, pady=10)


        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE)
        Table_frame.place(x=10,y=70,width=780,height=450)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.residents_table=ttk.Treeview(Table_frame,columns=("Spl Id","Name","Start Date","EndDate","hosId","HosName","docId","DocName","status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.residents_table.xview())
        scroll_y.config(command=self.residents_table.yview())

        self.residents_table.heading("Spl Id", text="Spl Id")
        self.residents_table.heading("Name", text="Name")
        self.residents_table.heading("Start Date", text="Start Date")
        self.residents_table.heading("EndDate", text="EndDate")
        self.residents_table.heading("hosId", text="hosId")
        self.residents_table.heading("HosName", text="HosName")
        self.residents_table.heading("docId", text="docId")
        self.residents_table.heading("DocName", text="DocName")
        self.residents_table.heading("status", text="status")
        self.residents_table["show"]="headings"
        self.residents_table.column("Spl Id",width=60)
        self.residents_table.column("Name", width=100)
        self.residents_table.column("Start Date", width=100)
        self.residents_table.column("EndDate", width=100)
        self.residents_table.column("hosId", width=50)
        self.residents_table.column("HosName", width=100)
        self.residents_table.column("docId", width=50)
        self.residents_table.column("DocName", width=100)
        self.residents_table.column("status", width=100)
        self.residents_table.pack(fill=BOTH,expand=1)
        self.residents_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.Clear()
        self.residents_table.pack()


    def add_hospitalizedResidents(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur=con.cursor()
        cur.execute("insert into hospitalized values(%s,%s,%s,%s,%s)",(self.Spl_Id.get(),self.hosId.get(),self.docId.get(),self.startDate.get(),self.endDate.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select a.`SplId`,a.Name,b.startDate,b.EndDate,c.hosId,c.hosName,d.docId,d.docName from doctors d,residents a,hospitalized b,hospitals c where a.`SplId`=b.splId and b.hosId=c.hosId and d.docId=b.docId")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.residents_table.delete(*self.residents_table.get_children())
            for row in rows:
                self.residents_table.insert('',END,values=row)

                con.commit()
        con.close()

    def Clear(self):
        self.Spl_Id.set("")
        self.startDate.set("")
        self.endDate.set("")
        self.hosId.set("")
        self.docId.set("")

    def get_cursor(self,eve):
        cursor_row=self.residents_table.focus()
        content=self.residents_table.item(cursor_row)
        row=content['values']
        self.Spl_Id.set(row[0])
        self.startDate.set(row[2])
        self.endDate.set(row[3])
        self.hosId.set(row[4])
        self.docId.set(row[6])

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("update hospitalized set `startDate`=%s,`EndDate`=%s,`hosId`=%s,`docId`=%s where `splId`=%s", (self.startDate.get(), self.endDate.get(), self.hosId.get(), self.docId.get(), self.Recovery_status.get(),self.Spl_Id.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("delete from hospitalized where `splId`="+self.Spl_Id.get())
        con.commit()

        self.fetch_data()
        self.Clear()
        con.close()

    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute(
            "select a.`SplId`,a.Name,b.startDate,b.EndDate,c.hosId,c.hosName,d.docId,d.docName from doctors d,residents a,hospitalized b,hospitals c where a.`SplId`=b.splId and b.hosId=c.hosId and d.docId=b.docId and a.`" + str(
                self.search_value.get()) + "` like '%" + str(self.search_text.get()) + "%'")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.residents_table.delete(*self.residents_table.get_children())
            for row in rows:
                self.residents_table.insert('',END,values=row)

                con.commit()
        con.close()

root=Tk()

ob=Hospitalized(root)
root.mainloop()

