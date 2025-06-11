#Condicional Compuesto que era el And o el Y y el Or o el O
#Ej
Edad=16
#Esto es lo mismo que una seleccion, como establecer un rango de edad válido que esto se puede represantar en una escala númerica
if(Edad>=18 and Edad<=45):#Números que se encuentren entre 18 y 45 son los que cumplen con la segmentación que esteblacemos en la condición. Aquellos valores numéricos que no cumplan con esta condición van a ser mentira.
    print("Está obligado a votar")
else:
    print("No puede votar")

#Esto es mas sencillo que programar
if(Edad>18):
    if(Edad<45):
        print("Está obligado a votar")
else:
    print("No puede votar")

#Esto se puede aplicar al ejemplo del clase7-5.py
Letra="E"
if(Letra=="A" or Letra=="E" or Letra=="I" or Letra=="O" or Letra=="U"):
    print("Es una vocal la letra")
else:
    print("La letra no es una vocal")
