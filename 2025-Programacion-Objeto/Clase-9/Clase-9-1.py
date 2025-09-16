from tkinter import *

#   Entrada de datos


class Aplicacion:
    def __init__(self):
        self.ventana = Tk()

        self.label = Label(self.ventana, text="Nombre")
        self.label.grid(column=0, row=0)

        #   Para ingresar datos
        self.nombre = Entry(self.ventana)
        self.nombre.grid(column=1, row=0)

        self.boton = Button(self.ventana, text="Enviar",
                            command=self.obtenernombre)
        self.boton.grid(column=0, row=1)

        self.ventana.mainloop()

    def obtenernombre(self):
        self.obteneringreso = self.nombre.get()
        print(f"El usuario ingreso {self.obteneringreso}")


aplicacion = Aplicacion()
