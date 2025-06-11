#Acá repasamos condicionales
#Recordemos que los condicionales son llamados pruebas lógicas que permiten analizar/comparar y si se cumple la condición va a pasar algo por verdad, siempre y cuando la condición se cumpla. Si no se cumple, va a pasar algo por mentira o por descarte, es decir. Si se cumple ocurre una acción, si no se cumple, ocurre otra.
Numero1=9
Numero2=6
#Analizamos si un número es mayor al otro
#La prueba analiza si el primer numero es mayor que el segundo. Si se cumple
if (Numero1>Numero2):
    #Muestra este cartel por verdad
    print(f"El número 1 es verdad que es mayor que el número 2. El mayor es: {Numero1}")
else:#Si no se cumple
    #Muestra este cartel por mentira
    print(f"El número 1 es mentira que es mayor que el número 2. El mayor es: {Numero2}")

Numero1=6
Numero2=9
#La pureba analiza si el primer numero es mayor que el segundo. Si se cumple
if (Numero1>Numero2):
    #Muestra este cartel por verdad
    print(f"El número 1 es verdad que es mayor que el número 2. El mayor es: {Numero1}")
else:#Si no se cumple
    #Muestre este cartel por mentira
    print(f"El número 1 es mentira que es mayor que el número 2. El mayor es: {Numero2}")

#Este condicional, es el simple y analiza una sola prueba lógica, por ese motivo, va a suceder algo por verdad y algo por mentira, no existe la repregunta. Eso se da cuando tenemos mas pruebas lógicas para analizar. Que veremos en clase7-5.py
operacion="+"
if(operacion=="+"):
    print(f"La suma es: {Numero1+Numero2}")

#En este caso este condicional solo tiene algo por verdad y nada por mentira, porque no se necesita, podríamos analizar solo el tipo de operacion ingresada, entonces esto queda:
if(operacion=="+"):
    print(f"La suma es: {Numero1+Numero2}")
if(operacion=="-"):
    print(f"La Resta es: {Numero1-Numero2}")
if(operacion=="*"):
    print(f"La Multiplicacion es: {Numero1*Numero2}")
if(operacion=="/"):
    print(f"La Division es: {Numero1/Numero2}")
#Solo muestra la suma, porque en ningun momento la variable operación, cambio de operacion, por ese motivo solo muestra la suma.