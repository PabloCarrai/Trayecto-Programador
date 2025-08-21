"""
Realizar un objeto con constructor que permita introducir 5 personas 
y mostrar la cantidad total de hombres. Deben ingresar nombre, apellido, sexo y edad
"""


class Persona:
    nombres = []
    apellidos = []
    sexos = []
    edades = []
    cPCargar = 5

    def __init__(self):
        for i in range(self.cPCargar):
            #   Pido los datos
            self.nombre = input("Nombre? ")
            self.apellido = input("Apellido? ")
            self.sexo = input("Sexo? ")
            self.edad = int(input("Edad? "))
            #   Cargo los mismos en las listas
            self.nombres.append(self.nombre)
            self.apellidos.append(self.apellido)
            self.sexos.append(self.sexo)
            self.edades.append(self.edad)

    def MostrarPersonas(self):
        for i in range(self.cPCargar):
            print(
                f"Nombre: {self.nombres[i]} Apellido:{self.apellidos[i]} Sexo:{self.sexos[i]} Edades:{self.edades[i]}")


pirulo = Persona()
pirulo.MostrarPersonas()
