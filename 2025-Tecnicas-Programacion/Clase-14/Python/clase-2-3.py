"""
evaluar si se puede dividir por 0
"""
n1=int(input("Ingresar un numero "))
n2=int(input("Ingrese otro numero "))
#evaluo si el n2 es un 0
if(n2==0):
    print("No se puede dividir por 0")
else:
    print(f" la division es: {n1/n2}")
    
#transformar a operador ternario
print(f"No se puede dividir por 0" if(n2==0) else "La division es:",n1/n2)
