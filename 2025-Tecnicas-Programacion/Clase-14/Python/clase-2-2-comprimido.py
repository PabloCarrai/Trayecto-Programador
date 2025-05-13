nacimiento=int(input("Introducir año de nacimiento"))
edad=2025-nacimiento

print(f"Esta obligado a votar " if(edad>=18 and edad<=64) else "No puede votar " if(edad>=0 and edad<16) else "No es posible" if(edad<0 or edad>99) else "No hago nada")