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

        self.SplId=StringVar()
        self.deathDate=StringVar()
        self.hosId=StringVar()
        self.Place_Id=StringVar()
        self.search_value=StringVar()
        self.search_text=StringVar()


        title=Label(self.root,text="Deaths",bd=10,relief=GROOVE,font=("roboto",35,"bold"))
        title.pack(side=TOP,fill=X)

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_frame.place(x=850,y=100,width=450,height=600)

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE)
        Detail_frame.place(x=20, y=100, width=800, height=560)

        m_title=Label(Manage_frame,text="Manage Deaths",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lb1_splid=Label(Manage_frame,text="Spl Id",font=("times new roman",20))
        lb1_splid.grid(row=1, columnspan=1, pady=10,sticky="w")

        txt_Spl_id = Entry(Manage_frame,textvariable=self.SplId, font=("times new roman", 15),)

        txt_Spl_id.grid(row=1, column=1, pady=10, sticky="w")

        lb1_DeathDate = Label(Manage_frame, text="Death Date", font=("times new roman", 20))
        lb1_DeathDate.grid(row=2, columnspan=1, pady=10, sticky="w")

        txt_deathDate = Entry(Manage_frame,textvariable=self.deathDate, font=("times new roman", 15))
        txt_deathDate.grid(row=2, column=1, pady=10, sticky="w")

        lb2_hospId = Label(Manage_frame, text="Hospital Id", font=("times new roman", 20))
        lb2_hospId.grid(row=3, columnspan=1, pady=10, sticky="w")

        txt_hosId = Entry(Manage_frame, textvariable=self.hosId, font=("times new roman", 15))
        txt_hosId.grid(row=3, column=1, pady=10, sticky="w")

        lb2_placeId = Label(Manage_frame, text="Place id", font=("times new roman", 20))
        lb2_placeId.grid(row=4, columnspan=1, pady=10, sticky="w")

        txt_placeId = Entry(Manage_frame, textvariable=self.Place_Id, font=("times new roman", 15))
        txt_placeId.grid(row=4, column=1, pady=10, sticky="w")


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
        self.Deaths_table=ttk.Treeview(Table_frame,columns=("Spl Id","Name","Death Date","hosId","Place_Id"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Deaths_table.xview())
        scroll_y.config(command=self.Deaths_table.yview())

        self.Deaths_table.heading("Spl Id", text="Spl Id")
        self.Deaths_table.heading("Name", text="Name")
        self.Deaths_table.heading("Death Date", text="Start Date")
        self.Deaths_table.heading("hosId", text="hosId")
        self.Deaths_table.heading("Place_Id", text="Place_Id")
        self.Deaths_table["show"]="headings"
        self.Deaths_table.column("Spl Id",width=50)
        self.Deaths_table.column("Name", width=100)
        self.Deaths_table.column("Death Date", width=100)
        self.Deaths_table.column("hosId", width=50)
        self.Deaths_table.column("Place_Id", width=50)
        self.Deaths_table.pack(fill=BOTH,expand=1)
        self.Deaths_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.Clear()
        self.Deaths_table.pack()


    def add_hospitalizedResidents(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur=con.cursor()
        cur.execute("insert into deaths values(%s,%s,%s,%s)",(self.SplId.get(),self.deathDate.get(),self.hosId.get(),self.Place_Id.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select a.`SplId`,a.Name,b.Deathdate,b.hosId,b.Place_Id from residents a,deaths b where a.`SplId`=b.splId")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Deaths_table.delete(*self.Deaths_table.get_children())
            for row in rows:
                self.Deaths_table.insert('',END,values=row)

                con.commit()
        con.close()

    def Clear(self):
        self.SplId.set("")
        self.deathDate.set("")
        self.hosId.set("")
        self.Place_Id.set("")

    def get_cursor(self,eve):
        cursor_row=self.Deaths_table.focus()
        content=self.Deaths_table.item(cursor_row)
        row=content['values']
        self.SplId.set(row[0])
        self.deathDate.set(row[2])
        self.hosId.set(row[3])
        self.Place_Id.set(row[4])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="residents")
        cur = con.cursor()
        cur.execute("update deaths set `DeathDate`=%s,`hosId`=%s,`Place_Id`=%s where `splId`=%s", (self.deathDate.get(), self.hosId.get(), self.Place_Id.get(),self.SplId.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("delete from deaths where `splId`="+str(self.SplId.get()))
        con.commit()

        self.fetch_data()
        self.Clear()
        con.close()

    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute(
            "select a.`SplId`,a.Name,b.Deathdate,b.hosId,b.Place_Id from residents a,deaths b where a.`SplId`=b.splId and a.`" + str(
                self.search_value.get()) + "` like '%" + str(self.search_text.get()) + "%'")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.Deaths_table.delete(*self.Deaths_table.get_children())
            for row in rows:
                self.Deaths_table.insert('',END,values=row)

                con.commit()
        con.close()

root=Tk()

ob=Hospitalized(root)
root.mainloop()

