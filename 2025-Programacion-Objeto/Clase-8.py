from tkinter import *
from tkinter import ttk


def Saludar():
    # funcion usada por el boton al presionarse
    # generamos un label en la ventana con el texto
    hola = Label(ventana, text="Bienvenido a Mauro 2.1")
    hola.pack()

    # creamos la ventana
ventana = Tk()
# modificar los ajuste de la ventana
ventana.geometry("400x400")  # seteamos el tamaño

#   textos
texto = Label(ventana, text="El texto que contiene")
#   incorporamos el texto en la ventana
texto.pack()
# boton
boton = Button(ventana, text="Boton ejemplo")
# lo ubicamos en algun lado
boton.pack()
#   programamos una accion para el boton
bienvenido = Button(ventana, text="Haz clic para saludar", command=Saludar)
bienvenido.pack()
# mantenemos el loop principal
ventana.mainloop()
