from dataclasses import dataclass

@dataclass
class User:
  first_name: str
  last_name: str

# equivalent à :

class User:
  def __init__(self, first_name: str, last_name: str):
    self.first_name = first_name
    self.last_name = last_name

patrick = User(first_name="Patrick", last_name="Smith")
print(repr(patrick))