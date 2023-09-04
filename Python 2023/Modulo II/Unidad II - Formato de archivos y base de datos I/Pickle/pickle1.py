import pickle

diccionario = {'id':1, 'nombre':'Anna'}
archivo = open("Archivo.pk1", "wb")
pickle.dump(diccionario, archivo)
archivo.close
