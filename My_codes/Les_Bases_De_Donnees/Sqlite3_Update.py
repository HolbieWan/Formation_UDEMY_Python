import sqlite3

connexion1 = sqlite3.connect("database.db")
curseur1 = connexion1.cursor() 

# Create the table
curseur1.execute("""
CREATE TABLE IF NOT EXISTS employees(
          prenom text,
          nom text,
          salaire int
)
""")

dico_insert = {
  "prenom": "Paul",
  "nom": "Dupond",
  "salaire": 10000
}
curseur1.execute("INSERT INTO employees (prenom, nom, salaire) VALUES (:prenom, :nom, :salaire)", dico_insert)

# Update the salary
dico_update = {
  "salaire": 20000,
  "prenom": "Paul",
  "nom": "Dupond"
}
curseur1.execute("UPDATE employees SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom", dico_update)

# Fetch and print the updated data
curseur1.execute("SELECT * FROM employees")
donnees = curseur1.fetchall()
print(set(donnees))

# curseur1.execute("DELETE FROM employees")   -> efface tout
curseur1.execute("DELETE FROM employees WHERE prenom='Paul'")
donnees = curseur1.fetchall()
print(set(donnees))

connexion1.commit()
connexion1.close()