from tkinter import *
root = Tk()


main_frame = Frame()
main_frame.grid(row=0, column=0)
main_frame.config(width=100, height=100)
main_frame.config(bg="red")


main_frame2 = Frame()
main_frame2.grid(row=0, column=1)
main_frame2.config(width=100, height=100)
main_frame2.config(bg="yellow")

main_frame3 = Frame()
main_frame3.grid(row=0, column=2)
main_frame3.config(width=100, height=100)
main_frame3.config(bg="red")


main_frame4 = Frame()
main_frame4.grid(row=1, column=1)
main_frame4.config(width=100, height=100)
main_frame4.config(bg="pink")

main_frame5 = Frame()
main_frame5.grid(row=0, column=2)
main_frame5.config(width=100, height=100)
main_frame5.config(bg="red")


main_frame6 = Frame()
main_frame6.grid(row=1, column=4)
main_frame6.config(width=100, height=100)
main_frame6.config(bg="pink")


boton1 = Button(root, text="Pulsa payaso", bg="blue", padx=50, pady=5, state=DISABLED).grid(row=3, column=1)

root.mainloop()