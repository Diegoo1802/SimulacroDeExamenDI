from tkinter import *
root = Tk()


def click_boton():
    texto = Label(root, text="Aprita mas fuerte, gracias").grid(row=1, column=0)


notom1 = Button(root, text="Presiona coño", bg="cyan",padx=100, pady=25, command=click_boton).grid(row=0, column=0)

root.mainloop()