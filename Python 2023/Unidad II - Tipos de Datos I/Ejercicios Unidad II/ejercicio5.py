valor = int(input("Ingrese un numero: "))


def funcionmax(param):
    perimetro = float(param * 2 * 3.14)
    area = float(param ** 2 * 3.14)
    valorincrementado = float(param + (param*0.10))
    return perimetro, area, valorincrementado


print("El perimetro con el numero ingresado es:", funcionmax(valor)[0])
print("El area con el numero ingresado es:", funcionmax(valor)[1])
print("El valor ingresado incrementado un 10% es:", funcionmax(valor)[2])
