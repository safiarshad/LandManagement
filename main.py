from tkinter import*
from PIL import Image,ImageTk #pip install pillow
import os
from addland import Add_Land

current_directory = os.getcwd()
img1_path = os.path.join(current_directory, "LMS.png")
logo_path = os.path.join(current_directory, "LOGO.jpg")




class LandManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Land Management System")
        self.root.geometry("1550x800+0+0")#zeros indicate that x & y axis stars with 0


        #=======================BANNER================
        img1=Image.open(img1_path)
        img1=img1.resize((1200, 250))
        self.photoimg1=ImageTk.PhotoImage(img1)


        lblimg=Label(self.root, image=self.photoimg1,bd=4, relief=RIDGE)
        lblimg.place(x=320, y=0, width=1200, height=250)


        #=======================LOGO===================
        img2=Image.open(logo_path)
        img2=img2.resize((350, 250))
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root, image=self.photoimg2,bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=350, height=250)

        #================TITLE=======================
        lbl_title=Label(self.root, text="LAND MANAGEMENT SYSTEM", font=("times new roman", 40,"bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y = 250, width=1550, height=50)

        #=======================Main Frame================
        main_frame=Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y= 300, width=1550, height=620)

        #=============MENU=======
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman", 20,"bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_menu.place(x=0, y = 0, width=330)
        #=======================Options Frame================
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y= 36, width=330, height=210)

        Newland_btn=Button(btn_frame, text="Add Land",command=self.addLand_details ,width=22, font=("times new roman", 20,"bold"), bg="black", fg="gold", bd=0)
        Newland_btn.grid(row=0, column=0,pady=1)

        Search_btn = Button(btn_frame, text="Search", width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Search_btn.grid(row=1, column=0,pady=1)

        Delete_btn = Button(btn_frame, text="Delete", width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Delete_btn.grid(row=2, column=0, pady=1)


        Exit_btn = Button(btn_frame, text="Exit", width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Exit_btn.grid(row=3, column=0, pady=1)

    def addLand_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Add_Land(self.new_window)


def main():
    root=Tk()
    obj=LandManagement(root)
    root.mainloop()



if __name__ == "__main__":
    main()