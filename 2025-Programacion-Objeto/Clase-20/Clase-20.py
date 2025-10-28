#   importamos libreria operative system
import os

with open("/home/ed/Trayecto-Programador/2025-Programacion-Objeto/Clase-20/texto.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("/home/ed/Trayecto-Programador/2025-Programacion-Objeto/Clase-20/texto.txt","w") as archivo:
    contenido = "Locura dejate de joder"
    archivo.write(contenido)

with open("/home/ed/Trayecto-Programador/2025-Programacion-Objeto/Clase-20/texto.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)


open("/home/ed/Trayecto-Programador/2025-Programacion-Objeto/Clase-20/Marina.db","x")