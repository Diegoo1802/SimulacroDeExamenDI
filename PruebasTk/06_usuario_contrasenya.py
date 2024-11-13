from tkinter import *
root = Tk()

texto = Label(root, text="Introduzca su nombre de usuario y contraseña").grid(row=0, column=0)

usuario = Entry(root, width=25)
usuario.grid(row=1, column=0)


password = Entry(root, width=25, show="*")
password.grid(row=2, column=0)

def click_boton():
    texto = Label(root, text=f"Hola {usuario.get()}, usted inició la sesión correctamente.").grid(row=1, column=0)

boton1 = Button(root, text="Enviar", bg="brown", padx=50, pady=10,
                command=click_boton).grid(row=3, column=0)


root.mainloop()