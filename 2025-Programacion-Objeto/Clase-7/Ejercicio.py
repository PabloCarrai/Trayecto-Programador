""" 
Realizar una ventana llamada "Terminator 1" que tenga 
1 texto de tipografia Verdana y tamaño 33, que diga: 
"El fin se acerca" y un botón de color negro y letras 
blancas que diga "exterminar"
"""

#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk


ventana = Tk()
ventana.title("Terminator 1")
texto = Label(ventana, text="El fin se acerca")
texto.pack()
texto.config(font=("Verdana", 21))
boton = Button(ventana, text="Exterminar", background="black", fg="white")
boton.pack()
ventana.mainloop()
