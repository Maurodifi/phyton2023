from tkinter import *
from tkinter import ttk
mi_id= 0
main = Tk()

var_nombre = StringVar()
var_apellido = StringVar()


nombre = Label(main, text="Ingrese su nombre: ")
nombre.grid(row=0,column=0)
apellido = Label(main, text="Ingrese su apellido: ")
apellido.grid(row=1, column=0)

entry_nombre = Entry(main, textvariable=var_nombre)
entry_nombre.grid(row=1,column=1)
entry_apellido = Entry(main, textvariable=var_apellido)
entry_apellido.grid(row=0,column=1)


def funcion():
    global mi_id
    mi_id += 1
    tree.insert("", "end", text=str(mi_id), values=(var_nombre.get(), var_apellido.get()))


def eliminar():
    global mi_id
    item = tree.focus()
    print(item)
    print(tree.item(item))
    tree.delete(item)
    mi_id -= 1


tree = ttk.Treeview(main)
tree["columns"] = ("col1","col2","col3")
tree.column("#0", width=50, anchor=W)
tree.column("col1", width=80, anchor=W)
tree.column("col2", width=80, anchor=W)
tree.column("col3", width=100, anchor=W)

tree.grid(column=0, row=4, columnspan=4)


boton = Button(main, text="Aceptar", command=funcion)
boton.grid(row=2, column=1)
boton = Button(main, text="Borrar", command=eliminar)
boton.grid(row=3, column=1)


main.mainloop()