while (True):
    nombre1 = input("Entrez un premier nombre : ")
    nombre2 = input("Entrez un deuxième nombre : ")

    if not (nombre1.isdigit() and nombre2.isdigit()):
        print("Veuillez entrer deux nombres valides")
        continue

    else:
        print(
            f"Le résultat de l'addition de {nombre1} avec {nombre2} est égal à {int(nombre1) + int(nombre2)}")
        break
