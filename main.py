from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
import os   #pip install os
import sys #pip install sys
import importlib
from tkinter import messagebox
from login import LoginApp
import tkinter as tk

current_directory = os.getcwd()
img1_path = os.path.join(current_directory, "LMS.png")
logo_path = os.path.join(current_directory, "LOGO.jpg")
icon_path = os.path.join(current_directory, "ICON.png")

class LandManagement:
    def __init__(self, root, admin=False):
        self.root = root
        self.root.title("Land Management System")
        self.root.geometry("1550x800+0+0")  # zeros indicate that x & y axis stars with 0
        self.root.iconphoto(False, PhotoImage(file=icon_path))

        self.admin = admin
        self.add_land_class = None  # Initialize the add_land_class variable

        if self.admin:
            # Initialize admin-specific features
            self.init_admin_features()
        else:
            # Initialize user-specific features
            self.init_user_features()

        # =======================BANNER================
        img1 = Image.open(img1_path)
        img1 = img1.resize((1200, 250))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=320, y=0, width=1200, height=250)

        # =======================LOGO===================
        img2 = Image.open(logo_path)
        img2 = img2.resize((350, 250))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=350, height=250)

        # ======================TITLE=======================
        lbl_title = Label(self.root, text="LAND MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y=250, width=1550, height=50)

        # =======================Main Frame================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=300, width=1550, height=620)

        # =============MENU=======
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=330)

        # =======================Options Frame================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=36, width=330, height=210)

        Newland_btn = Button(btn_frame, text="Manage Lands", command=self.addLand_details, width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Newland_btn.grid(row=0, column=0, pady=1)

        Logout_btn = Button(btn_frame, text="Logout", command=self.logout, width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Logout_btn.grid(row=1, column=0, pady=1)

        Delete_btn = Button(btn_frame, text="...", width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Delete_btn.grid(row=2, column=0, pady=1)

        Exit_btn = Button(btn_frame, text="Exit", width=22, command=self.stop_application, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0)
        Exit_btn.grid(row=3, column=0, pady=1)

    def init_admin_features(self):
        Add_land = self.dynamic_import("admin_file.Add_Land")
        if Add_land:
            self.add_land_class = Add_land
        else:
            print("Admin features could not be initialized.")

    def init_user_features(self):
        Add_land = self.dynamic_import("user_file.Add_Land")
        if Add_land:
            self.add_land_class = Add_land
        else:
            print("User features could not be initialized.")

    def dynamic_import(self, module_name):
        try:
            module_path, class_name = module_name.rsplit('.', 1)
            module = importlib.import_module(module_path)
            return getattr(module, class_name)
        except ImportError as e:
            print(f"Error: Module '{module_path}' not found. {e}")
            return None
        except AttributeError as e:
            print(f"Error: Module '{module_path}' does not contain a class named '{class_name}'. {e}")
            return None

    def addLand_details(self):
        if self.add_land_class:
            self.new_window = Toplevel(self.root)
            self.app = self.add_land_class(self.new_window)
        else:
            print("Error: Add_land class is not initialized.")

    def stop_application(self):
        self.root.quit()

    def logout(self):
        self.root.destroy()
        os.execv(sys.executable, ['python'] + sys.argv)


def main():
    root = Tk()

    # Create an instance of LoginApp
    login_app = LoginApp(root)

    # Run the login window and wait until it is closed
    root.mainloop()

    # If login is successful, create the main application window
    if login_app.login_successful:
        root = Tk()  # Create a new root window for the main application

        if login_app.is_admin:
            # Perform actions for admin user
            obj = LandManagement(root, admin=True)
        else:
            # Perform actions for normal user
            obj = LandManagement(root, admin=False)

        root.mainloop()


if __name__ == "__main__":
    main()

