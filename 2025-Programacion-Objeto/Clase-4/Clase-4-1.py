class produccion:
    mostrar = ""
    total = 0

    def __init__(self):
        cpatas = int(input("Patas? "))
        material = input("Material? ")
        precio = int(input("Precio"))
        tiempop = int(input("Tiempo Produccion? "))
        self.mostrar += f"{cpatas} {material} {precio} {tiempop}"
        self.total += precio+tiempop

    def mostrarMesa(self):
        print(self.mostrar)

    def mostrarTotal(self):
        print(self.total)


for i in range(6):
    mesa = produccion()

print(mesa.mostrarMesa)
print(mesa.mostrarTotal)
