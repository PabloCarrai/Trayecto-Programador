import os

#   Me trae la ruta absoluta del archivo
ruta = os.path.abspath("Marina.db")

print(f"La ruta es {ruta}")

#   Otra forma
ruta1 = os.path.basename("Marina.db")
print(ruta1)


#   otra forma de devolver rutas
directorio="/home/ed/Trayecto-Programador/2025-Programacion-Objeto/Clase-20/Marina.db"
print(os.path.dirname(directorio))

#   obtener ruta 
print(os.path.realpath("Marina.db"))

#   eliminar archivo
os.remove("/home/ed/Trayecto-Programador/2025-Programacion-Objeto/Clase-20/Marina.db")