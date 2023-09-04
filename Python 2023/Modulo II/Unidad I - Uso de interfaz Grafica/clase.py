from tkinter import *
#creamos la ventana, dentro de esto es todo lo que hago
root = Tk()
e = Entry(root)
e.pack()

a = 4
b = 5
c = a + b
d = "mi resultado es: " + str(c)

var = IntVar()
e.config(textvariable=var)
var.set(d)
#se cierra la venta na
root.mainloop()