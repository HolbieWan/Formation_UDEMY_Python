#!/usr/bin/python3
"""Programme pour trier les fichiers du dossier Downloads"""

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
  ".webp" : "Images",
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
  ".dmg" : "Logiciels",
  ".pkg" : "Logiciels",
  ".pdf" : "PDF",
  "zip" : "Archives",
  "Dossiers" : "Dossiers"
}

Dossier_a_trier = Path("/Users/mjx/Downloads")
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
