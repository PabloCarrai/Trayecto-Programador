def saludar():
    print("Hola Valeria Gigante")


def despedida():
    print("Chau Valeria Gigante")


class celular:
    def __init__(self):
        self.nombre = input("Ingresar el nombre del celular ")
        self.precio = float(input("Ingrese precio "))
        print(
            f"Se ha creado el celular {self.nombre} con el precio de {self.precio}")
