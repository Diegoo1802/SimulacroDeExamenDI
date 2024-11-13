from tkinter import *
#import tkinter as tk
root = Tk()

# METODO .GRID( )
#Creo diferentes Frames o Marcos:
#Frame1:
main_frame1 = Frame()
main_frame1.grid(row=0, column=0)
main_frame1.config(width=100, height=100) 
main_frame1.config(bg="red")


#Frame2:
main_frame2 = Frame()
main_frame2.grid(row=1, column=0)
main_frame2.config(width=100, height=100)
main_frame2.config(bg="blue") 

#Frame3:
main_frame3 = Frame()
main_frame3.grid(row=1, column=1)
main_frame3.config(width=100, height=100)
main_frame3.config(bg="orange")

#Frame4:
main_frame4 = Frame()
main_frame4.grid(row=2, column=0)
main_frame4.config(width=100, height=100)
main_frame4.config(bg="green")

root.mainloop()