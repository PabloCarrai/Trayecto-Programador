""" 
Realizar un login que permita ingresar el nombre, 
el mail y la contraseña para cada usuario. 
Luego mostrar los datos ingresados por pantalla
"""


from tkinter import *


class Acceso:

    def __init__(self):
        self.ventana = Tk()

        self.ventana.geometry("250x250")

        self.ventana.title("Bienvenido al sistema de Acceso. ")

        self.etiquetaNombre = Label(self.ventana, text="Nombre:")
        self.etiquetaNombre.grid(column=0, row=0)

        self.entradaNombre = Entry(self.ventana)
        self.entradaNombre.grid(column=1, row=0)

        self.etiquetaMail = Label(self.ventana, text="Correo:")
        self.etiquetaMail.grid(column=0, row=2)

        self.entradaMail = Entry(self.ventana)
        self.entradaMail.grid(column=1, row=2)

        self.etiquetaClave = Label(self.ventana, text="Clave:")
        self.etiquetaClave.grid(column=0, row=3)

        self.entradaClave = Entry(self.ventana, show="*")
        self.entradaClave.grid(column=1, row=3)

        self.botonMostrarDatos = Button(
            self.ventana, text="Detalle", command=self.mostrarResumen)
        self.botonMostrarDatos.grid(column=0, row=4)

        self.etiquetaResumen = Label(self.ventana, text="resultado")
        self.etiquetaResumen.grid(column=0, row=6)

        self.ventana.mainloop()

    def mostrarResumen(self):
        mostrar = f"Nombre: {self.entradaNombre.get()}\nCorreo:{self.entradaMail.get()}\nClave:{self.entradaClave.get()}"
        self.etiquetaResumen.configure(text=mostrar)


acceso = Acceso()
