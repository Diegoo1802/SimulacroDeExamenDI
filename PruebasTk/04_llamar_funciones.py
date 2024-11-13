from tkinter import *
root = Tk()


def click_boton():
    texto = Label(root, text="Presiona un poco más fuerte y de manera continuada").grid(row=1, column=0)


boton1 = Button(root, text="Presiona este botón para poder hacer una función",  bg="cyan", padx=100, pady=25,
                command=click_boton).grid(row=0, column=0) #Si uso parentesis despues de la funcion click_boton(), hago que no tenga funcionalidad.
#Si quiero que la funcion tenga funcionalidad, debo quitar los parentesis.


root.mainloop()