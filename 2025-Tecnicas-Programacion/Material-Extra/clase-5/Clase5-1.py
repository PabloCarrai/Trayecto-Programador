#Codificar un programa que permita el ingreso de las distintas materias de una escuela, y los distintos alumnos que se encuentran anotados dentro de un curso. Para eso la escuela debe especificar cuantas materias tiene en total por cada año, y además cuantos cursos tiene en cada año respectivo. Se pide mostrar el total de alumnos, el total de materias. El total de alumnos que se encuentren en el último año.

def Alumnos(nombre,apellido,dni,sexo,anio,curso):
    CargarAlumno=f"{nombre} {apellido} {dni} {sexo} {anio} {curso}"
    return CargarAlumno

def Materias(nombre,docente,anio,curso):
    CargarMateria=f"{nombre} {docente} {anio} {curso}"
    return CargarMateria

print ("Necesito que ingreses la cantidad de años en total que tiene tu institución educativa:")
Canios = int(input())

print("Necesito que ingreses la cantidad total de materias por año que tiene tu institución educativa:")
Cmaterias = int(input())
mostrar=""
#Ciclo para ingresar todo lo relacionado a ese año respectivo
for I in range(0,Canios):
    print(f"Ingrese la cantidad de cursos que tiene el {I+1} año: ")
    Ccursos = int(input())
    #Ciclo para ingresar materias y alumnos del curso actual
    for X in range(0,Ccursos):
        #Ciclo para ingresar las materias y asignar docentes
        for Z in range (0,Cmaterias):
            materia=input(f"Ingrese la Materia del curso {I+1} {X+1}: ")
            docente=input(f"Ingrese el docente a cargo de la materia {materia}: ")
            mostrar=mostrar+Materias(materia,docente,I,X)+"""
"""
        #Fin de ciclo de ingreso de materias
        CAlumnos=int(input(f"Ingrese la cantidad de alumnos del curso: {I+1} {X+1}"))
        #Ciclo para ingresar los alumnos del año y del curso especifico
        for Y in range (0,CAlumnos):
           nombre=input(f"Ingrese el nombre del alumno del curso {I+1} {X+1}:")
           apellido=input(f"Ingrese el apellido del alumno del curso {I+1} {X+1}:")
           dni=input(f"Ingrese el dni de {nombre} {apellido} del curso {I+1} {X+1}:")
           sexo=input(f"Ingrese el sexo de {nombre} {apellido} del curso {I+1} {X+1}:")
           Alumnos(nombre,apellido,dni,sexo,I,X) 

print(mostrar)