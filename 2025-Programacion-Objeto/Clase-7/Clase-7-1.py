#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk


ventana = Tk()  # ventana
ventana.title("Pablo 2.0 ")  # titulo de ventana
ventana.geometry("400x400")  # Defino tamaño de ventana
bienvenida = ttk.Label(ventana, text="Hola vale vengo a flotar")  # texto
bienvenida.pack()  # para que aparezca
bienvenida.config(font=("Arial", 25))  # tamaño de fuente y tipografia
ventana.mainloop()  # loop del programa
