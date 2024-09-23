class Voiture:
  def __init__(self, marque, vitesse, prix):
    self.marque = marque
    self.vitesse = vitesse
    self.prix = prix

  @classmethod
  def lamborghini(cls):
    return cls(marque="Lamborghini", vitesse=250, prix=200000)
  
  @classmethod
  def porshe(cls):
    return cls(marque="Porshe", vitesse=200, prix=180000)
  
lambo = Voiture.lamborghini()
print(lambo)
porshe = Voiture.porshe()
print(porshe)
print(porshe.prix)