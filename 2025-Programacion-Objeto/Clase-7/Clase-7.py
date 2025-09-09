#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk
# import tkFont


def Saludar():
    mostrarsaludo = ttk.Label(programa, text="Bienvenido Lautaro")
    mostrarsaludo.pack()


programa = Tk()
# establece el tamaño del contenido
espacio = ttk.Label(programa, text="Bienvenido a Python")  # salida de texto
# fuentes = tkFont.Font(family="Arial",size=22)
boton = ttk.Button(programa, text="Realizar Suma",
                   command=Saludar)  # boton

# espacio.grid()  # Prepara el espacio en la ventana
espacio.pack()  # con pack
boton.pack()  # hago que aparesca
programa.mainloop()
