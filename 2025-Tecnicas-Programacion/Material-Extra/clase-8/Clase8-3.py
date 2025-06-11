"""Realizar un vector con una carga de 10 materias, Otro vector con la carga de 10 alumnos y otro vector con la carga de 10 notas.
Mostrar las 10 materias cargadas
Luego en conjunto mostrar la carga de las notas y los alumnos"""
Materias = []
for I in range(0,10):
    print("ingrese el nombre de la materia:")
    materia = input()
    Materias.append(materia)

Alumnos = []
for J in range(0,10):
    print("Ingrese el nombre y apellido del alumno:")
    alumno = input()
    Alumnos.append(alumno)

Notas = []
for K in range(0,10):
    #Agrego un ciclo mientras para obligar al usuario a ingresar notas entre 1 y 10
    nota=int(input("Ingrese la nota del alumno:"))
    while(nota<1 or nota>10):
        print("La nota ingresada no es correcta, Ingrese nuevamente")
        nota=int(input("Ingrese la nota del alumno:"))
    Notas.append(nota)

for Z in range(0,10):
    print(f"Las materia es: {Materias[Z]}")
    print(f"El alumno {Alumnos[Z]} apróbo con una nota {Notas[Z]}")