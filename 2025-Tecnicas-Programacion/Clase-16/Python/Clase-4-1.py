#   Defino la funcion
def alumno():
    print("Bienvenido a campus 2.0.1")
    print("Ingrese el nombre del estudiante ")
    estudiante=input("")
    print("Ingrese la primer nota ")
    n1=int(input())
    print("Ingrese la segunda nota")
    n2=int(input())
    print("Ingrese la tercer nota")
    n3=int(input())
    promedio=(n1+n2+n3)/3
    return "El promedio de las notas es: ",promedio

#   la invoco
print(alumno())