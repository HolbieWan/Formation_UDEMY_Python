#!/usr/bin/python3

import sys
import os
import json

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "Data/")

if not os.path.exists(DATA_DIR):
  os.makedirs(DATA_DIR)

class Liste():

  def __init__(self, nom_liste : str = "nouvelle_liste", chemin : str = DATA_DIR) -> None:
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
     if element in self.liste:
        print(f"{element} est déjà présent dans la liste")
        return False
     self.liste.append(element)
     self.enregistrer()
     print(f"L'élément: {element} à bien été ajouté à \"{self.nom_liste}\"")
     return True
     
  def retirer(self, element: str = "element_suprime"):
     if not element in self.liste:
        print(f"{element} n'est pas présent dans la liste")
        return False
     else:
        self.liste.remove(element)
        self.enregistrer()
        print(f"L'élément: {element} a bien été retiré de \"{self.nom_liste}\"")
        return True

  def effacer(self):
     self.liste.clear()
     self.enregistrer()
     print(f"La liste \"{self.nom_liste}\" a bien été effacée")
     return True

  def enregistrer(self):
    with open(self.chemin, "w") as liste:
      json.dump(self.liste, liste, indent=4)
    return True
  