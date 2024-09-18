#!/usr/bin/python3
"""Script that handles exeptions when opening a file and reading it"""

from pathlib import Path

Dir = Path("/root/Formation_UDEMY_Python/My_codes/Exo_gestion_exeptions/")

fichier_a_ouvrir = input("Entrez un fichier à ouvrir: ")
chemin_fichier_a_ouvrir = Dir / fichier_a_ouvrir

try:
  with open(chemin_fichier_a_ouvrir, "r") as fichier:
    contenu = fichier.read()
    print(contenu)

except IsADirectoryError:
  print("Il n'y pas de fichier présent, c'est un dossier!")

except FileNotFoundError:
  print("Ce nom de fichier n'existe pas dans ce dossier")

except Exception as e:
  print(f"Une erreur est survenue: {e}")

else:
  if chemin_fichier_a_ouvrir.suffix != ".txt":
    print(f"Impossible d'ouvrir le fichier: {fichier_a_ouvrir}")
    