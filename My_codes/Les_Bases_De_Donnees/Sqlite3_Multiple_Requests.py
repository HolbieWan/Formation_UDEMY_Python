import sqlite3

connexion1 = sqlite3.connect("database.db")
# Pour creer un tableau (Colonnnes, lignes) il faut d'aboord creer un cursor:
curseur1 = connexion1.cursor() # curseur qui va permettre d'executer nos requètes SQL

# Pour executer des requètes SQL:
curseur1.execute("""
CREATE TABLE IF NOT EXISTS employees(
          prenom text,
          nom text
)
""")

liste = [
  {"prenom": "Paul", "nom": "Dupond"},
  {"prenom": "Cedric", "nom": "LeGrand"},
  {"prenom": "Momo", "nom": "Hamed"},
  {"prenom": "George", "nom": "Clooney"},
  {"prenom": "Bob", "nom": "Marley"},
  {"prenom": "Michael", "nom": "Jackson"},
  ]

curseur1.executemany("INSERT INTO employees VALUES (:prenom, :nom)", liste)

for items in liste:
  # curseur1.execute("SELECT * FROM employees WHERE prenom=:prenom", liste)
  curseur1.execute("SELECT * FROM employees")
  
donnees = curseur1.fetchall()   # -> generateur qui ne peut etre executé que une seule fois par requete si on utilise fetchall mais autant de fois qu'il y a d'employés si on utilise fetchone!!
# employe1 = curseur1.fetchone()
# print(employe1)
# employe2 = curseur1.fetchone()
# print(employe2)
# employe3 = curseur1.fetchone()
# print(employe3)
print(set(donnees))

connexion1.commit()
connexion1.close()