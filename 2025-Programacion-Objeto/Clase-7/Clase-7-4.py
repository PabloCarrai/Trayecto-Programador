#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk


def cierre():
    ventana.destroy()


def minimiza():
    ventana.iconify()


def maximizar():
    # compruebo estado de ventana
    if (ventana.state() == 'zoomed'):
        ventana.state('normal')
    else:
        ventana.attributes('-zoomed', True)


# cerrar ventana con boton
ventana = Tk()
cerrar = Button(ventana, text="Salir", command=cierre)
cerrar.pack()
minimizar = Button(ventana, text="minimizar", command=minimiza)
minimizar.pack()

m = Button(ventana, text="maximizar", command=maximizar)
m.pack()


ventana.mainloop()
