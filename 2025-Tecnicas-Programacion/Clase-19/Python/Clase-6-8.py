#   Vaciar un array
animales=["Jirafa","Raton","Zebra","Gorrion","Gato"]
for i in range(0,len(animales)): #  len nos muestra cantidad de elementos del vector
    animales[i]=None
    
for i in animales:
    print(i)

animales=["Jirafa","Raton","Zebra","Gorrion","Gato"]
    
#   otra forma
animales.clear()

for i in animales:
    print(i)
