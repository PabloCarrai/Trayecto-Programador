class Persona:
    def __init__(self,nombre,edad,nacionalidad,sexo):
        print(f"El nombre de la persona creada es: {nombre} la edad: {edad}, cuya nacionalidad {nacionalidad}, sexo {sexo}") 
        
mostrar=""
for i in range(10):
    nombre=input("Nombre? ")
    edad=input("Edad? ")
    nacionalidad=input("Nacionalidad? ")
    sexo=input("Sexo? ")
    mostrar=Persona(nombre,edad,nacionalidad,sexo)