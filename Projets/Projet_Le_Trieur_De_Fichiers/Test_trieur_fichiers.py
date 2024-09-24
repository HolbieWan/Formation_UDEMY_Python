from pathlib import Path

dico_tri = {
  ".png" : "Images",
  ".jpeg" : "Images",
  ".jpg" : "Images",
  ".gif" : "Images",
  ".webp" : "Images",
  ".mp4" : "Videos",
  ".mov" : "Videos",
  "zip" : "Archives",
  ".pdf" : "Documents",
  ".txt" : "Documents",
  ".pages" : "Documents",
  ".mp3" : "Musique",
  ".wav" : "Musiques",
  ".dmg" : "Logiciels",
  ".pkg" : "Logiciels"
}

tri_directory = Path("/root/Formation_UDEMY_Python/My_codes/Downloads")
files = [f for f in tri_directory.iterdir() if f.is_file()]  # f.is_dir() pour récuperer les dossiers
for f in files:
  output_dir = tri_directory / dico_tri.get(f.suffix, "Autres")
  output_dir.mkdir(exist_ok=True)
  f.rename(output_dir / f.name)