import mysql.connector


mydb = mysql.connector.connect(
    user="root",
    passwd="SomosDeCarn3",
    host="192.168.0.222",
    port=3307,
    database="db1",
)

mycursor = mydb.cursor()


valores = []
sql = "insert into usuarios(nombre,direccion,telefono)values(%s,%s,%s)"

for i in range(3):
    nombre = input("Nombre? ")
    direccion = input("Direccion ")
    telefono = input("Telefono ")
    valores.append((nombre, direccion, telefono))


mycursor.executemany(sql, valores)
mydb.commit()

mycursor.close()
mydb.close()
