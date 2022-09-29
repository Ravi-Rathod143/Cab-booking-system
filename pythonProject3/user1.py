from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from user2 import *
from tkinter import messagebox as ms
import sqlite3

Item4 = 0

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (no INTEGER,username TEXT NOT NULL,password TEXT NOT NULL,fpassword TEXT NOT NULL,PRIMARY KEY(no AUTOINCREMENT))')
db.commit()
db.close()
#username TEXT NOT NULL ,password TEXT NOT NULL
#fpassword TEXT NOT NULL,


class user(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.title('Login Form')
        self.geometry("500x300+320+200")
        self.resizable(False, False)
        self.wm_iconbitmap("1LOGO.ico")
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.f_password = StringVar()
        self.n_username1 = StringVar()
        self.f_password1 = StringVar()
        self.n_password2 = StringVar()
        self.n_password3 = StringVar()


        # Create Widgets
        self.head = Label(self, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()

        self.logf = Frame(self, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Forgot Password? ', bd=3, font=('', 15), padx=5, pady=5, relief=FLAT, fg='Red'
               , command=self.fr).grid(row=2, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid(row=3)
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=3,column=1)



        self.logf.pack()
        self.crf = Frame(self, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Label(self.crf, text='Forgot_key: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.f_password, bd=5, show='*', font=('', 15)).grid(row=2, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=3,column=1)

        self.ff = Frame(self, padx=10, pady=10)
        Label(self.ff, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.ff, textvariable=self.n_username1, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.ff, text='Forgot_key : ', font=('', 20), pady=5, padx=5).grid(row=1)
        Entry(self.ff, textvariable=self.f_password1, bd=5, font=('', 15),show='*').grid(row=1,column=1)
        Label(self.ff, text='', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Button(self.ff, text='Verify', bd=3, font=('', 15), padx=10, pady=5, command=self.user_verification).grid(row=3,column=1)
        Button(self.ff, text='Go to login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=3, column=0)

        self.create = Frame(self, padx=10, pady=10)
        Label(self.create, text='Username: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        self.myent = Entry(self.create, text=self.n_username1, bd=5, font=('', 15))
        self.myent.grid(row=0, column=1)
        self.myent.config(state='disable')
        Label(self.create, text='New Password: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.n_password2, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Label(self.create, text='Confirm New Password: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create,textvariable=self.n_password3, bd=5, font=('', 15), show='*').grid(row=2, column=1)
        Button(self.create, text='Save', bd=3, font=('', 15), padx=20, pady=5,command=self.user_updation).grid(row=4,column=1)



        # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ? ')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome, " + self.username.get()
            self.head.configure(fg="green")
            self.head.pack(fill=X)
            mytravel = travel()
            self.destroy()

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Already Taken!')

        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password,fpassword) VALUES(?,?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get()), (self.f_password.get())])
        db.commit()


        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.ff.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
#
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def fr(self):
        self.logf.pack_forget()
        self.head['text'] = 'Verify Account'
        self.ff.pack()

    def user_verification(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and fpassword = ? ')
        c.execute(find_user, [(self.n_username1.get()), (self.f_password1.get())])
        result = c.fetchall()
        print(result)

        if result:
            self.na()
        else:
            ms.showerror('Oops!', 'Account Not Found.')

    def na(self):
        self.ff.pack_forget()
        self.head['text'] = 'Reset Password'
        self.create.pack()


    def user_updation(self):

        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        new_password = self.n_password3.get()
        username = self.n_username1.get()

        if self.n_password2.get() == self.n_password3.get():
            find_user = ("UPDATE user set password='{}' WHERE username ='{}'".format(new_password, username))
            c.execute(find_user)
            db.commit()
            ms.showinfo('Congratulation!','Successfully Completed!')
            self.create.pack_forget()
            self.log()

        else:
            ms.showerror('Oops!', "Both 'Password' and 'Confirmed Password' must be same")

