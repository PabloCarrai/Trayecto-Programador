#Repaso de arrays, porque ya hicimos varios repasos de funciones.
#Qué era un array?
#una variable que contiene varios datos y tipos de datos distintos
#Ej:
colores = ["rojo","azul",212331,"#3casef",3]
#Como muestro los distintos valores almacenados dentro del array
print(colores[0])
#Mostrar todos los elementos almacenados dentro del array
for I in colores:
    print(I)
    #En este caso la variable I va a inicializar de manera automática en 0, por eso va a permitir mostrar todos los valores y datos almacenados en el array porque en cada vuelta va ir sumando de a uno, hasta que no haya datos para mostrar que se encuentren almacenados en el array.
#Con el while se puede? SI
#Necesito saber la cantidad de elementos que tengo dentro de mi array, con la funcion len() que va a establecer la cantidad de valores almacenados dentro.
I=0
while(I<len(colores)):
    #Luego para mostrarlo, no alcanza con solo poner o mostrar la variable I, porque en este no es un indice que va a recorrer cada espacio, Lo utilizo para mostrar cada elemento por cada vuelta que se realiza. Entonces por ese motivo se necesita mostrar como si fuese que no lo instanciamos con un ciclo.
    print(colores[I])
    I=I+1