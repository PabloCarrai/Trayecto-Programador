"""
Codificar un Array que muestre 10 notas de 10 alumnos ingresados por el usuario
"""

#   Uso la lista notas para guardar las notas
notas=[]
#   Lista con los nombre de los estudiantes
nombres=[]
#   Creo el for para ingresar las notas
for i in range(3):
    nombre=input("Nombre del estudiante  ")
    nota=int(input(f"Ingrese la nota del alumno {nombre}: "))
    while(nota<0 or nota>10):
        print("Ingrese una nota correcta(de 0 a 10)")
        nota=int(input(f"Ingrese la nota del alumno {nombre}: "))    
    #   Agrego las notas a la lista
    notas.append(nota)
    nombres.append(nombre)

#   Muestro las notas   
print("Las notas ingresadas son ")
for i in range(3):
    print(f"Nota estudiante: {nombres[i]} Nota: {notas[i]}: ")