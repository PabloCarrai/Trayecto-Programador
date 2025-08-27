import random


class jugador:
    nombre = ""
    forma = ""
    cantidad = 4


jugador1 = jugador()
jugador1.nombre = input("Nombre?  ")
jugador1.forma = "X"
jugador2 = jugador()
jugador2.nombre = input("Nombre?  ")
jugador2.forma = "O"

jugador1.cantidad = jugador1.cantidad-random.randint(0, 4)
print("Ronda 1")
print(f"Cantidad de X que tiene el jugador 1 es {jugador1.cantidad}")
jugador2.cantidad = jugador2.cantidad-random.randint(0, 4)
print("Ronda 2")
print(f"Cantidad de O que tiene el jugador 1 es {jugador2.cantidad}")
