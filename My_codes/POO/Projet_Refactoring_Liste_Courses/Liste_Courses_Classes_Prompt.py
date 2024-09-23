#!/usr/bin/python3

import logging
import sys
import os
from pathlib import Path
import json
#from Liste_Courses_Classes_Lignes_Commandes import Liste
from Liste_Courses_Classes_Lignes_Commandes_2 import Liste

# LOGGER = logging.getLogger()
BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log',
  format='%(asctime)s - %(levelname)s - %(message)s', 
  level=logging.DEBUG)

nom_liste = input("\nQuelle est le nom de la liste que vous souhaitez utiliser? ")
ma_liste = Liste(nom_liste=f"{nom_liste}")
logging.info("Création d'une instance de la Classe Liste")

while(1):
    
    liste_choix = ["1", "2", "3", "4", "5"]

    choix = input("\nQue souhaitez-vous faire?\n \
    1. Ajouter un élément à la liste de courses\n \
    2. Retirer un élément de la liste de courses\n \
    3. Afficher les éléments de la liste de courses\n \
    4. Vider la liste de courses\n \
    5. Quitter le programme\n \
    \nVotre choix: ")

    try:
      if choix not in liste_choix:
        raise ValueError
        continue
    except ValueError:
        print("Veuillez entrer un choix valide entre 1 et 5\n")

    if choix == "1" :
      nouvel_article = input("\nQue souhaitez-vous ajouter à la liste? ")
      ma_liste.ajouter(element=f"{nouvel_article}")
      logging.info("Ajout dans la liste")
      print(f"{ma_liste.liste} \n")

    if choix == "2":
      article_a_retirer = input("\nQuel element de la liste souhaitez vous retirer? ")
      ma_liste.retirer(element=f"{article_a_retirer}")
      logging.info("Suppression d'un article dans la liste")
      print(f"{ma_liste.liste} \n")

    if choix == "3":
      ma_liste.afficher()
      logging.info("Affichage de la liste")

    if choix == "4":
      ma_liste.effacer()
      logging.info("Effacement de la liste")
      print(f"{ma_liste.liste} \n")

    if choix == "5":
      ma_liste.enregistrer()
      logging.info("Enregistrement de la liste dans fichier")
      print(f"Votre liste: \"{ma_liste.nom_liste}\" a bien été enregistrée\n")
      print("A plus!\n")
      sys.exit()
