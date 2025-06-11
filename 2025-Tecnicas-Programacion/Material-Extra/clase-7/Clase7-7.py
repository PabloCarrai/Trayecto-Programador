#Aca vamos a recordar ciclos
#Ciclo For | Ciclo While
#Ciclo For: Es un ciclo exacto porque tengo donde iniciar y tengo un tope.
#Ciclo While: Permite que se ejecute un bloque de código siempre y cuando se cumpla una condición.
"""for I in range(1,6):
    print(I)"""
#El ciclo sirve para repetir una x cantidad de veces un bloque de código para no tener la necesidad de estar realizando constantemente ese bloque de código por ejemplo 10 veces.
#Repasamos Contadores y Acumuladores
#En este necesitamos que solo ingrese y al final mostrar todas las temperaturas ingresadas
#Eso lo hacemos con un acumulador
acu="" #Primero el acumulador lo vaciamos, es decir lo inicializamos vacio
for I in range(1,6):
    print("Vamos a Ingresar la temperatura de los días de la semana")
    print(f"Necesito que ingreses la Temperatura del {I} día habil:")
    dia=input("")
    #Vamos a acumular el mensaje que necesito mostrar al final
    acu=acu+dia+'\n'#Aca se va a ir acumulando el día y un salto de linea

#Cuando termina el ciclo mostramos el resultado acumulado
#Eso se realiza imprimiendo la variable que utilizamos como acumulador
print(acu)

#Para el contador previamente vamos a repasar el ciclo while.
#El ciclo while funciona hasta que se deja de cumplir una condiciona. Se va a repetir siempre y cuando la condicion siga siendo verdad.
#Antes de entrar necesitamos evaluar o establecer la condición para ingresar al ciclo
print("Ingrese la letra a para ingresar")
letra=input()
#Establezco el contador
c=0#Primero le establezco a mi contador un número por el cual va a empezar
while(letra=="a"):
    print("Estás dentro del ciclo y estás en la vuelta N°:")
    print(c)
    #Dentro del ciclo lo que hago es decir cuanto va a aumentar por cada vuelta el contador
    c=c+1
    #En este caso este contador va a ir contando de uno en uno.
    #Lo que está faltando es volver a preguntar la letra a ingresar. Para saber si sigue o no dentro del ciclo
    print("Ingrese la letra a para seguir dentro del ciclo")
    letra=input()

#Una vez sale muestro la cantidad de vueltas realizadas
print(f"La cantidad de vueltas o de ingresos es de: {c}")

#el acumulador acumula datos, ya sea numero o texto y su declaracion es sumar la variable que usamos como acumulador + otra variable ej
#total=total+precio
#Esto es un ejemplo de acumulador
#En cambio el contador, cuenta y muestra un total expresado como número, puede ser cantidad de vueltas, cantidad de empleados, alumnos, etc. Ej:
#CAlumno=CAlumno+1
#La diferencia a simple vista es que el contador suma y cuenta, en cambio el acumulador, suma y como dice su nombre acumula los disntitos valores.