"""

Codificar un programa que permita ingresar empleados de una 
empresa que tiene 3 sedes. Cada sede tiene 15 empleados respectivamente. 
Se pide mostrar el sueldo promedio de los empleados 
y cantidad total gastada por cada sede en los materiales.
(Deben utilizar al menos 2 funciones)


"""

def crearSede():
    nombreSede=input("Ingrese el nombre de la sede")
    return nombreSede
    
def cargarEmpleado():
    cs=0    
    for i in range(0,15):
        nombre=input("Ingrese el nombre del empleado ")
        sueldo=int(input("Ingrese el sueldo del empleado"))
        cs=cs+sueldo
    promedio=cs/15
    return f" El promedio del sueldo es {promedio}"

for i in range(0,3):
    sede=crearSede()
    empleados=cargarEmpleado()
    print(sede)
    print(empleados)