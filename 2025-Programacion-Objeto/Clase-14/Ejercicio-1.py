from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import mysql.connector


class ventana:
    def __init__(self):
        self.ventana = Tk()

        self.etiquetaNombre = Label(self.ventana, text="Nombre")
        self.etiquetaNombre.grid(column=0, row=0, padx=10, pady=10)

        self.datoEntradaNombre = StringVar()
        self.entradaNombre = Entry(self.ventana, textvariable=self.datoEntradaNombre)
        self.entradaNombre.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaTelefono = Label(self.ventana, text="Telefono")
        self.etiquetaTelefono.grid(column=0, row=1, padx=10, pady=10)

        self.datoentradaTelefono = StringVar()
        self.entradaTelefono = Entry(
            self.ventana, textvariable=self.datoentradaTelefono
        )
        self.entradaTelefono.grid(column=1, row=1, padx=10, pady=10)

        self.botonIngresar = Button(
            self.ventana, text="Ingresar", command=self.ingresar
        )
        self.botonIngresar.grid(column=1, row=2, padx=10, pady=10)

        self.ventana.mainloop()

    def ingresar(self):
        mydb = mysql.connector.connect(
            user="root",
            passwd="SomosDeCarn3",
            host="192.168.0.222",
            port=3307,
            database="ejercicio",
        )
        datos = (self.datoEntradaNombre.get(), self.datoentradaTelefono.get())

        mycursor = mydb.cursor()
        sql = "insert into usuario(nombre,telefono)values(%s,%s)"
        mycursor.execute(sql, datos)
        mydb.commit()
        ms.showinfo("Datos Ingresados", "Datos Ingresados")
        self.entradaNombre.delete(0,END)
        self.entradaTelefono.delete(0,END)


aplicacion = ventana()
