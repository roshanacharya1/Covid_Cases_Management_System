from tkinter import *
import os
import sys
from functools import partial
from tkinter import ttk
import mysql.connector

def Admin():
    os.system('python LoginPage.py')

def Doctor():
    os.system('python DoctorsLogin.py')


con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
tkWindow = Tk()
tkWindow.geometry('460x150')
tkWindow.title('Login Form')

AdminLabel = Label(tkWindow, text="Admin Panel").grid(row=0, column=0,padx=50,pady=20)
DoctorsLabel = Label(tkWindow,text="Doctors Panel").grid(row=0, column=1,padx=50,pady=20)

AdminBtn = Button(tkWindow, text="Admin Login", command=Admin).grid(row=4, column=0)
DoctorBtn = Button(tkWindow, text="Doctors Login", command=Doctor).grid(row=4, column=1)

tkWindow.mainloop()