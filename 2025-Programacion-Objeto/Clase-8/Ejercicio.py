"""  
Realizar 3 botones, uno al lado del otro con grid, 
que uno tenga el color rojo, otro el color verde y otro el color azul.  
Luego 3 textos uno abajo del otro, con los mismos colores y tambien dandole la ubicacion con grid
"""
from tkinter import *
from tkinter import ttk


ventana = Tk()
boton1 = Button(ventana, text="Primer Boton", background="red",
                fg="white").grid(row=0, column=0)
boton2 = Button(ventana, text="Primer Boton", background="green",
                fg="white").grid(row=0, column=1)
boton3 = Button(ventana, text="Primer Boton", background="blue",
                fg="white").grid(row=0, column=2)
texto1 = Label(ventana, text="Primer Texto", bg="red",
               fg="white").grid(row=1, column=0)
texto2 = Label(ventana, text="Segundo Texto", bg="green",
               fg="white").grid(row=2, column=0)
texto3 = Label(ventana, text="Tercer Texto", bg="blue",
               fg="white").grid(row=3, column=0)
ventana.mainloop()
