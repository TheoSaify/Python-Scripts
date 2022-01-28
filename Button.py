import tkinter as tk
from tkinter import *
from tkinter import messagebox   
import os
import shutil

def move_ok():
    print("Piece OK")

def move_Nok():
    print("Piece NOK")
    



canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

# img = PhotoImage(file="C:\\Users\\alsaifyt\\Desktop\\PythonOpenCvScripts\\Scene.jpg")
# canvas.create_image(20,20, anchor=NW, image=img)







button = master.Button(frame, 
                   text="OK", 
                   fg="red",
                   command=move_ok)
button.pack(side=master.LEFT)


slogan = master.Button(frame,
                   text="No Ok",
                   command=move_Nok)
slogan.pack(side=master.LEFT)





mainloop()

















