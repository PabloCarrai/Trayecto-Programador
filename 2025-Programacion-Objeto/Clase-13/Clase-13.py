import mysql.connector


host = mysql.connector.connect(
    user="root",
    passwd="SomosDeCarn3",
    host="192.168.0.222",
    port=3307,
    database="db1",
)

secuencia=host.cursor()
secuencia.execute("create table users(id int auto_increment primary key,nombre varchar(255),mail varchar(255),pass varchar(255))")
host.commit
secuencia.close()
host.close()