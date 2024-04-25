from tkinter import*
from tkinter import Tk, ttk, Label, Entry, Frame, Button, OptionMenu, StringVar


class Add_Land:
    def __init__(self, root):
        self.root=root
        self.root.title("Land Management System")
        self.root.geometry("1195x440+330+330")


        #================TITLE=======================
        lbl_title=Label(self.root, text="Add Land Details", font=("times new roman", 22,"bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y = 0, width=1195, height=30)


        #==============Label Frame===============
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Land Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=30, width=325, height=400)

        #============Entries========
        #Land ID
        lbl_landId=Label(labelframeleft, text="Land ID:",font=("times new roman", 12), padx=2, pady=6)
        lbl_landId.grid(row=0, column=0, sticky=W)

        entry_id=ttk.Entry(labelframeleft, width=18,font=("times new roman", 12))
        entry_id.grid(row=0, column=1)
        #Owner info
        lbl_owner_name = Label(labelframeleft, text="Owner Name:", font=("times new roman", 12), padx=2, pady=6)
        lbl_owner_name.grid(row=1, column=0, sticky="w")
        entry_owner_name = Entry(labelframeleft, width=20, font=("times new roman", 12))
        entry_owner_name.grid(row=1, column=1)
        #Location
        lbl_location = Label(labelframeleft, text="Location:", font=("times new roman", 12), padx=2, pady=6)
        lbl_location.grid(row=2, column=0, sticky="w")
        # Assuming cities is a list of cities in Ghana
        """cities = ["Accra", "Kumasi", "Takoradi", "Tamale", "Cape Coast", "Ho", "Sunyani", "Bolgatanga", "Wa"]
        location_var = StringVar(value=cities[0])  # Set default value
        option_menu_location = OptionMenu(labelframeleft, location_var, *cities)
        option_menu_location.grid(row=2, column=1, sticky="ew")"""

        combo_loc=ttk.Combobox(labelframeleft,font=("times new roman", 12), width=20, state="readonly")
        combo_loc["value"]=("Accra", "Kumasi", "Takoradi", "Tamale", "Cape Coast", "Ho", "Sunyani", "Bolgatanga", "Wa")
        combo_loc.current(0)
        combo_loc.grid(row=2, column=1)
        #Land Area
        lbl_size_area = Label(labelframeleft, text="Size/Area:", font=("times new roman", 12), padx=2, pady=6)
        lbl_size_area.grid(row=3, column=0, sticky="w")
        entry_size_area = Entry(labelframeleft, width=14, font=("times new roman", 12))
        entry_size_area.grid(row=3, column=1, sticky="w")
        size_area_unit_var = StringVar(value="Acres")
        option_menu_size_area_unit = OptionMenu(labelframeleft, size_area_unit_var, "Acres", "Square meters")
        option_menu_size_area_unit.grid(row=3, column=1, sticky="e")
        #Sales Price
        lbl_sale_price = Label(labelframeleft, text="Sale Price:", font=("times new roman", 12), padx=2, pady=6)
        lbl_sale_price.grid(row=4, column=0, sticky="w")
        entry_sale_price = Entry(labelframeleft, width=20, font=("times new roman", 12))
        entry_sale_price.grid(row=4, column=1)
        #Purchase Price
        lbl_purchase_price = Label(labelframeleft, text="Purchase Price:", font=("times new roman", 12), padx=2, pady=6)
        lbl_purchase_price.grid(row=5, column=0, sticky="w")
        entry_purchase_price = Entry(labelframeleft, width=20, font=("times new roman", 12))
        entry_purchase_price.grid(row=5, column=1)
        #Usage
        lbl_usage = Label(labelframeleft, text="Usage:", font=("times new roman", 12), padx=2, pady=6)
        lbl_usage.grid(row=6, column=0, sticky="w")
        entry_usage = Entry(labelframeleft, width=20, font=("times new roman", 12))
        entry_usage.grid(row=6, column=1)

        #address
        lbl_address = Label(labelframeleft, text="Address:", font=("times new roman", 12), padx=2, pady=6)
        lbl_address.grid(row=7, column=0, sticky="w")
        entry_address = Entry(labelframeleft, width=20, font=("times new roman", 12))
        entry_address.grid(row=7, column=1)
        #Notes
        lbl_notes = Label(labelframeleft, text="Notes:", font=("times new roman", 12), padx=2, pady=6)
        lbl_notes.grid(row=8, column=0, sticky="nw")
        entry_notes = Text(labelframeleft, width=20, height=3, font=("times new roman", 12))
        entry_notes.grid(row=8, column=1, sticky="nw")


        save_button = Button(labelframeleft, text="Save Entry", font=("times new roman", 12), bg="black", fg="gold")
        save_button.grid(row=9, column=0, padx=5, pady=5)



        #============Table Frame===============
        tableframe=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Table", font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=335, y=30, width=860, height=400)

        lbl_searchby=Label(tableframe, font=("times new roman", 12, "bold"), text="Search By:", bg="Blue", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        search=ttk.Combobox(tableframe, font=("times new roman", 12, "bold"), width=24, state="readonly")
        search["values"]=("Land ID", "Owner's Name", "Location", "price") 

        search.current(0)
        search.grid(row=0, column=1, padx=2)
        text_search=ttk.Entry(tableframe, font=("times new roman", 12), width=24)
        text_search.grid(row=0, column=2, padx=2)

        search_button=Button(tableframe, text="Search", font=("times new roman", 11, "bold"), bg="black", fg="Gold", width=10)
        search_button.grid(row=0, column=3,padx=1)

        showall_button=Button(tableframe, text="Show All", font=("times new roman", 11, "bold") ,bg="black", fg="Gold", width=10)
        showall_button.grid(row=0, column=4,padx=1)

        #===========================DATA TABLE=================
        data_tableframe=LabelFrame(tableframe, bd=2, relief=RIDGE, padx=2)
        data_tableframe.place(x=0, y=50, width=860, height=325)

        scroll_xaxis=ttk.Scrollbar(data_tableframe, orient=HORIZONTAL)
        scroll_yaxis=ttk.Scrollbar(data_tableframe, orient=VERTICAL)

        self.land_details_table=ttk.Treeview(data_tableframe, column=("Land ID", "Owner's Name","Sales Price", "Purchased Price",
                                                                      "Location", "Land's Area" ), xscrollcommand=scroll_xaxis.set, yscrollcommand=scroll_yaxis.set)
        
        scroll_xaxis.pack(side=BOTTOM,fill=X)
        scroll_yaxis.pack(side=RIGHT,fill=Y)

        scroll_xaxis.config(command=self.land_details_table.xview)
        scroll_yaxis.config(command=self.land_details_table.yview)

        self.land_details_table.heading("Land ID", text="Land ID")
        self.land_details_table.heading("Owner's Name", text="Owner's Name")
        self.land_details_table.heading("Sales Price", text="Sales Price")
        self.land_details_table.heading("Purchased Price", text="Purchased Price")
        self.land_details_table.heading("Location", text="Location")
        self.land_details_table.heading("Land's Area", text="Land's Area")


        # Show the headings and pack the Treeview
        self.land_details_table['show'] = 'headings'
        self.land_details_table.pack(fill=BOTH, expand=1)



        









def main():
    root=Tk()
    obj=Add_Land(root)
    root.mainloop()




if __name__ == "__main__":
    main()