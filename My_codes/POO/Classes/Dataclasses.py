from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
  first_name: str = "Michel"
  last_name: str = ""

  C: ClassVar[int]

  def __post_init__(self):
    self.full_name = f"{self.first_name} {self.last_name}"

# equivalent à :

# class User:
#   def __init__(self, first_name: str, last_name: str):
#     self.first_name = first_name
#     self.last_name = last_name

user = User()
print(user.__dict__)
print(User.__dict__)
print(user.first_name, user.last_name)
print(user.full_name)

patrick = User(first_name="Patrick", last_name="Smith")
print(repr(patrick))
print(patrick.first_name, patrick.last_name)
