import pickle

archivo = open("archivo.pk1", "rb")
recuperar = pickle.load(archivo)
print(recuperar)