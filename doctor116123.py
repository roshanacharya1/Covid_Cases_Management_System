from tkinter import *
from tkinter import ttk
import pymysql
import mysql.connector


class residents:
    def __init__(self, root):
        def sel(self):
            print("baby")

        def Deaths_window(frame):
            frame.tkraise()
        def Table_window(frame):
            frame.tkraise()
        def Hospitalized_window(frame):
            frame.tkraise()
        def Recovered_window(frame):
            frame.tkraise()
        def HospitalInfo_window(frame):
            frame.tkraise()

        def Quarantined_window(frame):
            frame.tkraise()
        self.root = root
        self.root.title("Doctors Panel")
        self.root.geometry("1350x700+0+0")

        self.Spl_Id = StringVar()
        self.Name = StringVar()
        self.gender = StringVar()
        self.covid_status = StringVar()
        self.Family_no = IntVar()
        self.search_value = StringVar()
        self.search_text = StringVar()
        self.Hos_Id=StringVar()
        self.Hos_name=StringVar()
        self.searchHosInfo_value = StringVar()
        self.searchHosInfo_Text = StringVar()
        self.Deaths_Text=StringVar()
        self.Deaths_Value=StringVar()
        self.Recovered_Text = StringVar()
        self.Recovered_Value = StringVar()
        self.Quarantined_Text = StringVar()
        self.Quarantined_Value = StringVar()

        self.Hospitalized_Text = StringVar()
        self.Hospitalized_Value = StringVar()

        title = Label(self.root, text="Doctors Panel", bg="grey", bd=10, relief=GROOVE, font=("roboto", 35, "bold"))
        title.pack(side=TOP, fill=X)

        Buttons_frame = Frame(self.root, bd=4, relief=RIDGE)
        Buttons_frame.place(x=20, y=100, width=250, height=560)

        HospitalInfo_btn = Button(Buttons_frame,command=lambda:HospitalInfo_window(HospitalInfo_frame) ,text="Hospital Info", width=30).grid(row=0, column=0, padx=10, pady=10)

        Deaths_btn = Button(Buttons_frame, text="Deaths",command=lambda: Deaths_window(Death_frame), width=30).grid(row=1, column=0,
                                                                                                padx=10, pady=10)

        Recovered_btn = Button(Buttons_frame,command=lambda: Recovered_window(Recovered_frame), text="Recovered", width=30).grid(row=2, column=0, padx=10, pady=10)
        quarantined_btn = Button(Buttons_frame,command=lambda: Quarantined_window(Quarantine_frame), text="Quarantined", width=30).grid(row=3, column=0, padx=10, pady=10)
        Hospitalized_btn = Button(Buttons_frame,command=lambda:Hospitalized_window(Hospitalized_frame), text="Hospitalized", width=30).grid(row=4, column=0, padx=10, pady=10)
        Residents_btn = Button(Buttons_frame,command=lambda: Table_window(Table_frame) , text="Residents Data", width=30).grid(row=5, column=0, padx=10, pady=10)

        txt_Spl_id = Entry(Buttons_frame, textvariable=self.Spl_Id, font=("times new roman", 15), )
        txt_Spl_id.config(state='readonly')
        txt_Spl_id.grid(row=6, column=0, pady=10, sticky="w", padx=10)

        txt_Name = Entry(Buttons_frame, textvariable=self.Name, font=("times new roman", 15))
        txt_Name.config(state='readonly')
        txt_Name.grid(row=7, column=0, pady=10, sticky="w", padx=10)

        status_combo = ttk.Combobox(Buttons_frame, textvariable=self.covid_status, font=("times new roman", 20),
                                    state="readonly", width=13)
        status_combo['values'] = ("positive", "negative")
        status_combo.grid(row=8, column=0, pady=10, sticky="w", padx=10)

        update_btn = Button(Buttons_frame, command=self.update_data, text="Update", width=30).grid(row=9, column=0,
                                                                                                   padx=10, pady=10)

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE)
        Detail_frame.place(x=300, y=100, width=1020, height=550)

      #Death Fram -----------------------------------------------------------------------------------------------------------------
        Death_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        Death_frame.place(x=0, y=0, width=1010, height=540)
        SearchDeath_frame = Frame(Death_frame, bd=4, relief=RIDGE)
        SearchDeath_frame.place(x=10, y=0, width=930, height=60)
        lb1_search = Label(SearchDeath_frame, text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=0, column=0, pady=10, sticky="w")

        searchDeath_combo = ttk.Combobox(SearchDeath_frame, textvariable=self.Deaths_Value, font=("times new roman", 20),
                                    state="readonly", width=10)
        searchDeath_combo['values'] = ("SplId", "Name")
        searchDeath_combo.grid(row=0, column=1, pady=10, sticky="w")

        txt_Search = Entry(SearchDeath_frame, textvariable=self.Deaths_Text, font=("times new roman", 15))
        txt_Search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        searchDeath_btn = Button(SearchDeath_frame, text="Search", command=self.searchDeath_data, width=10).grid(row=0, column=3,
                                                                                                  padx=10, pady=10)
        showDeaths_btn = Button(SearchDeath_frame, text="Show_all",command=self.fetchDeath_data, width=10).grid(row=0, column=4,
                                                                                                 padx=10, pady=10)
        TableDeathData_frame = Frame(Death_frame, bd=4, relief=RIDGE)
        TableDeathData_frame.place(x=10, y=70, width=930, height=450)


        scroll_x = Scrollbar(TableDeathData_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(TableDeathData_frame, orient=VERTICAL)
        self.Deaths_table = ttk.Treeview(TableDeathData_frame,
                                            columns=("Spl Id", "Name", "Death date", "hospId", "Hospital name"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Deaths_table.xview())
        scroll_y.config(command=self.Deaths_table.yview())

        self.Deaths_table.heading("Spl Id", text="Spl Id")
        self.Deaths_table.heading("Name", text="Name")
        self.Deaths_table.heading("Death date", text="Death date")
        self.Deaths_table.heading("hospId", text="hospId")
        self.Deaths_table.heading("Hospital name", text="Hospital name")
        self.Deaths_table["show"] = "headings"
        self.Deaths_table.column("Spl Id", width=50)
        self.Deaths_table.column("Name", width=100)
        self.Deaths_table.column("Death date", width=100)
        self.Deaths_table.column("hospId", width=100)
        self.Deaths_table.column("Hospital name", width=100)
        self.Deaths_table.pack(fill=BOTH, expand=1)

        self.Deaths_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchDeath_data()
        self.Deaths_table.pack()

        #--------------------------------------------------------------------------------------------------------------------------------------------------------
        HospitalInfo_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        HospitalInfo_frame.place(x=0, y=0, width=1010, height=540)

        # Hospital info Fram -----------------------------------------------------------------------------------------------------------------

        SearchHospitalInfo_frame = Frame(HospitalInfo_frame, bd=4, relief=RIDGE)
        SearchHospitalInfo_frame.place(x=10, y=0, width=930, height=60)
        lb1_search = Label(SearchHospitalInfo_frame, text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=0, column=0, pady=10, sticky="w")

        searchHospitalInfo_combo = ttk.Combobox(SearchHospitalInfo_frame, textvariable=self.searchHosInfo_value,
                                         font=("times new roman", 15),
                                         state="readonly", width=15)
        searchHospitalInfo_combo['values'] = ("hosId", "hosName")
        searchHospitalInfo_combo.grid(row=0, column=1, pady=10, sticky="w")

        txt_Search = Entry(SearchHospitalInfo_frame, textvariable=self.searchHosInfo_Text, font=("times new roman", 15))
        txt_Search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        searchHosinfo_btn = Button(SearchHospitalInfo_frame,command=self.searchHospitalInfo_data, text="Search", width=20).grid(row=0, column=3,
                                                                             padx=20, pady=10)
        showHosInfo_btn = Button(SearchHospitalInfo_frame,command=self.fetchHospitalInfo_data, text="Show_all", width=20).grid(row=0, column=4,
                                                                             padx=20, pady=10)
        TableHospitalInfo_frame = Frame(HospitalInfo_frame, bd=4, relief=RIDGE)
        TableHospitalInfo_frame.place(x=10, y=70, width=930, height=450)

        scroll_x = Scrollbar(TableHospitalInfo_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(TableHospitalInfo_frame, orient=VERTICAL)
        self.Hospital_info_table = ttk.Treeview(TableHospitalInfo_frame,
                                         columns=("Hospital Id", "Name", "TotalBeds", "UnoccupiedBeds"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Deaths_table.xview())
        scroll_y.config(command=self.Deaths_table.yview())

        self.Hospital_info_table.heading("Hospital Id", text="Hospital Id")
        self.Hospital_info_table.heading("Name", text="Name")
        self.Hospital_info_table.heading("TotalBeds", text="totalBeds")
        self.Hospital_info_table.heading("UnoccupiedBeds", text="UnoccupiedBeds")
        self.Hospital_info_table["show"] = "headings"
        self.Hospital_info_table.column("Hospital Id", width=50)
        self.Hospital_info_table.column("Name", width=100)
        self.Hospital_info_table.column("TotalBeds", width=100)
        self.Hospital_info_table.column("UnoccupiedBeds", width=100)
        self.Hospital_info_table.pack(fill=BOTH, expand=1)

        self.Deaths_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchHospitalInfo_data()
        self.Hospital_info_table.pack()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        Hospitalized_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        Hospitalized_frame.place(x=0, y=0, width=1010, height=540)
        # Hospital info Fram -----------------------------------------------------------------------------------------------------------------

        SearchHospitalized_frame = Frame(Hospitalized_frame, bd=4, relief=RIDGE)
        SearchHospitalized_frame.place(x=10, y=0, width=930, height=60)
        lb1_search = Label(SearchHospitalized_frame, text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=0, column=0, pady=10, sticky="w")

        searchHospitalized_combo = ttk.Combobox(SearchHospitalized_frame, textvariable=self.Hospitalized_Value,
                                                font=("times new roman", 20),
                                                state="readonly", width=10)
        searchHospitalized_combo['values'] = ("SplId", "Name")
        searchHospitalized_combo.grid(row=0, column=1, pady=10, sticky="w")

        txt_Search = Entry(SearchHospitalized_frame, textvariable=self.Hospitalized_Text, font=("times new roman", 15))
        txt_Search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        searchHospitalized_btn = Button(SearchHospitalized_frame,command=self.searchHospitalized_data, text="Search", width=10).grid(row=0, column=3,
                                                                                    padx=10, pady=10)
        showHospitalized_btn = Button(SearchHospitalized_frame,command=self.fetchHospitalized_data ,text="Show_all", width=10).grid(row=0, column=4,
                                                                                    padx=10, pady=10)
        TableHospitalized_frame = Frame(Hospitalized_frame, bd=4, relief=RIDGE)
        TableHospitalized_frame.place(x=10, y=70, width=930, height=450)

        scroll_x = Scrollbar(TableHospitalized_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(TableHospitalized_frame, orient=VERTICAL)
        self.Hospitalized_table = ttk.Treeview(TableHospitalized_frame,
                                                columns=("Special Id", "Name", "Start Date", "End Date","Hospital Id","Hospital Name","docId","DocName"),
                                                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Deaths_table.xview())
        scroll_y.config(command=self.Deaths_table.yview())

        self.Hospitalized_table.heading("Special Id", text="Special Id")
        self.Hospitalized_table.heading("Name", text="Name")
        self.Hospitalized_table.heading("Start Date", text="Start Date")
        self.Hospitalized_table.heading("End Date", text="EndDate")
        self.Hospitalized_table.heading("Hospital Id", text="Hospital Id")
        self.Hospitalized_table.heading("Hospital Name", text="Hospital Name")
        self.Hospitalized_table.heading("docId", text="docId")
        self.Hospitalized_table.heading("DocName", text="DocName")
        self.Hospitalized_table["show"] = "headings"
        self.Hospitalized_table.column("Special Id", width=50)
        self.Hospitalized_table.column("Name", width=100)
        self.Hospitalized_table.column("Start Date", width=100)
        self.Hospitalized_table.column("End Date", width=100)
        self.Hospitalized_table.column("Hospital Id", width=100)
        self.Hospitalized_table.column("Hospital Name", width=100)
        self.Hospitalized_table.column("docId", width=100)
        self.Hospitalized_table.column("DocName", width=100)
        self.Hospitalized_table.pack(fill=BOTH, expand=1)

        self.Hospitalized_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchHospitalized_data()
        self.Hospitalized_table.pack()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        Recovered_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        Recovered_frame.place(x=0, y=0, width=1010, height=540)
        # Recovered Fram -----------------------------------------------------------------------------------------------------------------

        SearchRecovered_frame = Frame(Recovered_frame, bd=4, relief=RIDGE)
        SearchRecovered_frame.place(x=10, y=0, width=930, height=60)
        lb1_search = Label(SearchRecovered_frame, text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=0, column=0, pady=10, sticky="w")

        searchRecovered_combo = ttk.Combobox(SearchRecovered_frame, textvariable=self.Recovered_Value,
                                                font=("times new roman", 20),
                                                state="readonly", width=10)
        searchRecovered_combo['values'] = ("SplId", "Name")
        searchRecovered_combo.grid(row=0, column=1, pady=10, sticky="w")

        txt_Search = Entry(SearchRecovered_frame, textvariable=self.Recovered_Text, font=("times new roman", 15))
        txt_Search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        searchRecovered_btn = Button(SearchRecovered_frame,command=self.searchRecovered_data ,text="Search", width=10).grid(row=0, column=3,
                                                                                    padx=10, pady=10)
        showRecovered_btn = Button(SearchRecovered_frame,command=self.fetchRecovered_data, text="Show_all", width=10).grid(row=0, column=4,
                                                                                    padx=10, pady=10)
        TableRecovered_frame = Frame(Recovered_frame, bd=4, relief=RIDGE)
        TableRecovered_frame.place(x=10, y=70, width=930, height=450)

        scroll_x = Scrollbar(TableRecovered_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(TableRecovered_frame, orient=VERTICAL)
        self.Recovered_table = ttk.Treeview(TableRecovered_frame,
                                               columns=("Special Id", "Name", "Recovery Date", "Hospital Id",
                                                        "Hospital Name"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Deaths_table.xview())
        scroll_y.config(command=self.Deaths_table.yview())

        self.Recovered_table.heading("Special Id", text="Special Id")
        self.Recovered_table.heading("Name", text="Name")
        self.Recovered_table.heading("Recovery Date", text="RecoveryDate")
        self.Recovered_table.heading("Hospital Id", text="Hospital Id")
        self.Recovered_table.heading("Hospital Name", text="Hospital Name")
        self.Recovered_table["show"] = "headings"
        self.Recovered_table.column("Special Id", width=50)
        self.Recovered_table.column("Name", width=100)
        self.Recovered_table.column("Recovery Date", width=100)
        self.Recovered_table.column("Hospital Id", width=100)
        self.Recovered_table.column("Hospital Name", width=100)
        self.Recovered_table.pack(fill=BOTH, expand=1)

        self.Recovered_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchRecovered_data()
        self.Deaths_table.pack()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------

        Quarantine_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        Quarantine_frame.place(x=0, y=0, width=1010, height=540)
        # Quarantined Fram -----------------------------------------------------------------------------------------------------------------

        SearchQuarantined_frame = Frame(Quarantine_frame, bd=4, relief=RIDGE)
        SearchQuarantined_frame.place(x=10, y=0, width=930, height=60)
        lb1_search = Label(SearchQuarantined_frame, text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=0, column=0, pady=10, sticky="w")

        searchQuarantined_combo = ttk.Combobox(SearchQuarantined_frame, textvariable=self.Quarantined_Value,
                                             font=("times new roman", 20),
                                             state="readonly", width=10)
        searchQuarantined_combo['values'] = ("SplId", "Name")
        searchQuarantined_combo.grid(row=0, column=1, pady=10, sticky="w")

        txt_Search = Entry(SearchQuarantined_frame, textvariable=self.Quarantined_Text, font=("times new roman", 15))
        txt_Search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        searchQuarantined_btn = Button(SearchQuarantined_frame, command=self.searchQuarantine_data,text="Search", width=10).grid(row=0, column=3,
                                                                                 padx=10, pady=10)
        showQuarantined_btn = Button(SearchQuarantined_frame,command=self.fetchQuarantine_data, text="Show_all", width=10).grid(row=0, column=4,
                                                                                 padx=10, pady=10)
        TableQuarantined_frame = Frame(Quarantine_frame, bd=4, relief=RIDGE)
        TableQuarantined_frame.place(x=10, y=70, width=930, height=450)

        scroll_x = Scrollbar(TableQuarantined_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(TableQuarantined_frame, orient=VERTICAL)
        self.Quarantine_table = ttk.Treeview(TableQuarantined_frame,
                                            columns=("Special Id", "Name", "Start Date", "End Date",
                                                     "Place"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Deaths_table.xview())
        scroll_y.config(command=self.Deaths_table.yview())

        self.Quarantine_table.heading("Special Id", text="Special Id")
        self.Quarantine_table.heading("Name", text="Name")
        self.Quarantine_table.heading("Start Date", text="Start Date")
        self.Quarantine_table.heading("End Date", text="End Date")
        self.Quarantine_table.heading("Place", text="Place")
        self.Quarantine_table["show"] = "headings"
        self.Quarantine_table.column("Special Id", width=50)
        self.Quarantine_table.column("Name", width=100)
        self.Quarantine_table.column("Start Date", width=100)
        self.Quarantine_table.column("End Date", width=100)
        self.Quarantine_table.column("Place", width=100)
        self.Quarantine_table.pack(fill=BOTH, expand=1)

        self.Quarantine_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchQuarantine_data()
        self.Quarantine_table.pack()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------

        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        Table_frame.place(x=0, y=0, width=1010, height=540)
        TableData_frame = Frame(Table_frame, bd=4, relief=RIDGE)
        TableData_frame.place(x=10, y=70, width=930, height=450)
        Search_frame = Frame( Table_frame, bd=4, relief=RIDGE)
        Search_frame.place(x=10, y=0, width=930, height=60)
        lb1_search = Label(Search_frame, text="Search by", font=("times new roman", 20))
        lb1_search.grid(row=0, column=0, pady=10, sticky="w")

        search_combo = ttk.Combobox(Search_frame,textvariable=self.search_value, font=("times new roman", 20),
                                    state="readonly", width=10)
        search_combo['values'] = ("SplId", "Name", "CovidStatus", "Family_no")
        search_combo.grid(row=0, column=1, pady=10, sticky="w")

        txt_Search = Entry(Search_frame,textvariable=self.search_text, font=("times new roman", 15))
        txt_Search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        search_btn = Button(Search_frame, text="Search",command=self.search_data, width=10).grid(row=0, column=3,
                                                                        padx=10, pady=10)
        show_btn = Button(Search_frame,command=self.fetch_data, text="Show_all", width=10).grid(row=0, column=4,
                                                                        padx=10, pady=10)


        scroll_x = Scrollbar(TableData_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(TableData_frame, orient=VERTICAL)
        self.residents_table = ttk.Treeview(TableData_frame,
                                            columns=("Spl Id", "Name", "Covid Status", "Gender", "family no"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.residents_table.xview())
        scroll_y.config(command=self.residents_table.yview())

        self.residents_table.heading("Spl Id", text="Spl Id")
        self.residents_table.heading("Name", text="Name")
        self.residents_table.heading("Covid Status", text="Covid Status")
        self.residents_table.heading("Gender", text="Gender")
        self.residents_table.heading("family no", text="Family no")
        self.residents_table["show"] = "headings"
        self.residents_table.column("Spl Id", width=50)
        self.residents_table.column("Name", width=100)
        self.residents_table.column("Covid Status", width=100)
        self.residents_table.column("Gender", width=100)
        self.residents_table.column("family no", width=100)
        self.residents_table.pack(fill=BOTH, expand=1)

        self.residents_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        self.residents_table.pack()





    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select * from residents")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.residents_table.delete(*self.residents_table.get_children())
            for row in rows:
                self.residents_table.insert('', END, values=row)

                con.commit()
        con.close()
    def fetchDeath_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select r.Name ,r.SplId,d.DeathDate,e.hosId,e.hosName from hospitals e,residents r,deaths d where r.`SplId`=d.splId and d.hosId=e.hosId")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Deaths_table.delete(*self.Deaths_table.get_children())
            for row in rows:
                self.Deaths_table.insert('', END, values=row)

                con.commit()
        con.close()

    def fetchHospitalInfo_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select ho.hosId,ho.hosName,ho.TotalBeds,ho.TotalBeds-count(*)  from hospitals ho where ho.hosId in (select h.hosId from hospitalized h where h.hosId=ho.hosId group by(h.hosId)  having count(*)>0) group by(ho.hosId);")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Hospital_info_table.delete(*self.Hospital_info_table.get_children())
            for row in rows:
                self.Hospital_info_table.insert('', END, values=row)

                con.commit()
        con.close()
    def fetchHospitalized_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select a.SplId,a.Name,b.startDate,b.EndDate,c.hosId,c.hosName,d.docId,d.docName from doctors d,residents a,hospitalized b,hospitals c where a.`SplId`=b.splId and b.hosId=c.hosId and d.docId=b.docId ")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Hospitalized_table.delete(*self.Hospitalized_table.get_children())
            for row in rows:
                self.Hospitalized_table.insert('', END, values=row)

                con.commit()
        con.close()

    def fetchRecovered_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select a.`SplId`,a.Name,b.RecovDate,c.hosId,c.hosName from residents a,recovered b,hospitals c where a.`SplId`=b.splId and b.hosId=c.hosId")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Recovered_table.delete(*self.Recovered_table.get_children())
            for row in rows:
                self.Recovered_table.insert('', END, values=row)

                con.commit()
        con.close()
    def fetchQuarantine_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("select a.`SplId`,a.Name,b.startDate,b.endDate,b.Place from residents a,quarantined b where a.`SplId`=b.splid")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Quarantine_table.delete(*self.Quarantine_table.get_children())
            for row in rows:
                self.Quarantine_table.insert('', END, values=row)

                con.commit()
        con.close()

    def get_cursor(self, eve):
        cursor_row = self.residents_table.focus()
        content = self.residents_table.item(cursor_row)
        row = content['values']
        self.Spl_Id.set(row[0])
        self.Family_no.set(row[4])
        self.covid_status.set(row[3])
        self.gender.set(row[2])
        self.Name.set(row[1])

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()
        cur.execute("update residents set `Name`=%s,`Gender`=%s,`CovidStatus`=%s,`Family_no`=%s where `splId`=%s", (
        self.Name.get(), self.gender.get(), self.covid_status.get(), self.Family_no.get(), self.Spl_Id.get()))
        con.commit()
        self.fetch_data()
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

    def searchHospitalInfo_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()

        cur.execute("select * from hospital where `"+ str(self.searchHosInfo_value.get())+"` like '%" + str(self.searchHosInfo_Text.get()) + "%'")
        rows1 = cur.fetchall()
        if len(rows1) != 0:
            self.Hospital_info_table.delete(*self.Hospital_info_table.get_children())
            for row in rows1:
                self.Hospital_info_table.insert('', END, values=row)

                con.commit()
        con.close()
    def searchDeath_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
        cur = con.cursor()

        cur.execute("select r.Name ,r.`SplId`,d.DeathDate,e.hosId,e.hosName from hospitals e,residents r,deaths d where r.`SplId`=d.splId and d.hosId=e.hosId and r.`"+ str(self.Deaths_Value.get())+"` like '%" + str(self.Deaths_Text.get()) + "%'")
        rows1 = cur.fetchall()
        if len(rows1) != 0:
            self.Deaths_table.delete(*self.Deaths_table.get_children())
            for row in rows1:
                self.Deaths_table.insert('', END, values=row)

                con.commit()
        con.close()
    def searchRecovered_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="residents")
        cur = con.cursor()

        cur.execute("select a.`SplId`,a.Name,b.recovDate,c.hosId,c.hosName from residents a,recovered b,hospitals c where a.`SplId`=b.splId and b.hosId=c.hosId and a.`"+ str(self.Recovered_Value.get())+"` like '%" + str(self.Recovered_Text.get()) + "%'")
        rows1 = cur.fetchall()
        if len(rows1) != 0:
            self.Recovered_table.delete(*self.Recovered_table.get_children())
            for row in rows1:
                self.Recovered_table.insert('', END, values=row)

                con.commit()
        con.close()

    def searchQuarantine_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="residents")
        cur = con.cursor()

        cur.execute("select a.`SplId`,a.Name,b.startDate,b.endDate,b.Place from residents a,quarantined b where a.`SplId`=b.splId and a.`"+ str(self.Quarantined_Value.get())+"` like '%" + str(self.Quarantined_Text.get()) + "%'")
        rows1 = cur.fetchall()
        print()
        if len(rows1) != 0:
            self.Quarantine_table.delete(*self.Quarantine_table.get_children())
            for row in rows1:
                self.Quarantine_table.insert('', END, values=row)

                con.commit()
        con.close()
    def searchHospitalized_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="residents")
        cur = con.cursor()

        cur.execute("select a.`SplId`,a.Name,b.startDate,b.EndDate,c.hosId,c.hosName,d.docId,d.docName from doctors d,residents a,hospitalized b,hospitals c where a.`SplId`=b.splId and b.hosId=c.hosId and d.docId=b.docId and a.`"+ str(self.Hospitalized_Value.get())+"` like '%" + str(self.Hospitalized_Text.get()) + "%'")
        rows1 = cur.fetchall()
        if len(rows1) != 0:
            self.Hospitalized_table.delete(*self.Hospitalized_table.get_children())
            for row in rows1:
                self.Hospitalized_table.insert('', END, values=row)

                con.commit()
        con.close()



root = Tk()

ob = residents(root)
root.mainloop()
