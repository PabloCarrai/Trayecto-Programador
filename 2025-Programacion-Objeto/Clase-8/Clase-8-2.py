from tkinter import *
from tkinter import ttk


# botones

ventana = Tk()
ventana.geometry("500x500")

boton1 = Button(ventana, text="Primer Boton")
boton1.pack()

botonconFondo = Button(ventana, text="Boton con fondo", background="#3de21a")
botonconFondo.pack()

botonconcolortexto = Button(
    ventana, text="Boton con color de texto", fg="#4ed1ac")
botonconcolortexto.pack()

botonFusion = Button(ventana, text="Texto fusion",
                     background="#44ac21", fg="#9f21ad")
botonFusion.pack()


ventana.mainloop()
