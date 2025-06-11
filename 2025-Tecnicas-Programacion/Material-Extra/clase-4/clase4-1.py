promedio = 0
def Alumno():
    print("╔═══════════════════════════╗")
    print("║ Bienvenido a Campus 2.0.1 ║")
    print("╚═══════════════════════════╝")
    print("Ingrese el nombre del alumno:")
    alumno = input()
    print("Ingrese la primer nota:")
    n1 = int(input())
    print("Ingrese la segunda nota:")
    n2 = int(input())
    print("Ingrese la tercer nota:")
    n3=int(input())
    return alumno,n1,n2,n3

print(Alumno())
print(promedio)