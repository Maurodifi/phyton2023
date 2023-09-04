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


def funcion ():
    print("Tu nombre es, ",var_nombre.get()," y tu apellido ", var_apellido.get())


def funcionS():
    main.configure(bg='#EB1A01')
    nombre.configure(bg='#F66A0C')


boton_e = Button(main, text="Alta", command=funcion)
boton_e.grid(row=3, column=0)

boton_s = Button(main, text="Sorpresa", command=funcionS)
boton_s.grid(row=3, column=1)





main.mainloop()

