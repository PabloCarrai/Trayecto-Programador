"""

Realizar un vector con una carga de 10 materias, Otro vector con la carga de 10 alumnos 
y otro vector con la carga de 10 notas.Mostrar las 10 materias cargadas. 
Luego en conjunto mostrar la carga de las notas y los alumnos


"""

#   Creo las listas necesarias
materias=[]
estudiantes=[]
notas=[]
todo=[]

#   Recorro con un for pidiendo los datos y agregandolo a cada lista
for i in range(10):    
    nombre=input("Nombre del estudiante  ")
    materia=input(f"Materia del estudiante {nombre} ")
    nota=int(input(f"Nota del estudiante {nombre}  "))    
    while(nota<1 or nota>10):
        print("La nota ingresada no es correcta, ingrese nuevamente")
        nota=int(input(f"Nota del estudiante {nombre}  "))    
    estudiantes.append(nombre)
    materias.append(materia)
    notas.append(nota)

#   Recorro estudiante y agrego la info para cada elemento a las otras listas
for i in range(len(estudiantes)):
    todo.append([estudiantes[i],materias[i],notas[i]])

#   Visualizo la matriz
for i,j,k in todo:
    print(f"Nombre {i}  Materia {j} Nota {k}")
