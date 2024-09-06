#!/usr/bin/python3

import random

print("\n***Jeux de rôle***\n")
print("-------------------\n")

nombre_vies_utilisateur = 50
nombre_vies_adversaire = 50
nb_potions = 3

print(f"Nombre vies utilisateur: {nombre_vies_utilisateur}")
print(f"Nombre vies adversaire: {nombre_vies_adversaire}")
print(f"Nombre potions utilisateur: {nb_potions}\n")

while(nombre_vies_utilisateur > 0):

    choix_attaque_ou_potion = input("\nSouhaitez-vous attaquer(1) ou prendre une potion(2) ? ")

    if choix_attaque_ou_potion != "1" and choix_attaque_ou_potion != "2":
        print("Veuillez entrez 1 ou 2")

    points_potions = random.randrange(15, 51)
    degats_sur_ennemi = random.randrange(5, 10)
    degats_sur_utilisateur = random.randrange(5, 15)

    list_rejouer = ["Yes", "yes", "No", "no"]

    if choix_attaque_ou_potion == "1":

        points_potions = random.randrange(15, 51)
        degats_sur_ennemi = random.randrange(5, 10)
        degats_sur_utilisateur = random.randrange(5, 15)

        nombre_vies_adversaire -= degats_sur_ennemi
        print(f"Votre adversaire a perdu: {degats_sur_ennemi} vies")
        print(f"Nombre vies utilisateur: {nombre_vies_utilisateur}")
        print(f"Nombre vies adversaire: {nombre_vies_adversaire}\n")
        if nombre_vies_adversaire <= 0:
            print("Bravo, vous avez gagné!\n")
            print("-" * 50)
            rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")
            while(rejouer not in list(list_rejouer)):
                print("Veuiller taper yes or no")
                rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")

            if rejouer == "Yes" or rejouer == "yes":
                nombre_vies_utilisateur = 50
                nombre_vies_adversaire = 50
                nb_potions = 3
                continue
            else:
                print("\nA plus beau goss!\n")
                break
        print("-" * 50)

        print("Votre adversaire joue: ")
        nombre_vies_utilisateur -= degats_sur_utilisateur
        print(f"Vous avez perdu: {degats_sur_utilisateur} vies")
        print(f"Nombre vies utilisateur: {nombre_vies_utilisateur}")
        print(f"Nombre vies adversaire: {nombre_vies_adversaire}\n")
        if nombre_vies_utilisateur <= 0:
            print("T'as perdu looser!\n")
            rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")
            while(rejouer not in list(list_rejouer)):
                print("Veuiller taper yes or no")
                rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")

            if rejouer == "Yes" or rejouer == "yes":
                nombre_vies_utilisateur = 50
                nombre_vies_adversaire = 50
                nb_potions = 3
                continue
            else:
                print("\nA plus beau goss!\n")
                break
        print("-" * 50)
        continue

    if choix_attaque_ou_potion== "2":

        points_potions = random.randrange(15, 51)
        degats_sur_ennemi = random.randrange(5, 10)
        degats_sur_utilisateur = random.randrange(5, 15)

        if nb_potions == 0:
            print("Vous n'avez plus de potion, vous devez attaquer!\n")
            continue

        nombre_vies_utilisateur += points_potions
        nb_potions -= 1

        print(f"Vous avez récupéré: {points_potions} vies")
        print("Vous sautez le prochain tour")
        print(f"Nombre vies utilisateur: {nombre_vies_utilisateur}")
        print(f"Nombre vies adversaire: {nombre_vies_adversaire}\n")

        print("Votre adversaire joue:")
        nombre_vies_utilisateur -= degats_sur_utilisateur
        print(f"Vous avez perdu: {degats_sur_utilisateur} vies")
        print(f"Nombre vies utilisateur: {nombre_vies_utilisateur}")
        print(f"Nombre vies adversaire: {nombre_vies_adversaire}\n")
        if nombre_vies_utilisateur <= 0:
            print("T'as perdu looser!\n")
            rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")
            while(rejouer not in list(list_rejouer)):
                print("Veuiller taper yes or no")
                rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")

            if rejouer == "Yes" or rejouer == "yes":
                nombre_vies_utilisateur = 50
                nombre_vies_adversaire = 50
                nb_potions = 3
                continue
            else:
                print("\nA plus beau goss!\n")
                break
        print("-" * 50)

        print("Votre adversaire re-joue: ")
        degats_sur_utilisateur = random.randrange(5, 15)
        nombre_vies_utilisateur -= degats_sur_utilisateur
        print(f"Vous avez perdu: {degats_sur_utilisateur} vies")
        print(f"Nombre vies utilisateur: {nombre_vies_utilisateur}")
        print(f"Nombre vies adversaire: {nombre_vies_adversaire}\n")
        if nombre_vies_utilisateur <= 0:
            print("T'as perdu looser!\n")
            rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")
            while(rejouer not in list(list_rejouer)):
                print("Veuiller taper yes or no")
                rejouer = input("Souhaitez vous faire une autre partie? Yes, No? \n")

            if rejouer == "Yes" or rejouer == "yes":
                nombre_vies_utilisateur = 50
                nombre_vies_adversaire = 50
                nb_potions = 3
                continue
            else:
                print("\nA plus beau goss!\n")
                break
        print("-" * 50)
        continue




