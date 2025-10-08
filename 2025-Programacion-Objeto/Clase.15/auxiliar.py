from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms

from tkinter import font


class ventanaPrincipal:
    def __init__(self, dimension, titulo):
        self.ventana = Tk()
        self.ventana.title(titulo)
        self.ventana.geometry(dimension)
        self.ventana.configure(background="red")
        tipografia = font.Font(family="Times New Roman", size=14, weight="bold")
        texto = Label(self.ventana, text="Prueba", font=tipografia)
        
        texto.grid(column=0, row=0)

        self.ventana.mainloop()


class ventanaSecundaria:
    def __init__(self, dimension, titulo):
        self.ventana = Tk()
        self.ventana.title(titulo)
        self.ventana.geometry(dimension)
        self.ventana.mainloop()


# prueba=ventanaPrincipal("250x300","Prueba")
