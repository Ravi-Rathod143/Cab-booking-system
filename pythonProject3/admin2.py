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



class admin2(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.top_frame = Frame(self, bg="#4c5154", bd=5, height=150, width=650, cursor="target")
        self.top_frame.pack(fill=BOTH)
        self.bottom_frame = Frame(self, bg="#303233", bd=5, height=400, width=650, cursor="target")
        self.bottom_frame.pack(fill=BOTH)

        self.top_image_3 = PhotoImage(file="image-3.png")
        self.top_image_label_3 = Label(self.top_frame, image=self.top_image_3, bg="#4c5154")
        self.top_image_label_3.place(x=80, y=0)

        self.mylabel = Label(self.top_frame, text="Welcome Admin !", font="Helvetica 16 bold",
                             bg="#4c5154", fg="white")
        self.mylabel.place(x=220, y=40)

        self.back_button = Button(self.top_frame, text="LOGOUT", font="arial 15 bold", relief=RAISED, bd=4, activebackground="white",
                                   activeforeground="black", cursor="arrow",command=self.ask_Q)
        self.back_button.place(x=500, y=55, width=110)

        self.title('Admin Page')
        self.resizable(False,False)
        self.geometry("650x550+300+80")
        #self.attributes("-topmost", True)
        #self.wm_iconbitmap("1LOGO.ico")
        #
        self.listbox = Listbox(self.bottom_frame, height=27,
                          width=40,
                          bg="grey",
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="yellow")
        self.listbox.grid(row=0,column=0,padx=(40,0))

        users = c.execute("select * from 'user'").fetchall()
        count = 0
        for user in users:
            self.listbox.insert(count,str(user[0]) + ". " + user[1] + "  -->  " + user[2])
            count += 1

    def ask_Q(self):
        ans = ms.askyesno('Warning!','Are you sure?',parent=self)
        print(ans)
        if ans == True:
            self.destroy()
        else:
            pass
