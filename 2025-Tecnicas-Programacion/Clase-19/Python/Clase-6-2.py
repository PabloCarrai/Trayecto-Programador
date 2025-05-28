def resta():
    a=1 #   Valor local de la variable
    b=2
    resta=a-b
    return resta
a=99 #  Valor global
b=55
print(resta())
print(a)
print(b)

#   al ser global es para todo el programa
#   al ser local solo dentro de esa parte del programa