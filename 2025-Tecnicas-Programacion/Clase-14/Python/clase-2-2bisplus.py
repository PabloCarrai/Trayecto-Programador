nacimiento=int(input("Introducir año de nacimiento"))
edad=2025-nacimiento
if(edad>=18 and edad<=64):
    print("Esta obligado a votar")
elif(edad>=0 and edad<16):
    print("No puede votar")
elif(edad<0 or edad>99):
    print("No es posible")