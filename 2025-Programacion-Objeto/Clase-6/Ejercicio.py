"""
Realizar un programa para una heladeria que 
necesita generar 10 sabores de helados. 
Se pide mostrar los distintos sabores con el precio.
"""


class heladeria:
    def __init__(self):
        self.nombre = input("Nombre de la heladeria? ")
        self.sabores = []
        self.precios = []
        for i in range(10):
            sabor = input("Ingrese sabor ")
            precio = int(input("Precio? "))
            self.sabores.append(sabor)
            self.precios.append(precio)

    def resumen(self):
        gastototal = 0
        print("-"*60)
        print(f"Bienvenido a la heladeria {self.nombre}")
        print("Su eleccion en sabores son ")
        for i in range(len(self.sabores)):
            print(f"{self.sabores[i]} que vale $ {self.precios[i]}")
            gastototal = gastototal+self.precios[i]
        print("-"*60)
        print(f"Usted gasto en helados {gastototal}")
        print("-"*60)


vainilla = heladeria()
vainilla.resumen()
