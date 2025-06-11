#Blanquear un vector
#Vector con elementos
Animales = ["Jirafa","Ratón","Zebra","Gorreón","Gato"]
"""
for I in range (0,len(Animales)):
    Animales[I] = None
"""
Animales.clear()#Solo asi como está blanquea o elimina todos los elementos del array dejandolo vacio
for I in Animales:
    print(I)