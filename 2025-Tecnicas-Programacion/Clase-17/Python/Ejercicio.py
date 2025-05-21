"""
Codificar un programa con al menos dos funciones, 
una función va a permitir el ingreso de edad, 
y la otra función  va a comparar si la edad es entre 18 y 50 años. 
En ese caos debe mostrar "esta vivo" si no, 
debe mostrar "aun no está listo para estar vivo". 
La cantidad de edades que se van a ingresar son 15
"""


def evaluar(edad):
    """
    Evaluo la edad
    """
    if (edad > 17 and edad < 51):
        print("Esta vivo ")
    else:
        print("Aun no está listo para estar vivo ")


def ingresarEdad():
    """   
    Pido la edad y la paso a la otra funcion
    """
    edad = int(input("Ingrese su edad "))
    return evaluar(edad)


#   Aca solo repetimos la funcion unas 15 veces
for i in range(1, 15):
    ingresarEdad()
