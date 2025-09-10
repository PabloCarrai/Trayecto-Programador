from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.geometry("600x600")
# texto con color de fondo
texto_bg = Label(ventana, text="Texto con color de fondo", bg="pink")
texto_bg.pack()
# texto con color
texto_color = Label(ventana, text="Texto colorido", fg="blue")
texto_color.pack()
#   usando hexadecimal para los colores
texto_fucion = Label(ventana, text="Texto divertido", bg="#000", fg="#fff")
texto_fucion.pack()

ventana.mainloop()
