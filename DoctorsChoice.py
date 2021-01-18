from tkinter import *
import os
import sys
from functools import partial
from tkinter import ttk
import mysql.connector

def DoctorPanel():
        os.system('python doctor116123.py')


def Quatrantization():
    os.system('python QuarantinedInsert.py')

def Hospitalized():
        os.system('python HospitalizedInput.py')


def Deaths():
    os.system('python Deaths.py')

def recovered():
        os.system('python recoveredResidents.py')


#window
con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
tkWindow = Tk()
tkWindow.geometry('800x150')
tkWindow.title('Doctors Choioce')
DoctorsPnael_lbl = Label(tkWindow, text="Doctors Panel").grid(row=0, column=0,padx=40,pady=20)
Quarantization_label = Label(tkWindow,text="Quarantization").grid(row=0, column=1,padx=40,pady=20)
HospitalizedLabel = Label(tkWindow,text="Hospitalized").grid(row=0, column=2,padx=40,pady=20)
DeathsLabel = Label(tkWindow,text="Deaths").grid(row=0, column=3,padx=40,pady=20)
RecoveredLabel = Label(tkWindow,text="Recovered").grid(row=0, column=4,padx=40,pady=20)


Doctors_panel_btn = Button(tkWindow, text="Doctor's Panel", command=DoctorPanel).grid(row=4, column=0)
Quarantined_btn = Button(tkWindow, text="Quarantization", command=Quatrantization).grid(row=4, column=1)
Hospitalized_btn = Button(tkWindow, text="Hospitalized", command=Hospitalized).grid(row=4, column=2)
Deaths_btn = Button(tkWindow, text="Deaths", command=Deaths).grid(row=4, column=3)
Recovered_btn= Button(tkWindow, text="Recovered", command=recovered).grid(row=4, column=4)

tkWindow.mainloop()