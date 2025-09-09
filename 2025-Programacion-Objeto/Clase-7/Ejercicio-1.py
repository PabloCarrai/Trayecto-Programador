""" 
Realizar dos botones en una ventana
uno abajo y otro arriba
el boton de arriba con color azul
el boton de abajo con color rojo

"""


#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk

ventana = Tk()
boton1 = Button(ventana, text="Boton 1", background="blue", fg="white")
boton1.pack(padx="20", pady="10")
boton2 = Button(ventana, text="Boton 2", background="red", fg="white")
boton2.pack(padx="20", pady="10")
ventana.mainloop()
