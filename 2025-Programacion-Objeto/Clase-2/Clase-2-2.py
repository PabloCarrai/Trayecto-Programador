class Persona:
    nombre = ""
    apellido = ""
    precios = []
    total = 0

    def Ingreso(self, nombre="", apellido="", precio=1):
        precio = 1
        nombre = input("Nombre? ")
        self.nombre = nombre
        apellido = input("Apellido? ")
        self.apellido = apellido
        while precio != 0:
            print("Precio? ")
            valor = int(input("Precio"))
            self.precio = precio


bandera = 0
while bandera == 0:
    ingreso = Persona()
    ingreso.Ingreso()
    bandera = int(input("Ingrese 0 para continuar 1 para salir"))


#   Hay algo que no anduvo en el clase-2-4.py del profesor mirarlo
