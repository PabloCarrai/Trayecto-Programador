from tkinter import *

#   Evitar que cambien el tamaño de la ventana
ventana = Tk()
ventana.geometry("400x400")
#   Evito que cambie el tamaño de la ventana
# 1 false no puede modificar a lo ancho, y el 2 a lo alto
ventana.resizable(False, False)
ventana.mainloop()
