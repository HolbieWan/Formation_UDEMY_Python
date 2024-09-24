#!/usr/bin/python3
"""Script pour trier le contenue d'un ficher"""

from pathlib import Path

Chemin = Path("/root/Formation_UDEMY_Python/My_codes/Organiser_Des_Donnees/prenoms.txt")
Chemin_nouveau_fichier = Path("/root/Formation_UDEMY_Python/My_codes/Organiser_Des_Donnees/prenoms_tries.txt")

with open(Chemin, "r") as fichier_txt:
  contenu = fichier_txt.read()

liste_nom = contenu.split()
liste_nom_nettoyee = [prenom.strip(",. ") for prenom in liste_nom]
liste_nom_nettoyee.sort()

with open(Chemin_nouveau_fichier, "w") as saving_file:
  for element in liste_nom_nettoyee:
    saving_file.write(element)
    saving_file.write("\n")
    # = saving_fil.write(element + "\n")
