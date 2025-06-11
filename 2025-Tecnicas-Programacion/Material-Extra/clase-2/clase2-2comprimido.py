nacimiento = int(input("Introducir Año Nacimiento:"))
edad = 2025 - nacimiento
#Empezamos a evaluar si puede o no votar
"""if(edad>=18 and edad<=64):
    print("Está obligado a votar")
elif(edad>=0 and edad<16):
    print("No puede votar ♥")#ojo en el ultimo condicional
elif(edad<0 or edad>99):
    print("No es posible")"""

"""
if(edad>=18 and edad<=64):
    print("Está obligado a votar")
elif(edad>=0 and edad<16):
    print("No puede votar ♥")#ojo en el ultimo condicional
elif(edad<0 or edad>99):
    print("No es posible")"""
"""
"Esta obligado a votar" if(edad>=18 and edad<=64) else "no hago nada"

"No puede votar ♥" if(edad>=0 and edad<16) else "no haga nada"

"No es posible" if(edad<0 or edad>99) else "no hago nada"
"""

#"Esta obligado a votar" if(edad>=18 and edad<=64) else "No puede votar ♥" if(edad>=0 and edad<16) else "No es posible" if(edad<0 or edad>99) else "no hago nada"
#"Esta obligado a votar" if(edad>=18 and edad<=64) else "No puede votar ♥" if(edad>=0 and edad<16) else "No es posible" if(edad<0 or edad>99) else "no hago nada" Resultado final

print(f"{"Esta obligado a votar" if(edad>=18 and edad<=64) else "No puede votar ♥" if(edad>=0 and edad<16) else "No es posible" if(edad<0 or edad>99) else "opcion a votar"}")