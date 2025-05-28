"""
Codificar un programa que permita ingresar 30 colores y objetos. 
El ingreso debe ser programado en una función tanto para colores como objetos
"""


def ingresaColoresObjetos(color,objetos):
    elemento=f"{color} - {objetos} - "
    return elemento

mostrar=""

for i in range(0,3):
    color=input("Ingrese un color  ")
    objetos=input("Ingrese un objeto  ")
    mostrar=mostrar+ingresaColoresObjetos(color,objetos)+"""
"""

print("Resultado:")    
print(mostrar)