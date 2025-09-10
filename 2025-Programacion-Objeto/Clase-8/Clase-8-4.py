from tkinter import *

#   Evitar que cambien el tamaño de la ventana
ventana = Tk()
texto1 = Label(ventana, text="Texto en nuestra aplicacion")
texto1.pack()
#   Hacer el .pack en la misma linea
texto2 = Label(ventana, text="Otro texto en pantalla").pack()


# Colocar una imagen
imagen = PhotoImage(
    file="mesi.jpeg")
Label(ventana, image=imagen).pack()

ventana.mainloop()
