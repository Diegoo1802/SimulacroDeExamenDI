from tkinter import *
root = Tk()

etiqueta = Label(root, text="Bienvenidos a 2DAM")
etiqueta.pack()

main_frame = Frame()
main_frame.pack()
main_frame.config(width=500, height=400)
main_frame.config(bg="red")


main_frame2 = Frame()
main_frame2.pack()
main_frame2.config(width=500, height=400)
main_frame2.config(bg="yellow")

main_frame3 = Frame()
main_frame3.pack()
main_frame3.config(width=500, height=400)
main_frame3.config(bg="red")
root.mainloop()