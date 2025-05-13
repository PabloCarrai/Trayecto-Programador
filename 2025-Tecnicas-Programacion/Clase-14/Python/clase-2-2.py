# se pide un programa que permita calcular la edad de la persona introduciendo
# el año de nacimiento y saber si tiene derecho a votar a partir de los 18 hasta los 64 esta obligado a votar
# de los 0 a 15 no puede votar. Las demas edades tienen opcion a votar
nacimiento=int(input("Introducir año de nacimiento "))
edad=2025-nacimiento
#evaluamos si puede o no votar
if (edad>=18):
    if(edad<=64):
        print("Esta obligado a votar")
else:
    if(edad>=0):
        if(edad<15):
            print("No puede votar")