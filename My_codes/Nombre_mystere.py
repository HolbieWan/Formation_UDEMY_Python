#!/usr/bin/python3

import random
import sys

print("\n***Le jeux du nombre mystère***")

i = 0
nombre_mystere = random.randrange(0, 101)

while(i < 5):

    if i < 4:
        print(f"\nIl te reste {5 - i} essais")

    if i == 4:
        print("\nC'est votre dernier essais: ")

    nombre_utilisateur = input("Devinez le nombre mystère (entre 0 et 100): ")

    if not nombre_utilisateur.isdigit():
        print("Veuillez entrer un nombre valide")
    else:
        nombre_utilisateur = int(nombre_utilisateur)

        if nombre_utilisateur > 100 or nombre_utilisateur < 0:
            print("Veuillez entrer un nombre compris entre 0 et 100")
            continue

        if nombre_utilisateur > nombre_mystere and i < 4:
            print(f"Le nombre mystère est inférieur à {nombre_utilisateur}")
            i += 1
            continue

        elif nombre_utilisateur < nombre_mystere and i < 4:
            print(f"Le nombre mystère est supérieur à {nombre_utilisateur}")
            i += 1
            continue

        elif nombre_utilisateur == nombre_mystere:
            print("Bravo vous avez trouvé le nombre mystère!")
            continuer = input("Souhaitez vous recommencer? Yes, No? \n")
            if continuer == "Yes" or continuer == "yes":
                i = 0
                continue
            elif continuer == "No" or continuer == "no": 
                print("A la prochaine!")
                sys.exit()
            
        elif (nombre_mystere != nombre_utilisateur) and i == 4:
            print(f"Vous avez perdu, le nombre mystère était: {nombre_mystere}")
            continuer = input("Souhaitez vous recommencer? Yes, No? \n")
            if continuer == "Yes":
                i = 0
                continue
            elif continuer == "No" or continuer == "no": 
                print("A la prochaine!\n\n")
                sys.exit()
