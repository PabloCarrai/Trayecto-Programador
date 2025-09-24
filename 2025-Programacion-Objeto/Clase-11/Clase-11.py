""" Login"""

from tkinter import *


class Aplicacion:
    def __init__(self):
        self.ventana = Tk()

        self.texto = Label(self.ventana, text="Nombre")
        self.texto.grid(column=0, row=0)

        self.datosnombre = StringVar()
        self.entradanombre = Entry(self.ventana, textvariable=self.datosnombre)
        self.entradanombre.grid(column=1, row=0)

        self.textoclave = Label(self.ventana, text="Clave")
        self.textoclave.grid(column=0, row=1)

        self.datoclave = StringVar()
        self.entradaclave = Entry(self.ventana, textvariable=self.datoclave)
        self.entradaclave.grid(column=1, row=1)

        self.botonRegistrar = Button(
            self.ventana, text="Registrarse", command=self.registrar)
        self.botonRegistrar.grid(column=0, row=2)

        self.botonlogin = Button(
            self.ventana, text="Login", command=self.login)
        self.botonlogin.grid(column=1, row=2)

        self.ventana.mainloop()

    def registrar(self):
        print(self.datoclave.get(), self.datosnombre.get())

    def login(self):
        print(self.datoclave.get(), self.datosnombre.get())


aplicacion = Aplicacion()
