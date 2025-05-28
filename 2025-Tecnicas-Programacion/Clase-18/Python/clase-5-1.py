"""
codificar un programa que permita el ingreso de las distintas materias de una escuela 
y los distintos alumnos que se encuentran anotados dentro de un curso. 
Para eso la escuela debe especificar cuantas materias tiene en total por cada año, 
y ademas cuantos cursos tiene en cada año respectivo. 
Se pide mostrar el total de alumnos, el total de materias y el promedio de alumnos que se encuentren en el ultimo año. 
"""

def alumno(nombre,apellido,dni,sexo,anio,curso):
    cargaAlumno=f"{nombre} {apellido} {dni} {sexo} {anio} {curso}"
    return cargaAlumno

def materias(nombre,docente,anio,curso):
    cargaMateria=f"{nombre} {docente} {anio} {curso}"
    return cargaMateria

print("Necesito que ingreses la cantidad de años en total que tiene tu institucion educativa:")
canios=int(input())

print("Necesito que ingrese la cantidad total de materias por año que tiene tu institucion educativa")
cmaterias=int(input())
mostrar=""

for i in range(0,canios):
    print(f"Ingrese la cantidad de cursos que tiene el {i+1} años")
    ccursos=int(input())
    for x in range(0,ccursos):
        for z in range(0,cmaterias):
            materia=input(f"Ingrese la materia del curso {i+1} {x+1}")
            docente=input(f"Ingrese el docente a cargo de la materia {materia}")
            mostrar=mostrar+materias(materia,docente,i,x)+"""
"""
    calumnos=int(input("Ingrese la cantidad de alumnos del curso {i+1} {x+1}"))
    for y in range(0,calumnos):
        nombre=input(f"Ingrese el nombre del alumno del curso  {i+1} {x+1}")
        apellido=input(f"Ingrese el apellido del alumno del curso  {i+1} {x+1}")
        dni=input(f"Ingrese el dni de {nombre} {apellido} del curso  {i+1} {x+1}")
        sexo=input(f"Ingrese el sexo de {nombre} {apellido} del curso  {i+1} {x+1}")
        alumno(nombre,apellido,dni,sexo,i,x)
        
print(mostrar)