valor = False
total = 0
eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese otra tecla: ")
if eleccion == 'i':
    valor = True
else:
    valor = False

while valor is True:
    cantidad = float(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    total = total + cantidad * precio
    eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese otra tecla: ")

    if eleccion == 'i':
        valor = True
    else:
        valor = False


print("El valor total de la compra es: ", total)