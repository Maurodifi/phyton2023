from tkinter import *
import tkinter as tk
import mysql.connector

mibase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_plantilla2"
)

main = Tk()
micursor = mibase.cursor()



main.title("Hola S.O")
var_nombre = StringVar()
var_apellido = StringVar()
titulo = Label(main, text="Mi primer APP", width=25)
titulo.grid(pady=10)

nombre = Label(main, text="Nombre")
nombre.grid(column=0, row=1, sticky= W)
nombreEntry = Entry(main, textvariable=var_nombre)
nombreEntry.grid(column=1, row=1)

apellido = Label(main, text="Apellido")
apellido.grid(column=0, row=2, sticky= W)
apellidoEntry = Entry(main,textvariable=var_apellido)
apellidoEntry.grid(column=1, row=2)

 
def funcion ():
    sql = "INSERT INTO primerapp (nombre, apellido) VALUES (%s, %s)"
    dato1 = str((var_nombre.get()))
    dato2 = str((var_apellido.get()))
    dato = [dato1, dato2]
    micursor.execute(sql, dato)
    mibase.commit()
    


def funcionS():
    main.configure(bg='#EB1A01')

def funcionM():
    sql = "SELECT * FROM primerapp"
    micursor.execute(sql)
    resultado = micursor.fetchall()
    for x in resultado:
        print(x)


boton_e = Button(main, text="Alta", command=funcion)
boton_e.grid(row=3, column=0)

boton_s = Button(main, text="Sorpresa", command=funcionS)
boton_s.grid(row=3, column=1)

boton_m = Button(main, text="Mostrar", command=funcionM)
boton_m.grid(row=4, column=0)





main.mainloop()