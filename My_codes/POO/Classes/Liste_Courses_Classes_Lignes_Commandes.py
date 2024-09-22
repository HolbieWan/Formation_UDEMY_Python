#!/usr/bin/python3

import sys
import os
import json

class Liste():

  def __init__(self, nom_liste : str = "nouvelle_liste", chemin : str = "/root/Formation_UDEMY_Python/My_codes/POO/Classes/") -> None:
    self.nom_liste = nom_liste
    self.chemin = f"{chemin}{self.nom_liste}.json"
    
    if not os.path.exists(self.chemin):
      self.liste = []
      with open(self.chemin, "w") as liste:
          json.dump(self.liste, liste)
      print(f"\nLe fichier {self.chemin} a été créé\n")
    else:
        print(f"\nLe fichier {self.chemin} existe déjà\n")
        with open(self.chemin, "r") as liste:
            self.liste = json.load(liste)

  def afficher(self):
    print(f"\nVoici votre liste: \"{self.nom_liste}\":")
    for i, element in enumerate(self.liste):
      print(f"{i}. {element}")
    
  def ajouter(self, element: str = "nouvel_element"):
     self.liste.append(element)
     self.enregistrer()
     print(f"L'élément: {element} à bien été ajouté à \"{self.nom_liste}\"")
     
  def retirer(self, element: str = "element_suprime"):
     self.liste.remove(element)
     self.enregistrer()
     print(f"L'élément: {element} a bien été retiré de \"{self.nom_liste}\"")

  def effacer(self):
     self.liste.clear()
     self.enregistrer()
     print(f"La liste \"{self.nom_liste}\" a bien été effacée")

  def enregistrer(self):
    with open(self.chemin, "w") as liste:
      json.dump(self.liste, liste, indent=4)
  