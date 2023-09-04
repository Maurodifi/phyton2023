import shelve


db = shelve.open('persona')
juan = db['juan']
juan = {"nombre": "Juan perez", "edad":65}
db['juan']=juan
db.close