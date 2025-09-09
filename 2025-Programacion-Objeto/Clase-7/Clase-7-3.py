#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk


relleno = Tk()
texto1 = Label(relleno, text="Mira que lindo que se acerca la primavera")
texto1.pack(fill=BOTH)
boton1 = Button(relleno, text="Vamos a jugar")
boton1.pack(fill=BOTH)
boton2 = Button(relleno, text="Horizontal")
boton2.pack(pady="10", padx="5")  # le da espacio entre botones
boton3 = Button(relleno, text="Origen")
boton3.pack(pady="10", padx="5")  # le da espacio entre botones
boton4 = Button(relleno, text="relleno interno", background="yellow")
boton4.pack(ipadx="50")
boton5 = Button(relleno, text="relleno interno", background="red")
boton5.pack(ipady="50")
boton6 = Button(relleno, text="boton gigante", background="black", fg="white")
boton6.pack(ipadx="50", ipady="50")


# relleno texto
texto2 = Label(
    relleno, text="Este texto esta dentro de una caja mayor", bg="white")
texto2.config(font=("Arial", 25))
texto2.pack(ipadx="50", ipady="50")

relleno.mainloop()
