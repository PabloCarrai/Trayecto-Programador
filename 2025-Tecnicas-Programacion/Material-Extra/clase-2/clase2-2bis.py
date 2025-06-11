#Se pide un programa que permita calcular la edad de la persona introduciendo el año de nacimiento y saber si tiene derecho a votar a partir de los 18 hasta 64 años, está obligado a votar. de los 0 a 15 no puede votar. Los demás edades tiene opcion a voto.

nacimiento = int(input("Introducir Año Nacimiento:"))
edad = 2025 - nacimiento
#Empezamos a evaluar si puede o no votar
if(edad>=18 and edad<=64):
    print("Está obligado a votar")
else:
    if(edad>=0 and edad<16):
        print("No puede votar ♥")
    else: #podría agregarse para mejorar el programa
        if(edad<0 or edad>99):
            print("No es posible")