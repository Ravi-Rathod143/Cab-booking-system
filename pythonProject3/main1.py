from tkinter import *
from user1 import *
from admin1 import *
class Application(object):
    def __init__(self, master):
        self.mater = master

        # Frames    #157EFB
        self.top_frame = Frame(master,bg="#4c5154",bd=5,height=150,width=650,cursor="target")
        self.top_frame.pack(fill=BOTH)
        self.bottom_frame = Frame(master,bg="#303233", bd=5,height=400,width=650,cursor="target")
        self.bottom_frame.pack(fill=BOTH)

        # Label
        self.mylabel = Label(self.bottom_frame,text="Please select appropriate one",font="arial 15 bold",bg="#303233",
                             fg="white")
        self.mylabel.place(x=170,y=40)

        self.mylabel = Label(self.top_frame, text="Welcome to Cab Booking App", font="Helvetica 15 bold",
                             bg="#4c5154",fg="white")
        self.mylabel.place(x=220, y=40)


        # image
        self.top_image_1 = PhotoImage(file="image-1.png")
        self.top_image_label_1 = Label(self.bottom_frame, image=self.top_image_1, bg="#303233")
        self.top_image_label_1.place(x=170, y=130)

        self.top_image_2 = PhotoImage(file="image-2.png")
        self.top_image_label_2 = Label(self.bottom_frame, image=self.top_image_2, bg="#303233")
        self.top_image_label_2.place(x=0, y=0)

        self.top_image_3 = PhotoImage(file="image-3.png")
        self.top_image_label_3 = Label(self.top_frame, image=self.top_image_3, bg="#4c5154")
        self.top_image_label_3.place(x=80, y=0)

        # icons
        self.icon_1 = PhotoImage(file="icon-1.png")
        self.image_1 =self.icon_1.subsample(1,1)

        self.icon_2 = PhotoImage(file="icon-2.png")
        self.image_2 = self.icon_2.subsample(1, 1)

        # Buttons
        self.admin_button = Button(self.bottom_frame, text=" ADMIN",image=self.image_1,compound=LEFT, bg="#757c80",
                                   fg="white",font="arial 15 bold",relief=RAISED,bd=4,activebackground="white",
                                   activeforeground="black",cursor="arrow",command=admin1)
        self.admin_button.place(x=150,y=110,width=110)

        self.user_button = Button(self.bottom_frame, text=" USER",image=self.image_2,compound=LEFT, bg="#757c80",
                                   fg="white", font="arial 15 bold",relief=RAISED,bd=4,activebackground="white",
                                   activeforeground="black",cursor="arrow",command=user)
        self.user_button.place(x=400, y=110, width=110)

def call_user():
    myuser = user()

def admin1():
    adminpage=adminn()

def main():
    root = Tk()
    app = Application(root)
    root.title("Cab Booking")
    root.geometry("650x550+300+80")
    root.resizable(False, False)
    root.wm_iconbitmap("1LOGO.ico")
    root.mainloop()


if __name__ == '__main__':
    main()