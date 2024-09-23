from tinydb import TinyDB, Query, where

db = TinyDB("data_2.json", indent=4)

Users = db.table("Users")
Roles = db.table("Roles")

Users.insert({"name": "Patrick", "salaire": 35000})
Users.insert({"name": "Justine", "salaire": 25000})
Users.insert({"name": "Marcel", "salaire": 65000})

Roles.insert_multiple([
  {"role": "Dancer"},
  {"role": "Fascionista"},
  {"role": "Singer"}
])