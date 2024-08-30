import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
from subprocess import call
import pyttsx3
import speech_recognition as sr
import datetime
import threading
from threading import Thread

def on_double_click(event):
    call(["python", "attendance2.py"])

    # You can replace this messagebox with any other desired action or function call
def on_double_click1(event):
    root.destroy()
    call(["python", "graph.py"])


def run(event):
    root.destroy()
    on_double_click(event)





# Create main window
root=customtkinter.CTk()
root.title("SELECTION")
root.geometry("1530x790+0+0")
root.configure(fg_color="#33186B")


frame=CTkFrame(root)
frame.place(relx=0.43,rely=0.16)


# Load image
my_image=CTkImage(light_image=Image.open("att3.jpg"),dark_image=Image.open("att3.jpg"),
                  size=(250,250))
my_image1=CTkImage(light_image=Image.open("cal2.jpg"),dark_image=Image.open("cal2.jpg"),
                  size=(250,250))
my_image2=CTkImage(light_image=Image.open("stud.jpg"),dark_image=Image.open("stud.jpg"),
                  size=(250,250))
my_image3=CTkImage(light_image=Image.open("student.jpg"),dark_image=Image.open("student.jpg"),
                  size=(250,250))
my_image4=CTkImage(light_image=Image.open("att2.jpg"),dark_image=Image.open("att2.jpg"),
                  size=(250,250))


# Create label with the image
font=CTkFont(family= "Work Sans ,sans-serif",
   size=20,
   weight= "bold",)

label = CTkLabel(root,text="",image=my_image,font=font)
label.place(relx=0.13,rely=0.16)
l = CTkLabel(root,text="ATTENDANCE")
l.place(relx=0.18,rely=0.12)
label1 = CTkLabel(root,text="",image=my_image1)
label1.place(relx=0.43,rely=0.16)
l1 = CTkLabel(root,text="CALENDAR")
l1.place(relx=0.48,rely=0.12)
label2 = CTkLabel(root,text="",image=my_image2)
label2.place(relx=0.73,rely=0.16)
l2 = CTkLabel(root,text="CHANGE")
l2.place(relx=0.80,rely=0.12)
label3 = CTkLabel(root,text="",image=my_image3)
label3.place(relx=0.28,rely=0.56)
l3 = CTkLabel(root,text="STUDENT INFO")
l3.place(relx=0.34,rely=0.52)
label4 = CTkLabel(root,text="",image=my_image4)
label4.place(relx=0.58,rely=0.56)
l4 = CTkLabel(root,text="STUFF")
l4.place(relx=0.64,rely=0.52)

# Bind double click event to the label
label.bind("<Double-Button-1>", run)
label3.bind("<Double-Button-1>", on_double_click1)
# Run the Tkinter event loop
root.mainloop()
