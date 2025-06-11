#Condicional Anidado
#Es decir es un condiconal que se encuentra conectado o dentro de otro condicional, a eso se lo conoce o se llama condicional anidado.
Letra = "Z"
if(Letra=="A"):
    print("Es una vocal la letra")
else:
    print("La letra no es una vocal")

#En este caso no alcanza con un solo condicional. Porque las otras letras que son vocales, como la "e" la "i" y la "u" no las estoy analizando, entonces por ese motivo un solo condicional, no alcanza para analizar correctamente esta prueba lógica. Necesito otro condicional
if(Letra=="A"):
    print("Es una vocal la letra")
else:
    if(Letra=="E"):
        print("Es una vocal la letra")
    else:
        print("No es una vocal")

#En este caso volvemos a lo mismo, porque ahora solo alcanza hasta analizar la e. La i y la u quedaron fuera. Entonces, necesito la repregunta hasta que cumpla con lo básico a analizar.
if(Letra=="A"):
    print("Es una vocal")
else:
    if(Letra=="E"):
        print("Es una vocal")
    else:
        #Otro condicional
        if(Letra=="I"):
            print("Es una vocal")
        else:
            #Sigue sin alcanzarme, porque ahora necesito la u y la O tambien
            if(Letra=="O"):
                print("Es una vocal")
            else:
                #Sigo preguntando
                if(Letra=="U"):
                    print("Es una vocal")
                else:
                    #Ya no necesito mas nada para comparar, asi que cierro
                    print("No es una vocal")

#Esto se puede resumir o simplificar con el elif
if(Letra=="A"):
    print("Es una vocal")
elif(Letra=="E"):
    print("Es una vocal")
elif(Letra=="I"):
    print("Es una vocal")
elif(Letra=="O"):
    print("Es una vocal")
elif(Letra=="U"):
    print("Es una vocal")
else:
    print("No es una vocal")