#Vectores
#declaración de vector
Colores = [] #Con los corchetes estamos estableciendo que esa variable llamada colores se reconoce o comporte como vector
#Dar valor es ingresar manualmente, cuando se declara el vector, es decir:
Colores = ["Rojo", "Amarillo",33,37,22]#Cada valor separado mediante la "," representa un espacio almacenado en el vector y arranca en el indice 0.
#Ingresar Valores en un vector
"""---------------Aclaración------------------------"""
"""Si necesito borrar previamente a alguna carga el vector lo que hago es borrarlo, para eso lo realizamos mediante un ciclo exacto EJ:"""
"""for I in Colores:
    Colores="""""
#Esa una forma
Colores.clear()#El clear vacia el contenido del vector, sin necesidad de un ciclo
#Mediante ciclo para
#Donde se establece la cantidad de valores que ingresamos dentro del vector Ej:
for I in range(0,10): #La cantidad de valores que ingreso en total son 10
    #ahora para cargar voy a pedir al usuario que ingrese un valor
    print("Ingrese un valor que desee almacenar:")
    valor=input()#almaceno lo que ingresa el usuario en una variable
    #Lo guardo en el vector mediante la función append
    Colores.append(valor)#Guardar automaticamente en el vector el valor ingresado por el usuario

#Ahora que tenemos en cuenta los distintos tipos de ingreso para un vector o carga, vamos a repasar para mostrar los valores del vector

#Una manera era manual, que esto se realizaba mediante un print de un indice del vector ej:
print(Colores[3])#Imprime el 4to valor almacenado en el array Colores.

#Otra manera mas sencilla es utilizando el ciclo for asi visualizo todos los valores que se encuentran cargados en el array
for I in Colores:
    print(I)