import typer

def main(delete: bool = False, extension: str = typer.Argument("txt", help="Extension à chercher")):
  """Affiche les fichiers trouvés selon l'extension donnée
  """
  print(delete)
  typer.echo(f"Recherche des fichiers avec l'extension {extension}.")


if __name__=="__main__":
  typer.run(main)

