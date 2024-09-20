class Voiture:
  voitures_creees = 0

  def __init__(self, marque):
    self.marque = marque
    Voiture.voitures_creees += 1

voiture_01 = Voiture("Lamborghini")
voiture_02 = Voiture("Porshe")

print(voiture_01)
print(voiture_02)
print(voiture_01.marque)
print(voiture_02.marque)
print(Voiture.voitures_creees)

class Livre:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix

    def afficher_livre(self):
       print(f"{self.nom}: {self.nombre_de_pages} pages, prix: {self.prix}")

livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le Seigneur Des Anneaux", 400, 13.99)


print(f"{livre_HP.nom}: {livre_HP.nombre_de_pages} pages, prix: {livre_HP.prix}")
print(f"{livre_LOTR.nom}: {livre_LOTR.nombre_de_pages} pages, prix: {livre_LOTR.prix}")

Livre.afficher_livre(livre_HP)