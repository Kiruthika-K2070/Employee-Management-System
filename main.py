from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

# clearing data from entry fields

def clear(value=False):

    if value:
        tree.selection_remove(tree.focus())

    id_entry.delete(0,END)
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    role_entry.set("")
    gender_entry.set("")
    salary_entry.delete(0,END)

#showing data in treeview

def treeview_display():

    data=database.fetch_details()
    tree.delete(*tree.get_children())
    for i in data:
        tree.insert("",END,values=i)

def selection(data):

    selected_data=tree.selection()
    
    if selected_data:
        clear()
        row=tree.item(selected_data)["values"]
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        phone_entry.insert(0,row[2])
        role_entry.set(row[3])
        gender_entry.set(row[4])
        salary_entry.insert(0,row[5])

#functionality

def add_employee():

    if id_entry.get()=="" or name_entry.get()=="" or phone_entry.get()=="" or role_entry.get()=="" or gender_entry.get()=="" or salary_entry.get()=="":
        messagebox.showerror("ERROR","All fields are required")

    elif not id_entry.get().startswith("EMP"):
        messagebox.showerror("ERROR","ID should start with EMP followed by a number")

    elif database.id_exists(id_entry.get()):
        messagebox.showerror("ERROR","ID already exists !")

    else:
        database.insert(id_entry.get(),name_entry.get(),phone_entry.get(),role_entry.get(),gender_entry.get(),salary_entry.get())
        treeview_display()
        clear()
        messagebox.showinfo("SUCCESS","Data is added")
        
def update_employee():
    
    select_data=tree.selection()

    if not select_data:
        messagebox.showerror("ERROR","Data is not selected")

    else:
        database.update(id_entry.get(),name_entry.get(),phone_entry.get(),role_entry.get(),gender_entry.get(),salary_entry.get())
        clear()
        treeview_display()
        messagebox.showinfo("SUCCESS","Data is updated")

def delete_employee():

    selected_data=tree.selection()

    if not selected_data:
        messagebox.showerror("ERROR","Select employee to delete")
    
    else:
        database.delete(id_entry.get())
        clear()
        treeview_display()
        messagebox.showinfo("SUCCESS","Data is deleted")


def delete_all():

    result=messagebox.askyesno("ERROR","Do you really want to delete all the records ?")
    
    if result:
        database.delete_all()
        treeview_display()
    
    else:
        pass


def search():

    if search_by.get()=="":
        messagebox.showerror("ERROR","Select option to search")
    
    elif search_by_entry.get()=="":
         messagebox.showerror("ERROR","Select value to search")

    else:
        data=database.search_emp(search_by.get(),search_by_entry.get())
        tree.delete(*tree.get_children())
        for i in data:
            tree.insert("",END,values=i)
        
def show_all():

    treeview_display()
    search_by.set("Search By")
    search_by_entry.delete(0,END)

#window
ems_window=CTk()

#window customization
ems_window.geometry("1000x600+320+110")
ems_window.resizable(False,False)
ems_window.configure(fg_color="black")

#title
ems_window.title("TeamTrack")

#image
ems_bg_image=CTkImage(Image.open("images/main img.jpg"),size=(1000,150))
ems_bg_image_label=CTkLabel(ems_window,image=ems_bg_image,text="")
ems_bg_image_label.grid(row=0,column=0,columnspan=2)

#frames

#left frame
left_frame=CTkFrame(ems_window,fg_color="black")
left_frame.grid(row=1,column=0)

#left frame - contents

#id entry
id=CTkLabel(left_frame,text="ID",font=("arial",18,"bold"),text_color="white")
id.grid(row=0,column=0,padx=10,pady=17,sticky="w")
id_entry=CTkEntry(left_frame,font=("arial",15),width=175)
id_entry.grid(row=0,column=1)

#name entry
name=CTkLabel(left_frame,text="Name",font=("arial",18,"bold"),text_color="white")
name.grid(row=1,column=0,padx=10,pady=17,sticky="w")
name_entry=CTkEntry(left_frame,font=("arial",15),width=175)
name_entry.grid(row=1,column=1)

#phone entry
phone=CTkLabel(left_frame,text="Phone",font=("arial",18,"bold"),text_color="white")
phone.grid(row=2,column=0,padx=10,pady=17,sticky="w")
phone_entry=CTkEntry(left_frame,font=("arial",15),width=175)
phone_entry.grid(row=2,column=1)

#role entry
role=CTkLabel(left_frame,text="Role",font=("arial",18,"bold"),text_color="white")
role.grid(row=3,column=0,padx=10,pady=17,sticky="w")
role_options=["Web Developer","Cloud Architect","Technical Writer","Network Engineer","DevOps Engineer","Data Scientist","Business Analyst","IT Consultant","UI/UX Designer"]
role_entry=CTkComboBox(left_frame,values=role_options,font=("arial",15),width=175,state="readonly")
role_entry.grid(row=3,column=1)

#gender entry
gender=CTkLabel(left_frame,text="Gender",font=("arial",18,"bold"),text_color="white")
gender.grid(row=4,column=0,padx=10,pady=17,sticky="w")
gender_options=["Male","Female"]
gender_entry=CTkComboBox(left_frame,values=gender_options,font=("arial",15),width=175,state="readonly")
gender_entry.grid(row=4,column=1)

#salary entry
salary=CTkLabel(left_frame,text="Salary",font=("arial",18,"bold"),text_color="white")
salary.grid(row=5,column=0,padx=10,pady=17,sticky="w")
salary_entry=CTkEntry(left_frame,font=("arial",15),width=175)
salary_entry.grid(row=5,column=1)

#right frame
right_frame=CTkFrame(ems_window)
right_frame.grid(row=1,column=1)

#right frame - contents

#search by
search_by_options=["ID","Name","Phone","Role","Gender","Salary"]
search_by=CTkComboBox(right_frame,values=search_by_options,state="readonly",width=200)
search_by.grid(row=0,column=0,pady=5,padx=5)
search_by.set("Search By")

#search by entry
search_by_entry=CTkEntry(right_frame,width=180)
search_by_entry.grid(row=0,column=1,pady=5,padx=5)

#search button
search_button=CTkButton(right_frame,text="Search",command=search)
search_button.grid(row=0,column=2,pady=5,padx=5)

#show all button
show_all_button=CTkButton(right_frame,text="Show All",command=show_all)
show_all_button.grid(row=0,column=3,columnspan=2,pady=5,padx=5)

#treeview
tree=ttk.Treeview(right_frame,height=14)
tree.grid(row=1,column=0,columnspan=4)

#columns
tree["columns"]=("id","name","phone","role","gender","salary")

#column name cutomization
tree.heading("id",text="ID")
tree.heading("name",text="Name")
tree.heading("phone",text="Phone")
tree.heading("role",text="Role")
tree.heading("gender",text="Gender")
tree.heading("salary",text="Salary")

tree.config(show="headings")

#treeview style
style=ttk.Style()
style.configure("Treeview.Heading",font=("arial",14,"bold"),anchor=CENTER)
style.configure("Treeview",font=("arial",15),rowheight=27,background="black",foreground="white")

#treeview column customization
tree.column("id",width=100)
tree.column("name",width=165)
tree.column("phone",width=160)
tree.column("role",width=185)
tree.column("gender",width=110)
tree.column("salary",width=140)

#scroll bar
scroll_bar=ttk.Scrollbar(right_frame,orient=VERTICAL,command=tree.yview)
scroll_bar.grid(row=1,column=4,sticky="ns")

tree.config(yscrollcommand=scroll_bar.set)

#button frame
button_frame=CTkFrame(ems_window,fg_color="black")
button_frame.grid(row=2,column=0,columnspan=2,pady=10)

#button frame - contents

#new employee 
new_employee=CTkButton(button_frame,text="New Employee",font=("arial",15,"bold"),width=173,corner_radius=15,command=lambda: clear(True))
new_employee.grid(row=2,column=0,padx=10,pady=8)

#add employee
add_employee=CTkButton(button_frame,text="Add Employee",font=("arial",15,"bold"),width=173,corner_radius=15,command=add_employee)
add_employee.grid(row=2,column=1,padx=10,pady=8)

#update employee
update_employee=CTkButton(button_frame,text="Update Employee",font=("arial",15,"bold"),width=173,corner_radius=15,command=update_employee)
update_employee.grid(row=2,column=2,padx=10,pady=8)

#delete employee
delete_employee=CTkButton(button_frame,text="Delete Employee",font=("arial",15,"bold"),width=173,corner_radius=15,command=delete_employee)
delete_employee.grid(row=2,column=3,padx=10,pady=8)

#delete all employee
delete_all_employee=CTkButton(button_frame,text="Delete All",font=("arial",15,"bold"),width=173,corner_radius=15,command=delete_all)
delete_all_employee.grid(row=2,column=4,padx=10,pady=8)

treeview_display()
ems_window.bind("<ButtonRelease>",selection)

ems_window.mainloop()