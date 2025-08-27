class mesa:
    operacion = 0
    total = []

    def __init__(self):
        material = input("Material? ")
        cpatas = int(input("Cantidad patas? "))
        precio = float(input("Precio? "))
        tproduc = int(input("Tiempo Produccion?  "))
        self.total.append(precio*tproduc)
        self.mostrar += f"Mesa de {material}, Cantidad de Patas {cpatas}, Precio $ {precio*tproduc}"


for i in range(1, 11):
    nuevamesa = mesa()

print(nuevamesa.mostrar)
print(nuevamesa.total)
