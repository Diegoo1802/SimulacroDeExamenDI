from tkinter import *
root = Tk()

#CREO UNA VENTANA DONDE EL USUARIO PUEDA ESCRIBIR, PARA POSTERIORMENTE MANDAR DICHA INFORMACION y la coloco usando row y column.
#entrada = Entry(root)
#entrada.grid(row=0, column=0)
#Personalizo el cuadro de texto del usuario, modificando parámetros como p ej. tamaño, color de fondo, tipo de letra, bordes, mensaje en el interior de la etiqueta de entrada, etc
#entrada = Entry(root, width= 75, bg="cyan", fg="firebrick", border=5, borderwidth=10)
#Para que apoarezca un mensaje explicativo dentro de la caja, uso el metodo .insert()
#entrada.insert(0, "Escriba aquí...")
#entrada.grid(row=0, column=0)

#Para escribir p ej contraseñas y que no se vean los caracteres le digo a tkinter que lo sustituya por otro caracter, simbolo, etc. con el comando show=.
entrada = Entry(root, width=100, show="'***********'")
entrada.grid(row=0, column=0)
def click_boton():
    texto = Label(root, text="Envio mandado correctamente").grid(row=1, column=0)
    #Uso el metodo f para formateo de strings y hacer que una variable sea dinamica.
    #Con el metodo .get hago que se vea y devuelva lo que la variable ha guardado.
    #OJO con las comillas para que no dé error
    texto = Label(root, text=f'Se almacenó tu envio de " {entrada.get()}"correctamente').grid(row=1, column=0)

boton1 = Button(root, text="Enviar", padx=100, pady=25,
                command=click_boton).grid(row=2, column=0)


root.mainloop()