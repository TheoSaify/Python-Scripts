import tkinter as tk
 
fenetre = tk.Tk()
 
photo = tk.PhotoImage(file='C:\\Users\\alsaifyt\\Desktop\\PythonOpenCvScripts\\img1.png')
 
label = tk.Label(fenetre, image=photo)
label.pack()
 
fenetre.mainloop()