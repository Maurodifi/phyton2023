import datetime
edad = int(input("Ingrese su edad: "))


def añoscumplidos(edad):
    cumpleaños = datetime.datetime.now().year - int(edad)
    for x in range(cumpleaños, datetime.datetime.now().year):
        print("Cumpliste en el año: ", cumpleaños)
        cumpleaños = cumpleaños + 1


print(añoscumplidos(edad))
