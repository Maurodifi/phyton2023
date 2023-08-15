oracion = input("Ingrese una oracion: ")


def letrarepetida(elemento, oracion):
    veces = 0
    x = 0
    for i in oracion:
        while elemento:
            elemento = elemento[x]
            if elemento == i:
                veces += 1
            x += 1
    return veces


vocales = "a", "e", "i", "o", "u"
print(letrarepetida(vocales, oracion))
