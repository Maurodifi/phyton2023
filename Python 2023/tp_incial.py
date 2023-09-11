import sqlite3


def crear_base():
    global db
    db = sqlite3.connect("baseTPinicial.db")


def crear_tabla():
    global cursor
    cursor = db.cursor()
    sql = "CREATE TABLE IF NOT EXISTS personas(id PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50) NOT NULL, apellido VARCHAR(50) NOT NULL, documento INT NOT NULL, correo VARCHAR(50) NOT NULL, filiacion VARCHAR(50)"
    cursor.execute(sql)
    db.commit()


def registrarpersona():
    sql = "INSERT INTO personas (nombre, apellido, documento, correo) VALUES (%s, %s, %s, %s)"
    datos = ("Mauro", "Di Filippo", 44544627, "maurodifi16@gmail.com" )
    cursor.execute(sql, datos)
    db.commit()

def consultarpersona():
    var_documento = 44544627
    sql = "SELECT * FROM producto WHERE documento = " + var_documento
    cursor.execute(sql, datos)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

def modificarpersona():
    sql = "UPDATE producto SET titulo = %s WHERE id = %s"
    datos = ("producto1Modificado", 2)
    micursor.execute(sql, datos)
    mibase.commit()

def eliminarpersona():