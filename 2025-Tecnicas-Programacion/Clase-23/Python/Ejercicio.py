"""
Realizar un programa que permita Mostrar 10 pedidos en un restaurant. 
Se pide mostrar el mayor precio. 
La menor cantidad de productos y el sueldo promedio de los empleados
"""

pedidos=[]
precios=[]
empleados=[]
sueldos=[]

def menu():
    print("Bienvenido al restaurante ")
    print("""
       
       1)   Cargar Empleado
       2)   Mostrar Empleado
       3)   Mostrar Maximo Sueldo
       4)   Mostrar Promedio Sueldo
       5)   Salir   
          
          """)
    eleccion=int(input("Ingrese una opcion"))
    while(eleccion<1 or eleccion>5):
        eleccion=int(input("Ingrese una opcion(Valida)"))
    if(eleccion==5):
        salir()
    elif(eleccion==1):
        cargarE()
    elif(eleccion==2):
        listarS()
    elif(eleccion==3):
        pass
    elif(eleccion==4):
        pass

def cargarE():
    ceCargar=int(input("Cuantos empleados va a cargar? "))
    for i in range(ceCargar):
        nombre=input("Nombre del emplado  ")
        sueldo=int(input(f"Sueldo neto de {nombre} "))
        empleados.append(nombre)
        sueldos.append(sueldo)
    menu()

def salir():
    print("Adios")

def listarS():
    for i in range(len(empleados)):
        print(f"""
        id {i} Empleado {empleados[i]} Sueldo ${sueldos[i]}      
        """)
    menu()    



    
menu()