from tkinter import *
import os
import sys
from functools import partial
from tkinter import ttk
import mysql.connector

def validateLogin(username, password):
    if username.get()=='root' and password.get()=='password':
        os.system('python LandingPage.py')
        tkWindow.destroy()

con=mysql.connector.connect(host="localhost",user="root",password="",database="residents")
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Admin Login Form')

usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0,padx=40,pady=20)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)
loginButton2 = Button(tkWindow, text="Cancel", command=tkWindow.destroy).grid(row=4, column=1)

tkWindow.mainloop()