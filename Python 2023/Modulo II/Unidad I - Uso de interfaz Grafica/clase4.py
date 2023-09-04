from tkinter.messagebox import *
from tkinter import *

master = Tk()


def funcion():
    if askyesno("Titulo de la consulta de verificacion", "contenido de la consulta"):
        showinfo("Si", "Mensaje de informacion")
    else:
        showinfo("No", "Esta a punto de salir")


def funcion2():
    showerror("Titulo de mensaje de error", "Contenido")


boton = Button(master, text="Mostrar", command=funcion)
boton.grid(row=0, column=1)
boton2 = Button(master, text="Error", command=funcion2)
boton2.grid(row=0, column=2)

master.mainloop()