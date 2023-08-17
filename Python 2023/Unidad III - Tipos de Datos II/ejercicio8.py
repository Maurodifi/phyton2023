def menu():
    print("\n Elija una opción: ")
    print("    (a) Agregar producto: ")
    print("    (e) Eliminar producto: ")
    print("    (l) Listar producto: ")
    print("    (m) Modificar producto: ")
    print("    ó cualquier otra tecla para salir: ")
    global eleccion
    global valor
    eleccion = input("Ingrese la accion a realizar: ")
    if eleccion == 'a' or eleccion == "e" or eleccion == "l" or eleccion == "m":
        valor = True
    else:
        valor = False
    return valor


menu()
listadecompra = []


def alta(valor):
    total = 0
    while valor is True:
        producto, cantidad, precio = input("Ingrese nombre de producto cantidad y precio separado por espacio: ").split()
        cantidad = int(cantidad)
        precio = float(precio)
        total = total + cantidad * precio
        listadecompra.append([producto, cantidad, precio])
        eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese otra tecla: ")
        if eleccion == 'i':
            valor = True
        else:
            valor = False
    return total


def borrar():
    print("Elija que borrar")
    print(listadecompra)
    compraborrar = int(input("Ingrese el elemento que quiere eliminar: (0 para el primer elemento 1 para el primer elemento...)"))
    listadecompra.remove(listadecompra[compraborrar])
    print("El elemento ha sido eliminado ahora su lista es: ", listadecompra)


def listar():
    print(listadecompra)


def modificar():
    print(listadecompra)
    modificarelemento = int(input("que elemento de la lista quiere modificar: "))
    modificarobjeto = int(input("Indique que quiere modificar: "))
    modificacion = input("indique que valor quiere colocar: ")
    listadecompra[modificarelemento][modificarobjeto] = modificacion
    print("La lista nueva es: ",listadecompra)


print(valor)
while valor == True:
    if eleccion == "a":
       alta(valor)
    elif eleccion == "e":
        borrar()
    elif eleccion == "l":
        listar()
    elif eleccion == "m":
        modificar()
    else:
        break
    menu()
