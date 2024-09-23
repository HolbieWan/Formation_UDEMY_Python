# class Vehicule:
#   def avance(self):
#     print("Le véhicule démarre")

# class Voiture(Vehicule):
#   def roule(self):
#     print("Le véhicule roule")

# class Avion(Vehicule):
#   def vol(self):
#     print("L'avion vole")

# v = Voiture()
# a = Avion()
# v.roule()
# a.vol()
# print()
# v.avance()
# a.avance()

# class Vehicule:
#   def avance(self):
#     print("Le véhicule démarre")

# class Voiture(Vehicule):
#   def avance(self):
#     print("Le véhicule roule")

# class Avion(Vehicule):
#   def avance(self):
#     print("L'avion vole")

# v = Voiture()
# a = Avion()
# v.avance()
# a.avance()

class Vehicule:
  def avance(self):
    print("Le véhicule démarre")

class Voiture(Vehicule):
  def avance(self):
    super().avance()
    print("Le véhicule roule")

class Avion(Vehicule):
  def avance(self):
    super().avance()
    print("L'avion vole")

v = Voiture()
a = Avion()
v.avance()
a.avance()