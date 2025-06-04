#   Condicional anidado
letra="A"
if(letra=="A"):
    print("Es una vocal la letra")
else:
    print("La letra no es una vocal")
    

if(letra=="A"):
    print("Es una vocal la letra")
else:
    if(letra=="E"):
        print("Es una vocal la letra")
    else:
        print("No es una vocal")
        
if(letra=="A"):
    print("Es una vocal")
else:
    if(letra=="E"):
        print("Es una vocal")
    else:
        if(letra=="I"):
            print("Es una vocal")
        else:
            if(letra=="O"):
                print("Es una vocal")
            else:
                if(letra=="U"):
                    print("Es una vocal")
                else:
                    print("No es una vocal")
                    
                    
                    
#   Simplificado con elif
if(letra=="A"):
    print("Es una vocal")
elif(letra=="E"):
    print("Es una vocal")
elif(letra=="I"):
    print("Es una vocal")
elif(letra=="O"):
    print("Es una vocal")
elif(letra=="U"):
    print("Es una vocal")
else:
    print("No es una vocal")