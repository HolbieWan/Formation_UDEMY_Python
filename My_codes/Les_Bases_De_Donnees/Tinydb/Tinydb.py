from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
import json

db = TinyDB("data.json", indent=4)
# db = TinyDB(storage=MemoryStorage)
# db.insert({"name": "Patrick", "score": 0})
# db.insert_multiple([
#   {"name": "Paul", "score": 34}, 
#   {"name": "Julie", "score": 120}
#   ])

User = Query()
patrick = db.search(User.name=="Patrick")
print(patrick)
patrick = db.get(User.name=="Patrick")
print(patrick)
high_score = db.search(where("score") > 0)
print(high_score)
name = db.search(where("name") == "Patrick")
print(name)
print(db.contains(User.name == "Patrick"))
print(db.contains(User.name == "patrick"))
print(db.count(User.name == "Patrick"))

db.update({"score": 10}, where("name") == "Patrick")
patrick = db.get(User.name=="Patrick")
print(patrick)

db.update({"roles": ["Junior"]})
db.update({"roles": ["Dancer"]}, where("name") == 'Patrick')
patrick = db.get(User.name=="Patrick")
print(patrick)

db.upsert({"name": "Moris", "score": 45, "roles": ["senior"]}, where("name")=="Paul") # si lélément a modifié n'existe pas alors le nouvel element est créé
moris = db.get(User.name=="Moris")
paul = db.get(User.name=="Paul")
print(moris)
print(paul)
db.remove(where("name")=="Moris")

