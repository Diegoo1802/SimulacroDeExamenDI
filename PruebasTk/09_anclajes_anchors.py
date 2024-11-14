from tkinter import *

root = Tk()

titulo1 = Label(root, text="NorOeste").pack(anchor=NW)
titulo2 = Label(root, text="Norte").pack(anchor=N)
titulo3 = Label(root, text="NorEste").pack(anchor=NE)
titulo4 = Label(root, text="Oeste").pack(anchor=W)
titulo5 = Label(root, text="Centro").pack(anchor=CENTER)
titulo6 = Label(root, text="Este").pack(anchor=E)
titulo7 = Label(root, text="SurOeste").pack(anchor=SW)
titulo8 = Label(root, text="Sur").pack(anchor=S)
titulo9 = Label(root, text="SurEste").pack(anchor=SE)

# Izquierdas
boton1_izq = Button(root, text="Botón Izq 1").pack(anchor=W)
boton2_izq = Button(root, text="Botón Izq 2").pack(anchor=W)
boton3_izq = Button(root, text="Botón Izq 3").pack(anchor=W)

# Derechos
boton1_der = Button(root, text="Botón Der 1").pack(anchor=E)
boton2_der = Button(root, text="Botón Der 2").pack(anchor=E)
boton3_der = Button(root, text="Botón Der 3").pack(anchor=E)

# Centro
boton1_centro = Button(root, text="Botón Centro 1").pack(anchor=CENTER)
boton2_centro = Button(root, text="Botón Centro 2").pack(anchor=CENTER)
boton3_centro = Button(root, text="Botón Centro 3").pack(anchor=CENTER)
boton4_centro = Button(root, text="Botón Centro 4").pack(anchor=CENTER)
boton5_centro = Button(root, text="Botón Centro 5").pack(anchor=CENTER)
boton6_centro = Button(root, text="Botón Centro 6").pack(anchor=CENTER)

root.mainloop()