from tkinter import *
root = Tk()

#Las posibles variables de control de las que dispone Tkinter son:
# IntVar()
# DoubleVar()
# StringVar()
# BooleanVar()


#WIDGET RADIOBUTTON:

x = IntVar()

#Si quiero que aparezca una de las opciones marcada por defecto:
# x.set(value=1, 2 3...)

#Si quiero ver en pantalla la selección que ha hecho el ususario para posteriormente guardarlo, debo crear una funcion:

def visualizaOpcion(value):

#Dicha funcion a traves del widget label, mostrará el valor (value) obtenido mediante el metodo .get, de las funciones lambda que paso como evento, a traves del command de los Radiobutton().
#Para poder ver la opcion seleccionada por el usuario.

    opcion_set = Label(root, text=value).grid(row=4)

titulo = Label(root, text="Selecciona la respuesta correcta.").grid(row=0)

opcion_1 = Radiobutton(root, text="Esta es la primera opción.", value=1, variable=x, command=lambda: visualizaOpcion(x.get())).grid(row=1)

opcion_2 = Radiobutton(root, text="Esta es la segunda opción.", value=2, variable=x, command=lambda: visualizaOpcion(x.get())).grid(row=2)

opcion_3 = Radiobutton(root, text="Esta es la tercera opción.", value=3, variable=x, command=lambda: visualizaOpcion(x.get())).grid(row=3)


root.mainloop()