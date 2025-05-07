"""
Codificar un programa en python que ingrese los tres lados de un triángulo, analizar y mostrar que tipo de triángulo es: escaleno (todos los lados distintos) , equilátero (todos los lados iguales), iscóceles (dos lados iguales y uno distinto)
"""

a = input("Ingrese el primer lado del triangulo ")
b = input("Ingrese el segundo lado del triangulo ")
c = input("Ingrese el tercer lado del triangulo ")


if ((a == b) and (a == c) and (c == b)):
    print("Equilatero(todos los lados iguales)")
elif ((a != b) and (a != c) and (c != b)):
    print("Escaleno(todos los lados distintos)")
else:
    print("Isosceles(dos lados iguales uno distinto)")
