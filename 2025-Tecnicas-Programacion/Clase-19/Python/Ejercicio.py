"""
Codificar un vector que permita guardar 10 animales,
y luego mostrarlos con un ciclo
"""

animales=[]
for i in range(0,10):
    animal=input("Ingrese un animal  ")
    animales.append(animal)


for i in animales:
    print(i)