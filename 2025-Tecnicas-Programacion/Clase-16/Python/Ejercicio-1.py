"""
Codificar un programa que permita ingresar 3 números, 
mostrar si los números son pares. 
Mostrar un cartel de bienvenida cada vez que ingresa 
un número y permitir que ingrese el nombre y contraseña de usuario
"""


def saludar():
    return "Bienvenido"
    
def numeroPar():
    numero=int(input("Ingrese un numero   "))
    if(numero%2==0):
        return f"El numero {numero} es par  "
    else:
        return f"El numero {numero} no es par  "
        
def persona():
    input("Ingrese su nombre  ")
    input("Ingrese su clave  ")
    
print(saludar())
for i in range(3):
    print(numeroPar())
persona()