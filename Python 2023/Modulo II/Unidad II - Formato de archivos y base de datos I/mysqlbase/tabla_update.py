import mysql.connector

mibase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_plantilla2"
)

micursor = mibase.cursor()

sql = "UPDATE producto SET titulo = %s WHERE id = %s"
datos = ("producto1Modificado", 2)
micursor.execute(sql, datos)
mibase.commit()