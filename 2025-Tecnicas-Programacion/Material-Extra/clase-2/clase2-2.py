#Se pide un programa que permita calcular la edad de la persona introduciendo el año de nacimiento y saber si tiene derecho a votar a partir de los 18 hasta 64 años, está obligado a votar. de los 0 a 15 no puede votar. Los demás edades tiene opcion a voto.

nacimiento = int(input("Introducir Año Nacimiento:"))
edad = 2025 - nacimiento
#Empezamos a evaluar si puede o no votar
if(edad>=18):
    if(edad<=64):
        print("Está obligado a votar")
    else:
        print("No puede votar")
else:
    if(edad>=0):
        if(edad<16):
            print("No puede votar ♥")
        else:
            print("Tiene opcion a votar")
    else:
        print("Tiene opcion a votar ☻")