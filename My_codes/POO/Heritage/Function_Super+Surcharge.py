projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]

class Utilisateur:
  def __init__(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom

  def __str__(self):
    return f"Utilisateur {self.nom} {self.prenom}"
  
  def afficher_projets(self):
    for projet in projets:
      print(projet)

class Junior(Utilisateur):
  def __init__(self, nom, prenom):
    super().__init__(nom, prenom)   # -> equivqlent: Utilisateur.__init__(self, nom, prenom)
    
  def afficher_projets(self):
    for projet in projets:
      if not projet.startswith("pr_"):
        print(projet)


paul1 = Utilisateur("Paul", "Durand")
print(paul1)
paul1.afficher_projets()
print()
paul2 = Junior("Paul", "Durand")
print(paul2)
paul2.afficher_projets()
