from tkinter import *
import tkinter as tk

main = Tk()


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

nombresdict = {}
nombres = {}

def funcion ():
    nombres['Nombres'] = var_nombre.get()
    nombres['Apellido'] = var_apellido.get()
    nombresdict.update(nombres)
    


def funcionS():
    main.configure(bg='#EB1A01')

def funcionM():
    print(nombresdict)


boton_e = Button(main, text="Alta", command=funcion)
boton_e.grid(row=3, column=0)

boton_s = Button(main, text="Sorpresa", command=funcionS)
boton_s.grid(row=3, column=1)

boton_m = Button(main, text="Mostrar", command=funcionM)
boton_m.grid(row=4, column=0)





main.mainloop()