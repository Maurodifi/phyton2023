import sys

# variable1 = input("Ingrese tres numeros separados por un espacio: ").split

print("Si el resultado de dividir por 2 es 0 entonces el numero es par")
# [python ejercicio2.py '60', '4', '5']
print(int(sys.argv[1]) % 2 == 0)
