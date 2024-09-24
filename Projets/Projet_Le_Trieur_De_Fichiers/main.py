#!/usr/bin/python3
"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

from pathlib import Path
import shutil

Dico_tri = {
  ".mp3" : "Musique",
  ".wav" : "Musique",
  ".flac" : "Musique",
  ".mov" : "Videos",
  ".avi" : "Videos",
  ".mp4" : "Videos",
  ".gif" : "Videos",
  ".webm" : "Videos",
  ".bmp" : "Images",
  ".png" : "Images",
  ".jpg" : "Images",
  ".jpeg" : "Images",
  ".css" : "Code",
  ".js" : "Code",
  ".c" : "Code",
  ".py" : "Code",
  ".html" : "Code",
  ".json" : "Code",
  ".doc" : "Documents",
  ".docx" : "Documents",
  ".txt" : "Documents",
  ".pptx" : "Documents",
  ".csv" : "Documents",
  ".xlsx" : "Documents",
  ".xls" : "Documents",
  ".odp" : "Documents",
  ".pages" : "Documents",
  ".xls"
  "Dossiers" : "Dossiers"
}

Dossier_a_trier = Path("/root/Formation_UDEMY_Python/My_codes/Createur_de_dossiers/data")
files = [f for f in Dossier_a_trier.iterdir() if f.is_file()]
dossier = [d for d in Dossier_a_trier.iterdir() if d.is_dir()]
for f in files:
  Dossier_de_sortie = Dossier_a_trier / Dico_tri.get(f.suffix, "Autres")
  Dossier_de_sortie.mkdir(exist_ok=True)
  f.rename(Dossier_de_sortie / f.name)
for d in dossier:
  Dossier_de_sortie = Dossier_a_trier / Dico_tri.get("Dossiers")
  Dossier_de_sortie.mkdir(exist_ok=True)
  shutil.move(str(d), str(Dossier_de_sortie / d.name))
  