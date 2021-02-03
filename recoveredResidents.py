from tkinter import *
from tkinter import ttk
import pymysql
import mysql.connector

class Quarantined:

    def __init__(self,root):
        def sel(self):
            print("baby")
        self.root=root
        self.root.title("Covid Cases Management System")
        self.root.geometry("1350x700+0+0")

        self.Spl_Id=StringVar()
        self.recovDate=StringVar()
        self.Place_Id=StringVar()
        self.hoId=StringVar()
        self.search_value=StringVar()
        self.search_text=StringVar()

        title=Label(self.root,text="Recovered",bd=10,relief=GROOVE,font=("roboto",35,"bold"))
        title.pack(side=TOP,fill=X)

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_frame.place(x=850,y=100,width=450,height=560)

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE)
        Detail_frame.place(x=20, y=100, width=800, height=560)

        m_title=Label(Manage_frame,text="Manage Recovered Residents",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lb1_splid=Label(Manage_frame,text="Spl Id",font=("times new roman",20))
        lb1_splid.grid(row=1, columnspan=1, pady=10,sticky="w")

        txt_Spl_id = Entry(Manage_frame,textvariable=self.Spl_Id, font=("times new roman", 15),)

        txt_Spl_id.grid(row=1, column=1, pady=10, sticky="w")

        lb1_recoveryDate = Label(Manage_frame, text="Recovery Date", font=("times new roman", 20))
        lb1_recoveryDate.grid(row=2, columnspan=1, pady=10, sticky="w")

        txt_recoveryDate = Entry(Manage_frame,textvariable=self.recovDate, font=("times new roman", 15))
        txt_recoveryDate.grid(row=2, column=1, pady=10, sticky="w")

        lb2_hospId = Label(Manage_frame, text="hospital id", font=("times new roman", 20))
        lb2_hospId.grid(row=3, columnspan=1, pady=10, sticky="w")

        txt_hospId = Entry(Manage_frame, textvariable=self.hoId, font=("times new roman", 15))
        txt_hospId.grid(row=3, column=1, pady=10, sticky="w")

        lb2_placeId = Label(Manage_frame, text="Place Id", font=("times new roman", 20))
        lb2_placeId.grid(row=4, columnspan=1, pady=10, sticky="w")

        txt_placeId = Entry(Manage_frame, textvariable=self.Place_Id, font=("times new roman", 15))
        txt_placeId.grid(row=4, column=1, pady=10, sticky="w")



        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=10,y=450,width=420)

        add_btn=Button(btn_frame,command=self.add_quarantined,text="Add",width=15).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_frame,command=self.update_data, text="Update", width=15).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=15).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame,command=self.Clear, text="Clear", width=15).grid(row=1, column=0, padx=10, pady=10)

        lb1_search=Label(Manage_frame ,text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=6, column=0, pady=10, sticky="w")

        search_combo = ttk.Combobox(Manage_frame,textvariable=self.search_value ,font=("times new roman", 20), state="readonly", width=10)
        search_combo['values'] = ("SplId", "Name")
        search_combo.grid(row=6, column=1, pady=10, sticky="w")

        txt_Search = Entry(Manage_frame, textvariable=self.search_text,font=("times new roman", 15))
        txt_Search.grid(row=7, column=1,padx=0, pady=10, sticky="w")

        search_btn = Button(btn_frame, command=self.search_data,text="Search", width=15).grid(row=1, column=1, padx=10, pady=10)
        show_btn = Button(btn_frame, command=self.fetch_data,text="Show_all", width=15).grid(row=1, column=2, padx=10, pady=10)


        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE)
        Table_frame.place(x=10,y=70,width=780,height=450)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.Recovered_table=ttk.Treeview(Table_frame,columns=("Spl Id","Name","Recovery date","Place Id","Place Name","Hospital Id","Hospital Name"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Recovered_table.xview())
        scroll_y.config(command=self.Recovered_table.yview())

        self.Recovered_table.heading("Spl Id", text="Spl Id")
        self.Recovered_table.heading("Name", text="Name")
        self.Recovered_table.heading("Recovery date", text="Recovery date")
        self.Recovered_table.heading("Place Id", text="Plaace Id")
        self.Recovered_table.heading("Place Name", text="Place Name")

        self.Recovered_table.heading("Hospital Id", text="Hospital Id")

        self.Recovered_table.heading("Hospital Name", text="Hospital Name")
        self.Recovered_table["show"]="headings"
        self.Recovered_table.column("Spl Id",width=50)
        self.Recovered_table.column("Name", width=100)
        self.Recovered_table.column("Recovery date", width=100)
        self.Recovered_table.column("Place Id", width=100)
        self.Recovered_table.column("Place Name", width=100)
        self.Recovered_table.column("Hospital Id", width=100)
        self.Recovered_table.column("Hospital Name", width=100)
        self.Recovered_table.pack(fill=BOTH,expand=1)
        self.Recovered_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.Clear()
        self.Recovered_table.pack()


    def add_quarantined(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur=con.cursor()
        cur.execute("insert into recovered values(%s,%s,%s,%s)",(self.Spl_Id.get(),self.recovDate.get(),self.hoId.get(),self.Place_Id.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select a.`SplId`,a.Name,b.RecovDate,b.Place_Id,c.PLace_naem,b.hosId,d.hosName from residents a,recovered b,quarantine_center c,hospitals d where a.`SplId`=b.splid and b.Place_Id=c.Place_id and b.hosId=d.hosId")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Recovered_table.delete(*self.Recovered_table.get_children())
            for row in rows:
                self.Recovered_table.insert('',END,values=row)

                con.commit()
        con.close()

    def Clear(self):
        self.Spl_Id.set("")
        self.recovDate.set("")
        self.Place_Id.set("")
        self.hoId.set("")

    def get_cursor(self,eve):
        cursor_row=self.Recovered_table.focus()
        content=self.Recovered_table.item(cursor_row)
        row=content['values']
        self.Spl_Id.set(row[0])
        self.recovDate.set(row[2])
        self.hoId.set(row[5])
        self.Place_Id.set(row[3])

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("update recovered set `RecovDate`=%s,`Plce_Id`=%s,`hosId`=%s where `splId`=%s" , (self.recovDate.get(), self.Place_Id.get(), self.hoId.get(), self.Spl_Id.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("delete from recovered where `splId`="+self.Spl_Id.get())
        con.commit()

        self.fetch_data()
        self.Clear()
        con.close()

    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute(
            "select a.`SplId`,a.Name,b.RecovDate,b.Place_Id,c.PLace_naem,b.hosId,d.hosName from residents a,recovered b,quarantine_center c,hospitals d where a.`SplId`=b.splid and b.Place_Id=c.Place_id and b.hosId=d.hosId and a.`"+ str(self.search_value.get())+"` like '%" + str(self.search_text.get()) + "%'")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.Recovered_table.delete(*self.Recovered_table.get_children())
            for row in rows:
                self.Recovered_table.insert('',END,values=row)

                con.commit()
        con.close()

root=Tk()

ob=Quarantined(root)
root.mainloop()

