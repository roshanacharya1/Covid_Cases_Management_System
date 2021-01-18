from tkinter import *
from tkinter import ttk

import mysql.connector

class students:

    def __init__(self,root):
        def sel(self):
            print("baby")
        self.root=root
        self.root.title("Covid Cases Management System")
        self.root.geometry("1350x700+0+0")

        self.Spl_Id=StringVar()
        self.Name=StringVar()
        self.Name=StringVar()
        self.gender=StringVar()
        self.covid_status=StringVar()
        self.Family_no=IntVar()
        self.search_value=StringVar()
        self.search_text=StringVar()

        title=Label(self.root,text="Residents",bd=10,relief=GROOVE,font=("roboto",35,"bold"))
        title.pack(side=TOP,fill=X)

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_frame.place(x=850,y=100,width=450,height=560)

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE)
        Detail_frame.place(x=20, y=100, width=800, height=560)

        m_title=Label(Manage_frame,text="Manage Residents",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lb1_splid=Label(Manage_frame,text="Spl Id",font=("times new roman",20))
        lb1_splid.grid(row=1, columnspan=1, pady=10,sticky="w")

        txt_Spl_id = Entry(Manage_frame,textvariable=self.Spl_Id, font=("times new roman", 15),)

        txt_Spl_id.grid(row=1, column=1, pady=10, sticky="w")

        lb1_Name = Label(Manage_frame, text="Name", font=("times new roman", 20))
        lb1_Name.grid(row=2, columnspan=1, pady=10, sticky="w")

        txt_Name = Entry(Manage_frame,textvariable=self.Name, font=("times new roman", 15))
        txt_Name.grid(row=2, column=1, pady=10, sticky="w")

        lb2_gender = Label(Manage_frame, text="Gender", font=("times new roman", 20))
        lb2_gender.grid(row=3, columnspan=1, pady=10, sticky="w")

        gender_combo=ttk.Combobox(Manage_frame,textvariable=self.gender,font=("times new roman" , 15),state="readonly",width=18)
        gender_combo['values']=("male","female","others")
        gender_combo.grid(row=3, column=1, pady=10, sticky="w" )

        lb2_Status = Label(Manage_frame, text="Covid Status", font=("times new roman", 20))
        lb2_Status.grid(row=4, columnspan=1, pady=10, sticky="w")

        status_combo = ttk.Combobox(Manage_frame,textvariable=self.covid_status, font=("times new roman", 15), state="readonly", width=18)
        status_combo['values'] = ("positive","negative")
        status_combo.grid(row=4, column=1, pady=10, sticky="w")

        fam_no = Label(Manage_frame, text="Family no", font=("times new roman", 20))
        fam_no.grid(row=5, columnspan=1, pady=10, sticky="w")

        txt_fam = Entry(Manage_frame,textvariable=self.Family_no, font=("times new roman", 15))
        txt_fam.grid(row=5, column=1, pady=10, sticky="w")



        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=10,y=450,width=420)

        add_btn=Button(btn_frame,command=self.add_rresidents,text="Add",width=15).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_frame,command=self.update_data, text="Update", width=15).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=15).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame,command=self.Clear, text="Clear", width=15).grid(row=1, column=0, padx=10, pady=10)

        lb1_search=Label(Manage_frame ,text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=6, column=0, pady=10, sticky="w")

        search_combo = ttk.Combobox(Manage_frame,textvariable=self.search_value ,font=("times new roman", 15), state="readonly", width=18)
        search_combo['values'] = ("SplId", "Name","CovidStatus","Family_no")
        search_combo.grid(row=6, column=1, pady=10, sticky="w")

        txt_Search = Entry(Manage_frame, textvariable=self.search_text,font=("times new roman", 15))
        txt_Search.grid(row=7, column=1,padx=0, pady=10, sticky="w")

        search_btn = Button(btn_frame, command=self.search_data,text="Search", width=15).grid(row=1, column=1, padx=10, pady=10)
        show_btn = Button(btn_frame, command=self.fetch_data,text="Show_all", width=15).grid(row=1, column=2, padx=10, pady=10)


        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE)
        Table_frame.place(x=10,y=60,width=780,height=450)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.residents_table=ttk.Treeview(Table_frame,columns=("Spl Id","Name","Covid Status","Gender","family no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.residents_table.xview())
        scroll_y.config(command=self.residents_table.yview())

        self.residents_table.heading("Spl Id", text="Spl Id")
        self.residents_table.heading("Name", text="Name")
        self.residents_table.heading("Covid Status", text="Covid Status")
        self.residents_table.heading("Gender", text="Gender")
        self.residents_table.heading("family no", text="Family no")
        self.residents_table["show"]="headings"
        self.residents_table.column("Spl Id",width=50)
        self.residents_table.column("Name", width=100)
        self.residents_table.column("Covid Status", width=100)
        self.residents_table.column("Gender", width=100)
        self.residents_table.column("family no", width=100)
        self.residents_table.pack(fill=BOTH,expand=1)
        self.residents_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.Clear()
        self.residents_table.pack()


    def add_rresidents(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur=con.cursor()
        cur.execute("insert into residents values(%s,%s,%s,%s,%s)",(self.Spl_Id.get(),self.Name.get(),self.gender.get(),self.covid_status.get(),self.Family_no.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select * from residents")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.residents_table.delete(*self.residents_table.get_children())
            for row in rows:
                self.residents_table.insert('',END,values=row)

                con.commit()
        con.close()

    def Clear(self):
        self.Spl_Id.set("")
        self.Family_no.set(0)
        self.covid_status.set("")
        self.gender.set("")
        self.Name.set("")

    def get_cursor(self,eve):
        cursor_row=self.residents_table.focus()
        content=self.residents_table.item(cursor_row)
        row=content['values']
        self.Spl_Id.set(row[0])
        self.Family_no.set(row[4])
        self.covid_status.set(row[3])
        self.gender.set(row[2])
        self.Name.set(row[1])
        print(str(self.Spl_Id.get()))

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("update residents set `Name`=%s,`Gender`=%s,`CovidStatus`=%s,`Family_no`=%s where `SplId`=%s", (self.Name.get(), self.gender.get(), self.covid_status.get(), self.Family_no.get(), self.Spl_Id.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("delete from residents where `SplId`="+str(self.Spl_Id.get()))
        con.commit()

        self.fetch_data()
        self.Clear()
        con.close()

    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select * from residents where`"+ str(self.search_value.get())+"` like '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.residents_table.delete(*self.residents_table.get_children())
            for row in rows:
                self.residents_table.insert('',END,values=row)

                con.commit()
        con.close()

root=Tk()

ob=students(root)
root.mainloop()

