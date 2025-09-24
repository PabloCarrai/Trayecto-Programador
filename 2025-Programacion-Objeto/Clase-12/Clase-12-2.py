#   Importamos el modulo de mysql
import sqlite3

conectar = sqlite3.connect("python.db")

referencia = conectar.cursor()

if (conectar == True):
    print("Conexion exitosa")
else:
    print("Intente configurar para conectar")

# referencia.execute("CREATE table usuarios(id_usuario int primary key,nombre varchar(255),email varchar(255));")

referencia.execute(
    "insert into usuarios(nombre,email) values('juan','juan@gmail.com')")
conectar.commit()
consulta = referencia.execute("SELECT nombre,email FROM usuarios;")


print(consulta.fetchone())

conectar.close()
