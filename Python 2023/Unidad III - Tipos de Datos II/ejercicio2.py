oracion = input("Ingrese una oracion: ")


def letrarepetida(elemento, oracion):
    veces = 0
    for i in oracion:
        if elemento == i:
            veces += 1
    return veces


print(letrarepetida("a", oracion))
