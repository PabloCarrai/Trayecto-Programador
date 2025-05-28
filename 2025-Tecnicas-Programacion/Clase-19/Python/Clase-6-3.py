""" 
Funciones con parametros
"""

def suma(a,b): #dentro del parentesis van las variables(Parametros)
    #   a y b son parametros de la funcion
    suma=a+b #esos parametros tienen valores que se suman en la variable suma
    return suma

print(suma(2,1)) # imprimo la funcion suma pasandole los valores 2 y 1 como valor
print(suma(44,55))
print(suma(4,5))
print(suma(434,255))

#   Aca ingreso los valores por teclado
valor1=int(input("Ingrese un valor "))
valor2=int(input("Ingrese otro valor "))
#   Aca paso esos valores como parametro en la funcion
print(suma(valor1,valor2))

