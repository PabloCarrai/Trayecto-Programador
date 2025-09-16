""" 
Realizar una calculadora que permita realizar las operaciones 
básicas(suma,resta,ivision,multiplicacion) mediante dos numeros 
y muestre el resultado por interfaz grafica
"""

from tkinter import *


class Calculadora:
    def __init__(self):
        self.ventana = Tk()

        self.etiquetaNumero = Label(self.ventana, text="Numero 1:")
        self.etiquetaNumero.grid(column=0, row=0)

        self.entradaNumero = Entry(self.ventana)
        self.entradaNumero.grid(column=1, row=0)

        self.etiquetaNumero1 = Label(self.ventana, text="Numero 2:")
        self.etiquetaNumero1.grid(column=0, row=1)

        self.entradaNumero1 = Entry(self.ventana)
        self.entradaNumero1.grid(column=1, row=1)

        self.botonSumar = Button(
            self.ventana, text="Sumar", command=self.sumar)
        self.botonSumar.grid(column=0, row=3)

        self.botonRestar = Button(
            self.ventana, text="Restar", command=self.restar)
        self.botonRestar.grid(column=1, row=3)

        self.botonDividir = Button(
            self.ventana, text="Dividir", command=self.dividir)
        self.botonDividir.grid(column=0, row=4)

        self.botonMultiplicar = Button(
            self.ventana, text="Multiplicar", command=self.multiplicar)
        self.botonMultiplicar.grid(column=1, row=4)

        self.etiquetaResultado = Label(self.ventana, text="Resultado")
        self.etiquetaResultado.grid(column=0, row=5)

        self.ventana.mainloop()

    def sumar(self):
        suma = int(self.entradaNumero.get())+int(self.entradaNumero1.get())
        self.etiquetaResultado.configure(text=suma)

    def restar(self):
        resta = int(self.entradaNumero.get())-int(self.entradaNumero1.get())
        self.etiquetaResultado.configure(text=resta)

    def dividir(self):
        dividir = int(self.entradaNumero.get())/int(self.entradaNumero1.get())
        self.etiquetaResultado.configure(text=dividir)

    def multiplicar(self):
        multiplicar = int(self.entradaNumero.get()) * \
            int(self.entradaNumero1.get())
        self.etiquetaResultado.configure(text=multiplicar)


aplicacion = Calculadora()
