#!/usr/bin/python3

import sys
import os
import json

chemin = "/root/Formation_UDEMY_Python/My_codes/liste_de_course.json"
liste_course = []

if not os.path.exists(chemin):
    with open(chemin, "w") as liste_de_course:
        json.dump(liste_course, liste_de_course)
    print(f"Le fichier {chemin} a été créé\n")
else:
    print(f"Le fichier {chemin} existe déjà\n")
    with open(chemin, "r") as liste_de_course:
        liste_course = json.load(liste_de_course)

while(1):

    choix = input("Que souhaitez-vous faire? \n\n \
        1. Ajouter un élément à la liste de courses \n \
        2. Retirer un élément de la liste de courses \n \
        3. Afficher les éléments de la liste de courses \n \
        4. Vider la liste de courses \n \
        5. Quitter le programme\n\n \
        Votre choix: ")

    if not choix.isdigit():
        print("Veuillez entrer un choix valide entre 1 et 5\n")

    if choix == "1" :
        nouvel_article = input("\nQue souhaitez-vous ajouter à la liste? \n")
        liste_course.append(nouvel_article)
        print(f"{nouvel_article} a été ajouté à la liste\n")
        print(f"{liste_course} \n")

    if choix == "2":
        delete_element = input("\nQuel element de la liste souhaitez vous retirer? \n")
        if delete_element in liste_course:
            liste_course.remove(delete_element)
            print(f"{delete_element} à été suprimé de la liste: {liste_course} \n")

    if choix == "3":
        print(f"\nVoici votre liste de course:")
        for i, element in enumerate(liste_course):
            print(f"{i}. {element}")
        print()

    if choix == "4":
        liste_course.clear()
        print("\nLa liste de course à été vidée\n")

    if choix == "5":
        print("\nA plus!\n")
        with open(chemin, "w") as liste_de_course:
            json.dump(liste_course, liste_de_course, indent=4)
        sys.exit()