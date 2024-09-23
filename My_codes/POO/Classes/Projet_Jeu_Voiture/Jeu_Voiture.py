#!/usr/bin/python3
"""Definit une Class Voiture avec diferent attribus et Méthodes"""

class Voiture:
  """Classe qui représente une voiture
  """

  def __init__(self, essence : int = 100):
    """Methode pour initialiser une instance de Voiture

    Args:
        essence (int, optional): _Le nombre de litres d'essence_. Defaults to 100.
    """
    self.essence = essence

  def afficher_reservoir(self):
    """Methode qui affiche la quantité d'essence présente dans le réservoire
    """
    print(f"La voiture contient {self.essence} litres d'essence")

  def roule(self, km : int = 0):
    """Méthode qui simule le deplacement de la voiture et indique la quantité d'essence
      restante en fonction du nombre de km parcourus
      Prévient l'utilisateur quand le réservoir < 10l
      Prévient l'utilisateur quand le réservoir est vide

    Args:
        km (int, optional): _Nombre de km parcourus_. Defaults to 0.
    """
    consomation = (km * 5) / 100
    self.essence -= consomation

    if self.essence < 10 and self.essence > 0:
      print("Vous n'avez bientôt plus d'essence !")

    elif self.essence <= 0:
      print("Vous n'avez plus d'essence, faites le plein !")
      self.essence = 0
    
    self.afficher_reservoir()

  def faire_le_plein(self):
    """Méthode qui remet la quantité d'essence à Zéro
    et prévient l'utilisateur qu'il peut repartir
    """
    self.essence = 100
    print("Vous pouvez repartir !")
