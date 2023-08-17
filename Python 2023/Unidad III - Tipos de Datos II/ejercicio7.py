valor = False
total = 0
eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese otra tecla: ")
if eleccion == 'i':
    valor = True
else:
    valor = False

listadecompra = {'producto': 'prueba', 'precio': 0, 'cantidad': 0}


while valor is True:
    producto, cantidad, precio = input("Ingrese nombre de producto cantidad y precio separado por espacio: ").split()
    cantidad = int(cantidad)
    precio = float(precio)
    total = total + cantidad * precio
    eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese otra tecla: ")
    listadecompra.update({'producto': producto, 'precio': precio, 'cantidad': cantidad})
    if eleccion == 'i':
        valor = True
    else:
        valor = False


print("El valor total de la compra es: ", total)
print("La compra realizada fue de: ", listadecompra)