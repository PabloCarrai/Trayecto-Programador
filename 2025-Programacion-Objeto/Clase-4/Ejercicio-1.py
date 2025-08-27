"""  
Realizar un objeto que permita crear 10 mesas, se pide mostrar el material, 
la cantidad de patas, el precio y el tiempo de producción. 
Se pide mostrar al final el total gastado
"""


class mesa:
    material = []
    cantidadPatas = []
    precio = []
    tproduc = []

    def producirMuchasMesas(self, cantidadMesas):
        for i in range(cantidadMesas):
            material = input("Material? ")
            cantidadPatas = int(input("Patas? "))
            precio = int(input("Precio? "))
            tproduc = int(input("Tiempo"))
            self.material.append(material)
            self.cantidadPatas.append(cantidadPatas)
            self.precio.append(precio)
            self.tproduc.append(tproduc)

    def mostrarMuchasMesas(self, cantidadMesas):
        for i in range(cantidadMesas):
            print(
                f"El material de la mesa es {self.material[i]} Cantidad de Patas {self.cantidadPatas[i]} Precio {self.precio[i]} Tiempo en producir {self.tproduc[i]} {self.precio[i]*self.tproduc[i]}")


prueba = mesa()
prueba.producirMuchasMesas(2)
prueba.mostrarMuchasMesas(2)
