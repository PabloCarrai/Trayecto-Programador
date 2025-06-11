"""
Codificar un programa en python un vector que Tenga 10 edades cargadas de personas. Se pide modificar las 10 edades y mostrar las modificadas.
"""


edades=[4,10,13,45,6,77,88,9,43,21]
for x in range(len(edades)):
    print(f"Indice {x} edad cargada {edades[x]}")

print("Modificamos la lista y cargamos las nuevas edades")
for x in range(len(edades)):
    nuevovalor=int(input("Ingrese nuevo valor  "))
    edades[x]=nuevovalor

print("Mostramos como queda ahora la lista  ")
for x in range(len(edades)):
    print(f"Indice {x} nueva edad cargada {edades[x]}")

