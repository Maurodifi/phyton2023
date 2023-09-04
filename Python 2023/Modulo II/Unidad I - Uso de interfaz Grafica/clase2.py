from tkinter import *

main = Tk()

el_id = Label(main, text="Este es mi primer texto")
el_id.grid(row=0,column=0)
nombre = Label(main, text="Este es mi segundo texto")
nombre.grid(row=1,column=0)

entry_id = Entry(main)
entry_id.grid(row=0,column=1)
entry_nombre = Entry(main)
entry_nombre.grid(row=1,column=1)

def funcion():
    print("hola")


boton = Button(main, text="Aceptar", command=funcion)
boton.grid(row=2, column=1)


main.mainloop()
