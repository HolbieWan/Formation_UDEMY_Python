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

dictionnaire = {
  "prenom": "Paul",
  "nom": "Dupond",
  "prenom": "Cedric",
  "nom": "LeGrand"
  }
curseur1.execute("INSERT INTO employees VALUES (:prenom, :nom)", dictionnaire)
curseur1.execute("SELECT * FROM employees WHERE prenom=:prenom", dictionnaire)
curseur1.execute("SELECT * FROM employees")
donnees = curseur1.fetchall()
print(donnees)

connexion1.commit()
connexion1.close()