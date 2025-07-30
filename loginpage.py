from customtkinter import *
from PIL import Image
from tkinter import messagebox

#functionality

def login():

    if username_entry.get()=="" or password_entry=="":
        messagebox.showerror("ERROR","All fields are required")

    elif username_entry.get()=="abcd" or password_entry=="1234":
        messagebox.showinfo("SUCCESS","Login successful")
        login_window.destroy()
        import main
    
    else:
        messagebox.showerror("ERROR","Login failed")

#window
login_window=CTk()

#window customization
login_window.geometry("1000x600+320+110")
login_window.resizable(0,0)

#title
login_window.title("TeamTrack-Login")

#image
login_bg_image=CTkImage(Image.open("images/loginpage img.jpg"),size=(1000,600))
login_bg_image_label=CTkLabel(login_window,image=login_bg_image,text="")
login_bg_image_label.place(x=0,y=0)

#content

#title
title=CTkLabel(login_window,text="Employee Management System",bg_color="white",text_color="dark blue",font=("goudy old style",23,"bold"))
title.place(x=50,y=100)

#username
username_entry=CTkEntry(login_window,placeholder_text="Enter Your Username",width=180,bg_color="white")
username_entry.place(x=103,y=160)

#password
password_entry=CTkEntry(login_window,placeholder_text="Enter Your Password",width=180,bg_color="white",show="x")
password_entry.place(x=103,y=200)

#login button
login_button=CTkButton(login_window,text="Login",width=80,command=login,cursor="hand2")
login_button.place(x=147,y=255)

login_window.mainloop()