films = {
  0: {"Le Seigneur des Anneaux" : 12},
  1: {"Harry Potter" : 9},
  2: {"Blade Runner" : 7.5}
}
prix = films[0]["Le Seigneur des Anneaux"] + films[2]["Blade Runner"]
print(prix)

for key in films:
  print(key, films[key])
print()

for key in films.keys():
  print(key)
print()

for value in films.values():
  print(value)
print()

for key in films.items():
  print(key)
print()

for value in films.items():
  print(value)
print()

for key, value in films.items():
  print(key, value)
print()
