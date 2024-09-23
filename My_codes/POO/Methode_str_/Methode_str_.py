class Voiture:
  voitures_creees = 0

  def __init__(self, marque, vitesse, prix):
    Voiture.voitures_creees += 1
    self.marque = marque
    self.vitesse = vitesse
    self.prix = prix

  def __str__(self):
    return f"Voiture de marque {self.marque} avec v.max de {self.vitesse}."

  @classmethod
  def lamborghini(cls):
    return cls(marque="Lamborghini", vitesse=250, prix=200000)
  
  @classmethod
  def porshe(cls):
    return cls(marque="Porshe", vitesse=200, prix=180000)
  
  @staticmethod
  def afficher_nombre_voitures():
    print(f"Vous avez {Voiture.voitures_creees} voitures dans votre garage")

  
  
lambo = Voiture.lamborghini()
print(lambo)    # affiche le str de l'instance a la place de la représentation en mémoire
porshe = Voiture.porshe()
print(porshe)   # affiche le str de l'instance a la place de la représentation en mémoire
print(porshe.prix)
afficher_porshe = str(porshe)
print(afficher_porshe)    # equivalent 
Voiture.afficher_nombre_voitures()