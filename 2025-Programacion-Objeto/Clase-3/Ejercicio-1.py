""" 
Realizar un objeto que permita ingresar 30 paises 
que participan del mundial, se pide mostrar nombre, 
bandera, puntos, grupo y posicion de cada uno
"""


class copa():
    mostrar = []

    def __init__(self):
        bandera = input("Bandera:  ")
        nombre = input("Nombre:  ")
        grupo = input("Grupo:  ")
        self.mostrar.append(
            f"Bandera: {bandera} Nombre: {nombre}  Grupo: {grupo}")


for i in range(3):
    crearpais = copa()

for i in range(3):
    print(crearpais.mostrar[i])
