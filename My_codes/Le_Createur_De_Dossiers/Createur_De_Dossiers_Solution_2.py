#!/usr/bin/python3
"""Script pour créer une structure de dossiers à partir d'un dictionnaire"""

from pathlib import Path

Chemin = Path("/root/Formation_UDEMY_Python/My_codes/Le_Createur_De_Dossiers")

Dico = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}


for key, value in Dico.items():
  Dossier_De_Sortie = Chemin / key
  Dossier_De_Sortie.mkdir(exist_ok=True)
  for i in value:
      Dossier_De_Sortie = Dossier_De_Sortie / i
      Dossier_De_Sortie.mkdir(exist_ok=True)
print("La structure de dossier a été créée")