"""
Repaso funciones
"""

#   Definimos una funcion
def suma(): #   funcion sin parametros
    #   instrucciones de la funcion
    suma=a+b # una variable que suma dos variables
    return suma # devuelve suma

a=2
b=1
suma() # llamo a la funcion suma para operar
print(suma()) # imprimo lo que devuelve la funcion suma()
a=int(input("Ingrese un valor  "))
b=int(input("Ingrese otro valor  "))
print(suma())