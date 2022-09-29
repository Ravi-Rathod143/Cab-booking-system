from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from user2 import *
from tkinter import messagebox as ms
import sqlite3
from admin2 import *

Item4 = 0

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

class adminn(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.title('Admin Page')
        self.geometry("500x300+320+200")
        self.wm_iconbitmap("1LOGO.ico")
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()


        # Create Widgets
        self.head = Label(self, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()

        self.logf = Frame(self, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid(column=1)

        self.logf.pack()

    def login(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        p=self.password.get()
        try:

            if result[0][2] == p and result[0][1] =='admin':

                self.logf.pack_forget()
                self.head['text'] = "Welcome, " + self.username.get()
                self.head.configure(fg="green")
                self.head.pack(fill=X)
                adminpage2 = admin2()
                self.destroy()

            else:
                ms.showerror('Oops!', 'Username Not Found.')
        except Exception as e:
            ms.showerror('Oops!', 'Username Not Found.')


        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

