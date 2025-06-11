# recibe el dato "Pablo"
# Lo asigna a el párametro nombre
#           nombre = "Pablo"
def Saludar(nombre):
    return f"Bienvenido {nombre}"

#Dare la bienvenida a un usuario
# Pablo es el argumento que le voy a dar a el párametro nombre
print(Saludar("Pablo"))
print(Saludar("Mauro"))
print(Saludar("Marina"))
print(Saludar("Lautaro"))
print(Saludar("Valeria"))
print(Saludar("Abel"))
#Párametros 1   y Párametro
# numero1 = 1, numero2 = 3
def Suma(numero1 = 0, numero2 = 0):
    #suma = 1, 3
    numero1=int(input("Ingrese un número: "))
    numero2=int(input("Ingrese otro número: "))
    suma=numero1+numero2
    return suma
#Enviar Argumentos que recibe cada párametro
#   Argumento 1 y Argumento 2
#print(Suma(1,3))
#print(Suma(2,4))
#print(Suma(7,6))
#################
print(Suma())