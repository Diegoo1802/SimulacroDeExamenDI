from tkinter import *
root = Tk()


x = IntVar()

def visualizaOpcion(value):

    opcion_set = Label(root, text=value).grid(row=4)

titulo = Label(root, text="Selecciona la respuesta correcta.").grid(row=0)

opcion_1 = Radiobutton(root, text="Esta es la primera opción.", value=1, variable=x).grid(row=1)

opcion_2 = Radiobutton(root, text="Esta es la segunda opción.", value=2, variable=x).grid(row=2)

opcion_3 = Radiobutton(root, text="Esta es la tercera opción.", value=3, variable=x).grid(row=3)

boton_enviar= Button(root, text="Enviar", command=lambda: visualizaOpcion(x.get())).grid(row=5)

root.mainloop()