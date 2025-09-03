"""  
Se pide programar un objeto que procese distintos
materias en un cuatrimestre de una universidad. 
Debe procesarse el nombre de la materia. El docente 
a cargo el nombre de la carrera. El turno y la cantidad
de alumnos anotados. Por otro lado Cada alumno debe poseer
un nombre, apellido, dni y las notas de cada materia. 
Se pide mostrar los alumnos que hayan aprobado las materias
sabiendo que se aprueba con 4, mostrando un cartel diciendo
aprobado. En cualquier otro caso recursa 
"""


class materia():
    def __init__(self):
        nombre = input("Nombre? ")
        docente = input("Docente? ")
        turno = input("Turno? ")
        cantidad_Alumnos = int(input("Cantidad de alumnos? "))
        carrera = input("Carrera? ")
        self.nombre = nombre
        self.docente = docente
        self.turno = turno
        self.cantidad_Alumnos = cantidad_Alumnos
        self.carrera = carrera
        self.cantidad_notas = int(input("Cantidad de notas? "))


class alumnos():
    def __init__(self):
        notas = []
        nombre = input("Nombre? ")
        apellido = input("Apellico? ")
        dni = input("dni? ")
        nota = int(input("Notas? "))
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nota = nota
        notas.append(nota)


biologia = materia()
jose = alumnos()
