from tkinter import *
from tkinter import ttk


# grid(mejor que pack)
ventana = Tk()
texto1 = Label(ventana, text="Primer Texto", fg="blue")
texto1.grid(row=0, column=0)
texto2 = Label(ventana, text="Texto muy pero muy extenso", bg="yellow")
texto2.grid(row=1, column=0)
texto3 = Label(ventana, text="Tercer Texto", bg="red")
texto3.grid(row=0, column=1)
boton = Button(ventana, text="", width=20).grid(row=0, column=2)
texto4 = Label(ventana, text="Gato").grid(row=0, column=2)
texto5 = Label(ventana, text="Locura").grid(row=0, columnspan=3)
ventana.mainloop()
