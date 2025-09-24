"""  
Realizar una interfaz grafica que permita ingresar el nombre del empleado. 
Cantidad de horas trabajadas. Sueldo básico. Pago por hora. 
Boton calcular sueldo que realize el calculo sumando el 
sueldo básico a la cantidad de horas trabajas por el precio por hora
"""

from tkinter import *


class CalculoSueldo:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Ejercicio")
        self.ventana.geometry("400x400")

        self.etiquetaNombre = Label(self.ventana, text="Nombre:")
        self.etiquetaNombre.grid(column=0, row=0, padx=10, pady=10)

        self.entradaNombre = Entry(self.ventana)
        self.entradaNombre.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaCantidadHoras = Label(self.ventana, text="Cantidad Horas")
        self.etiquetaCantidadHoras.grid(column=0, row=1, padx=10, pady=10)

        self.datoCantidadHoras = StringVar()
        self.entradaCantidadHoras = Entry(
            self.ventana, textvariable=self.datoCantidadHoras)
        self.entradaCantidadHoras.grid(column=1, row=1)

        self.etiquetaSueldoBasico = Label(self.ventana, text="Sueldo Basico")
        self.etiquetaSueldoBasico.grid(column=0, row=2, padx=10, pady=10)

        self.datoSueldoBasico = StringVar()
        self.entradaSueldoBasico = Entry(
            self.ventana, textvariable=self.datoSueldoBasico)
        self.entradaSueldoBasico.grid(column=1, row=2, padx=10, pady=10)

        self.etiquetasueldoporhora = Label(
            self.ventana, text="Sueldo por Hora")
        self.etiquetasueldoporhora.grid(column=0, row=3, padx=10, pady=10)

        self.datoentradasueldoporhora = StringVar()
        self.entradasueldoporhora = Entry(
            self.ventana, textvariable=self.datoentradasueldoporhora)
        self.entradasueldoporhora.grid(column=1, row=3, padx=10, pady=10)

        self.botonCalcular = Button(
            self.ventana, text="Calcular Monto", command=self.operacionSueldo)
        self.botonCalcular.grid(column=1, row=4, padx=10, pady=10)

        self.etiquetaResultado = Label(self.ventana, text="Cobrar")
        self.etiquetaResultado.grid(column=0, row=5, padx=10, pady=10)

        self.ventana.mainloop()

    def operacionSueldo(self):
        """   
        sumando el sueldo básico a la cantidad de horas trabajas por el precio por hora
        """
        sb = self.datoSueldoBasico.get()  # sueldo basico
        ch = self.datoCantidadHoras.get()  # cantidad horas
        ph = self.datoentradasueldoporhora.get()  # precio por hora
        resultado = (int(sb)+int(ch))*int(ph)
        self.etiquetaResultado.configure(text=f"{self.entradaNombre.get()} Debe Cobrar ${resultado}")


prueba = CalculoSueldo()
