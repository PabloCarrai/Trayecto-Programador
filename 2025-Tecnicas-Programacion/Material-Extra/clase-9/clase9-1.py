#Repaso Funciones la venganza del la funciones
#Para qué sirven? Para no tener la necesidad de estar utilizando un mismo bloque de código varias veces en nuestro programa. Como así también, nos sirve para reutilizar ese código a lo largo de nuestro programa la cantidad de veces que sean necesarias.
#¿Cómo declarar una función?
def IngresarEdad(): #Siempre va la palabra reservada def seguido del nombre de la función y los parentesis, que decimos, que dentro van los parámetros de la función. Si no hay, van a estar vacios.
    #Dentro de la función, establezco o programo la función o el bloque de código que quiero reutilizar.
    print("Ingrese el año de nacimiento:")
    edad=int(input())#ACLARACIÓN: TODA VARIABLE DECLARADA DENTRO DE UNA FUNCIÓN. NACE Y MUERE DENTRO DE ELLA.
    #Una vez que se programo el código que quiero reutilizar, no debo olvidar que la función debe retornar algo, ese algo es un valor que devuelve de manera interna la funcion
    return edad
#Esta funcion que programamos, permite que el usuario ingrese una edad y luego lo guardamos y retornamos, es decir, nos quedamos con ese valor.
#Ahora necesitamos una vez que existe la función, necesitamos ejecutarla. Para ejecutarla, siempre es el nombre de la función con los parentesís, que dentro van los argumentos en cuyo caso que la función tenga los parámetros.
IngresarEdad()#En este caso al no tener parámetros la función no necesito generar ningun argumento. NOTA: EN ESTE PUNTO SE EJECUTA LA FUNCIÓN, PERO EL DATO, ES DECIR LO QUE RETORNA, SOLAMENTE EXISTE INTERNATE. OSEA NO VAMOS A VISUALIZAR SU VALOR POR PANTALLA.
#Para poder visualizar ese valor debo utilizar antes del llamado el print
print(IngresarEdad())
#Repaso Vectores
#¿Qué era un vector?
#Un conjunto o lista de elementos que pueden ser o son de distinto tipo de dato que se guardan en una sola variable, y también ocupan un solo espacio de la memoria.
#cómo defino una lista:
cabeza = [] #Es una lista vacia, pero es la definición de una lista
#¿Cómo le cargo valores?
cabeza = ["Pelo","Ojos",231,1,33]#Este es una manera manual, es decir, internamente
#Otra opcion es un mediante un ciclo, donde le establezco la cantidad de valores que deseo guardar. Por Ejemplo
Colores = []
for I in range(0,5):
    #Pido al usuario ingresar un valor
    print("Ingrese un valor a agregar:")
    ingreso=input()
    Colores.append(ingreso)#Recuerden que la funcion append, es para agregar valores a la lista. Entre parentesis va el dato que deseo agregar, ese dato en este caso es el que ingresa el usuario, que está guardado en la variable ingreso. Por ese motivo entre parentesis va la variable ingreso.

#¿Cómo mostramos valores de una lista?
for x in Colores:
    print(x)

print(cabeza[0])

for x in range(len(cabeza)):
    print(x,cabeza[x])
#la funcion len() lo que hace es calcular la cantidad de elementos que tiene en este caso el vector "cabeza"
#Repaso Matriz