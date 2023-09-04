import shelve

juan = {"nombre": "Juan perez", "edad": 43}
susana = {"nombre": "Susana Gomez", "edad": 44}

db = shelve.open('persona')
db['juan'] = juan
db['susana'] = susana
db.close