"""
Codificar un programa con al menos 4 funciones 
y que permita realizar las 4 operaciones básicas entre 3 números
"""


def suma(n, n1, n2):
    return f"La Suma entre {n} y {n1} y {n2} es {n+n1+n2} "


def resta(n, n1, n2):
    return f"La Resta entre {n} y {n1} y {n2} es {n-n1-n2} "


def multiplicacion(n, n1, n2):
    return f"La Multiplicacion entre {n} y {n1} y {n2} es {n*n1*n2} "


def division(n, n1, n2):
    if (n == 0 or n1 == 0 or n2 == 0):
        return f"no se puede dividir por 0 "
    else:
        return f"La division entre {n} y {n1} es {n/n1/n2} "


def operacion():
    n = int(input("Ingrese un numero "))
    n1 = int(input("Ingrese otro numero "))
    n2 = int(input("Ingrese otro numero "))
    print(f"{suma(n,n1,n2)}")
    print(f"{resta(n,n1,n2)}")
    print(f"{multiplicacion(n,n1,n2)}")
    print(f"{division(n,n1,n2)}")


print(operacion())
