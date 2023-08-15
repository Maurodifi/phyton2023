"""
Cree un programa que incorpore el módulo sys,
al cual desde la terminal se le pueda pasar tres parámetros.
El programa debe tomar los parámetros e indicar en la terminal
si son múltiplos de dos. Utilice la estructura if/else
"""
import sys
# [python ejercicio2.py '60', '4', '5']

if ((int(sys.argv[1]) % 2 == 0)):
    print("El valor uno es par")
else:
    print("El valor uno no es par")

if ((int(sys.argv[2]) % 2 == 0)):
    print("El valor dos es par")
else:
    print("El valor dos no es par")

if ((int(sys.argv[3]) % 2 == 0)):
    print("El valor tres es par")
else:
    print("El valor tres no es par")
