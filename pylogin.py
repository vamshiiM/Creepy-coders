from tkinter import messagebox

import customtkinter
from customtkinter import *
from PIL import Image,ImageTk
import mysql.connector
from subprocess import call



def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"




app=customtkinter.CTk()
app.title("LOGIN")
app.geometry("1530x790+0+0")
app.configure(fg_color="#33186B")
fr=CTkFrame(app,width=1080,height=600,fg_color="#7360DF",corner_radius=10)
fr.place(relx=0.15,rely=0.15)
fr1=CTkFrame(fr,width=450,height=540,fg_color="white",corner_radius=10)
fr1.place(relx=0.56,rely=0.05)



fetch=CTkImage(light_image=Image.open("pict.png"),dark_image=Image.open("pict.png"),
                  size=(600,500))
flabel = CTkLabel(fr,text="",image=fetch)
flabel.place(relx=0,rely=0.05)

font=CTkFont(family= "Poppins,Work Sans ,sans-serif",
   size=17,
   weight= "normal",
    )
font1=CTkFont( family= "Poppins, sans-serif",
  weight="bold",
               size=40,
 )
font2=CTkFont(family= "Poppins,Work Sans ,sans-serif",
   size=16,
   weight= "normal",
    )

# MySQL Database Connection
db = mysql.connector.connect(
      host="localhost",
        user="root",
        password="Vamshi@51124",
        database="pympr"
    )

cursor = db.cursor()

def login_action(*args):
    username = e1.get()
    password = e2.get()


    # Check if the provided username and password match any record in the database
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        # Successful login
        app.destroy()  # Close the current window
        # Open the LectureTypePage
        call(["python", "p4.py"])

    else:
        # Incorrect credentials, display an error message
        print("Invalid username or password")
        messagebox.showerror("Error", "Invalid username or password. Please try again.")


wel=CTkLabel(fr1,text="WELCOME BACK!",text_color="#33186B",font=font1)
wel.place(relx=0.05,rely=0.05)
si=CTkLabel(fr1,text="LOG IN TO YOUR ACCOUNT",text_color="gray")
si.place(relx=0.05,rely=0.13)
p2=CTkImage(light_image=Image.open("p2.png"),dark_image=Image.open("p2.png"),
                  size=(25,25))
plabel = CTkLabel(fr1,text="",image=p2)
plabel.place(relx=0.05,rely=0.3)
l1=CTkLabel(fr1,text="USERNAME:",text_color="#33186B")
l1.place(relx=0.12,rely=0.3)
e1=CTkEntry(fr1,width=400,height=40,fg_color="#F0ECE5",placeholder_text="ENTER USERNAME",text_color="#33186B",font=font2,placeholder_text_color="gray")
e1.place(relx=0.05,rely=0.37)
lo=CTkImage(light_image=Image.open("loc.png"),dark_image=Image.open("loc.png"),
                  size=(40,40))
llabel = CTkLabel(fr1,text="",image=lo)
llabel.place(relx=0.03,rely=0.45)
l2=CTkLabel(fr1,text="PASSWORD:",text_color="#33186B")
l2.place(relx=0.12,rely=0.46)
e2=CTkEntry(fr1,width=400,height=40,fg_color="#F0ECE5",placeholder_text="ENTER PASSWORD",placeholder_text_color="gray",text_color="#33186B",show="*",font=font2)
e2.place(relx=0.05,rely=0.53)
butt=CTkButton(fr1,text="LOGIN",width=400,height=50,corner_radius=10,fg_color="#33186B",font=font,command=login_action)
butt.place(relx=0.05,rely=0.7)


img=Image.open("g1.png")
butt1=CTkButton(fr1,text="GOOGLE",width=400,height=50,corner_radius=10,image=CTkImage(dark_image=img,light_image=img),fg_color="#F0ECE5",border_color="#33186B",border_width=2
                ,text_color="#33186B",font=font2)

butt1.place(relx=0.05,rely=0.8)





app.mainloop()
