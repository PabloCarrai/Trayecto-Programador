"""
Repaso Funciones 
Vectores
Matriz   
"""
#   Declaro una funcion
def nombreFuncion():    #   Declaracion
    pass    #   Codigo de la funcion

#   Llamada a una funcion
nombreFuncion()

#   Ejemplo
def saludar():
    print("Hola como estas?")

saludar()

#   Otro ejemplo
def ingresarEdad():
    print("Ingrese el año de nacimiento: ")
    edad=int(input())
    return f"Nacio {edad}"

    
print(ingresarEdad())    

#   Vectores
lista=["uno","dos","tres"]
listavariada=["Listo",True,2,3.4,[2,3,4,"Llaves"]]
listavacia=[]

#   Aca lo cargo por un bucle for
colores=[]
for i in range(0,5):
    print("Ingrese un valor ")
    ingreso=input()
    colores.append(ingreso)
    
#   Aca los muestro
for x in colores:
    print(x)