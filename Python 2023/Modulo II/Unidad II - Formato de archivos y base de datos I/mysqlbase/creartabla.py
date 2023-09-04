import mysql.connector

mibase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_plantilla2"
)

micursor = mibase.cursor()

micursor.execute("CREATE TABLE producto(id int(7) NOT NULL PRIMARY KEY, titulo VARCHAR(50))")