#   Importo los modulos necesario
from tkinter import *  # Importo tkinter
from tkinter import ttk  # Importo ttk


packman = Tk()
boton = ttk.Button(packman, text="Haz clic")
# boton.pack(fill=BOTH)   #ocupa todo el espacio. Se hace grande.
# boton.pack(expand=True) #se va al medio
boton.pack(expand=True)  # se va Arriba
registrar = Button(packman, text="Registrate", background="blue", fg="white")
registrar.pack(side=LEFT)  # Ubico a la izquierda al centro y izquierda
contacto = ttk.Button(packman, text="Contactate")
# contacto.pack(side=LEFT)
# contacto.pack(side=RIGHT)
arriba = Label(packman, text="Comienza la caceria")
arriba.pack(side=TOP)
abajo = Label(packman, text="Abajo")
abajo.pack(side=BOTTOM)
packman.mainloop()
