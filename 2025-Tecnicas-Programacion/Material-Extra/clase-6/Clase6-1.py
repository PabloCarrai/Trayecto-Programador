#Repaso de funciones
#def definimos o establecemos que vamos a instanciar una función
#def NombreDeFuncion() Definición y nombramiento de la función ej:
def Suma():
#Esta función no tiene párametros
    #Generamos el código o instrucciones que queremos que realice la función cuando la llamamos
    suma = a+b
    #En este caso generamos una variable suma y le guardamos la operación de suma entre dos variables que se envian o se toman desde afuera de la función
    return suma
    #Siempre las función hacen un retorno, es decir, devuelven un resultado. Ese resultado, puede ser la, el resulatado de esa operación, un valor número, un texto, o el mensaje que quiero mostrar, etc.

a=2
b=1
Suma()#Llamo a la función suma para que realice la operación que necesito de estas variables con esos valores asignados.
#Aclaración, el resultado no se verá en pentalla, porque la función devuelve el resultado de manera intera, para poder mostrarlo, se necesita imprimirlo por pantalla al usuario
print(Suma())
#Este ejemplo es introduciendo los valores de manera manual, es decir, dentro del código y no se pueden modificar.
#Ahora vamos a pedirle al usuario que ingrese los valores y luego los mostraremos por pantalla con el llamado a la función.
a=int(input("Ingrese un valor: "))
b=int(input("Ingrese otro valor: "))
print(Suma())
#Este ejemplo es mostrar la suma de los valores ingresados por el usuario.

#Se los dejo este código en limpio
def Suma():
    suma = a+b
    return suma
a=int(input("Ingrese un valor: "))
b=int(input("Ingrese otro valor: "))
print(Suma())