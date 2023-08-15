import sys
# [python ejercicio1.py 60 4 5]
i = 0
for x in sys.argv:
    i = i + 1
    if (int(sys.argv[i]) % 2 == 0):
        print("El numero es par")
    else:
        print("El numero no es par")


