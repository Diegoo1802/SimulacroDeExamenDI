from tkinter import *
#import tkinter as tk
root = Tk()

etiqueta = Label(root, text="Bienvenidos a 2º DAM")
etiqueta.pack()
# .pack => Se usa para mostrar cada uno de los Widgets en la ventana.

# WIDGET FRAME(marco o contenedor).
#Creo una variable y le doy el valor de frame:
main_frame = Frame()
#Añado el marco a la ventana:
main_frame.pack()
#Personalizo el tamaño:
main_frame.config(width=500, height=400)
#Color de fondo:
main_frame.config(bg="green")
#Añado un segundo marco dentro de la misma ventana:
main_frame2 = Frame()
main_frame2.pack()
main_frame2.config(width=500, height=400)
main_frame2.config(bg="blue")


root.mainloop()