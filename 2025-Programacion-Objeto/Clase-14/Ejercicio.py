import mysql.connector


def crearDB():
    mydb = mysql.connector.connect(
        user="root", passwd="SomosDeCarn3", host="192.168.0.222", port=3307
    )

    mycursor = mydb.cursor()
    mycursor.execute("create database ejercicio")
    mydb.close()
    print("DB creada")


def crearTabla():
    mydb = mysql.connector.connect(
        user="root",
        passwd="SomosDeCarn3",
        host="192.168.0.222",
        port=3307,
        database="ejercicio",
    )

    mycursor = mydb.cursor()
    mycursor.execute(
        "create table usuario(id int auto_increment primary key,nombre varchar(30),telefono varchar(30))"
    )
    mydb.close()
    print("tabla creada")


#crearDB()
crearTabla()
