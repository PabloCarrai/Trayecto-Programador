#Evaluar si se puede dividir por 0
# numero 1
n1 = int(input("Ingresar un número:"))
# numero 2
n2 = int(input("Ingresar un número:"))
#evaluo si el numero 2 es un 0
"""if(n2==0):
    print("No se Puede dividir por 0")
else:
    print(f"La división es: {n1/n2}")"""
#Transformar a operador ternario
#print(f"{"No se Puede dividir por 0" if(n2==0) else n1/n2}") Opcion 1

print(f"{"No se Puede dividir por 0" if(n2==0) else f"La division es: {n1/n2}"}")

