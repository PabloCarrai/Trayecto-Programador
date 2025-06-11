#Funciones con parametros
#Dentro del parantesis, se le asigna uno o mas nombres, dependiendo de la necesidad para introducir valores y no tener la necesidad de crear variables
def Suma(a,b):
#En este caso se crea un párametro llamado a, y otro llamado b
    suma = a+b
    #La operación es la misma, pero, con la diferencia que estoy llamando a los párametros. Se Guardan, dentro de la variable suma
    return suma

#Esto que beneficio trae?
#Ahora puedo llamar a la función y enviarle directamente los valores, que necesito para esa operación
print(Suma(2,1))
#Ese 2, va a ser leido por el párametro a, el 1 va a ser leído por el parametro b.
#Esto es lo mismo que decir a=2 y b=1. Con la diferencia que la función va a leer y asignar automáticamente, sin que lo realicemos mediante el código
#Este sería generando los valores de manera interna
print(Suma(3,4))
print(Suma(2,4))
print(Suma(6,1))
#Ahora vamos a ver como queda si le pido ingresar al usuario
#se crea una variable donde se guarda el valor que ingresa el usuario
print("Ingrese un valor: ")
valor1=int(input())
print("Ingrese otro valor: ")
valor2=int(input())
#Que esto una vez que se guarda se lo envio a la función que necesito realizar
print(Suma(valor1,valor2))
#Se va a asignar el valor en el párametro a, a lo que ingresa el usuario, en este caso, en el valor 1. También se asigna el valor en el párametro b, a lo que ingrese el usuario, en este caso, en el valor2
#Esto es lo mismo que decir a=valor1, b=valor2