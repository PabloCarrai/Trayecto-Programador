from tkinter import *


class Aplicacion:
    def __init__(self):
        self.ventana = Tk()
        self.texto = Label(self.ventana, text="Bienvenido")
        self.texto.grid(column=0, row=1)
        self.texto1 = Label(self.ventana, text="Mauro es el mejor")
        self.texto1.grid(column=0, row=2)
        self.boton = Button(self.ventana, text="Enviar")
        self.boton.grid(column=0, row=3)
        self.ventana.mainloop()


aplicacion = Aplicacion()
