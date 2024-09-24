import re
import string
from tinydb import TinyDB, where
from typing import List
from pathlib import Path

class User:

  DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)


  def __init__(self, first_name : str, last_name : str, phone_number: str="", address: str="", a: int =0):
    self.first_name = first_name
    self.last_name = last_name
    self.address = address
    self.phone_number = phone_number
    self.a = 5

  def __repr__(self) -> str:
    return f"User({self.first_name} {self.last_name})"

  def __str__(self):
    return f"\n{self.full_name}\nPhone_number: {self.phone_number}\naddress: {self.address}\n"

  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"
  
  @property
  def db_instance(self):
    return User.DB.get((where("first_name") == self.first_name) & (where("last_name") == self.last_name))
  
  def _check_phone_number(self):
    phone_number = re.sub(r"[+()\s]*", "", self.phone_number)   # -> \s pour les espaces, * pour signifier 0 ou plusieurs
    if len(phone_number) < 10 or not phone_number.isdigit():
      raise ValueError(f"Numéro de telephone: {self.phone_number} invalide !")
    
  def _check_names(self):
    if not self.first_name and self.last_name:
      raise ValueError("Le prénom et le nom ne peuvent pas être vides !")
    
    special_chars = string.punctuation + string.digits
    name = self.first_name + self.last_name

    for char in name:
      if char in special_chars:
        raise ValueError(f"Le nom {self.full_name} n'est pas valide !")

  def delete(self) -> List[int]:
    instance = self.db_instance
    if instance:
      return User.DB.remove(doc_ids=[self.db_instance.doc_id])
    return []

  def exists(self):
    return bool(self.db_instance)

  def _checks(self):
    self._check_names()
    self._check_phone_number()

  def save(self, validate_data: bool=False) -> int:
    if validate_data:
      self._checks()
    if self.exists():
      return -1
    else:
      return User.DB.insert(self.__dict__)
  
def get_all_users():
  return [User(**user) for user in User.DB.all()]
  # for user in User.DB.all():
  #   #User(first_name=user["first_name"], last_name=user["last_name"])
  #   or #each_user = User(**user)



if __name__=="__main__":
  from faker import Faker
  fake = Faker(locale="fr_FR")
  for _ in range(10):
    user = User(first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                address=fake.address())
    
    user._checks()
    print(repr(user))
    print(user)
    print("-" * 10)
    user.save()
    # print(get_all_users())
    # user.first_name = "Jordan"  sans utilliser @property first_name ne serait pas mis à jour à chaque instance
    #print(user.full_name) # avec la property pas besoin d'ajouter les parenthèses pour appeler la methode full_name, se comporte comme un attribut
  # print(string.punctuation)
  # print(string.digits)

  # Récupérer le dico Patrick si il existe ds la DB:
  Capucine = User(first_name="Capucine", last_name="Launay")
  print(Capucine.db_instance)
  # print(Nath.exists())
  print(Capucine.db_instance.doc_id)

  if Capucine.db_instance:
    for key, values in Capucine.db_instance.items():
      print(values)

  # Nath.delete()

