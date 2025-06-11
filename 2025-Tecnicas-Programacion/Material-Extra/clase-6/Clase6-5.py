#Vectores - Arrays - Listas - Filas - Columnas
#¿Para qué sirve o qué son?
#En si los vectores que el con es el nombre con el cual se reconoce mayormente. Es un espacio que se asigna y se almacena en la memoria que permite distintos tipos de datos, a diferencia de las variables, que recordemos solo permite un valor y un tipo de dato, en un espacio de la memoria. Es decir, que los vectores permiten almacenar y asignar distintos tipos de datos en un solo espacio de la memoria ram.

Colores = [] #Esto es un array pero vacio
#Es una variable que le doy un nombre le asigno no un valor, si no, un vector
#Vamos a ver un array de ejemplo
Frutas = ["Banana","Frutilla","Kiwi","Melón"] #este un array de 4 elementos
#Lo importante, es que el primer elemento o valor se lo reconoce como indice 0, el segundo se lo reconoce como indice 1, el tercero como indice 2 y el cuarto como indice 3. En este caso el array arranca en el indice 0 y termina en el indice 3.
#Lo que hicimos darle los valores que tiene ese array, pero nos falta mostrarlos.
#Para mostrarlos lo hacemos con un print, donde llamamos y mostrarmos a la variable y el indice que necesito mostrar ej:
print(Frutas[0])#Se muestra el primer elemento del array Frutas. Aca muestra "Banana"
print(Frutas[1])
print(Frutas[2])
print(Frutas[3])

#¿Qué pasa si por error sigo mostrando elementos del vector, pero que aun no tienen valor o no se les dió ningun valor.
print(Frutas[9])#No se puede, osea va a tirar error, porque dice que no existe o aun no se creo ese valor de indice dentro de ese array. No se puede listar ese valor porque está fuera de rango.