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
main_frame3.grid(row=1, column=2)
main_frame3.config(width=100, height=100)
main_frame3.config(bg="orange")

#Frame4:
main_frame4 = Frame()
main_frame4.grid(row=2, column=0)
main_frame4.config(width=100, height=100)
main_frame4.config(bg="green")


#Frame5:
main_frame5 = Frame()
main_frame5.grid(row=2, column=1)
main_frame5.config(width=100, height=100)
main_frame5.config(bg="orange")

#Frame6:
main_frame6 = Frame()
main_frame6.grid(row=3, column=0)
main_frame6.config(width=100, height=100)
main_frame6.config(bg="green")

#CREO UN WIDGET TIPO BOTON y lo presonalizo con:
# color de fondo, padx = se expande el boton a lo ancho y pady = a lo alto, el metodo state = disabled hace que el usuario no pueda usar dicho boton. 
# mediante el metodo .grid coloco el widget boton usando row y column.
boton1 = Button(root, text="Presiona este bóton", bg="blue", padx=50, pady=5).grid(row=3, column=1)


root.mainloop()