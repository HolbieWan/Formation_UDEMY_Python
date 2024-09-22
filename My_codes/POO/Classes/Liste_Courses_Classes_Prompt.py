#!/usr/bin/python3

import sys
import os
import json
from Liste_Courses_Classes_Lignes_Commandes import Liste

nom_liste = input("\nQuelle est le nom de la liste que vous souhaitez utiliser? ")
ma_liste = Liste(nom_liste=f"{nom_liste}")

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
      print(f"{ma_liste.liste} \n")

    if choix == "2":
      article_a_retirer = input("\nQuel element de la liste souhaitez vous retirer? ")
      if article_a_retirer in ma_liste.liste:
        ma_liste.retirer(element=f"{article_a_retirer}")
      print(f"{ma_liste.liste} \n")

    if choix == "3":
      ma_liste.afficher()

    if choix == "4":
      ma_liste.effacer()
      print(f"{ma_liste.liste} \n")

    if choix == "5":
      ma_liste.enregistrer()
      print(f"Votre liste: \"{ma_liste.nom_liste}\" a bien été enregistrée\n")
      print("A plus!\n")
      sys.exit()
