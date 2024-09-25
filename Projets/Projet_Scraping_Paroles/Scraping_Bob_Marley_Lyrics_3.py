#!/usr/bin/python3

from tinydb import TinyDB, Query
from pathlib import Path
from bs4 import BeautifulSoup
import requests
import re

DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

def get_all_urls():
  current_page = 1
  next_page = current_page + 1
  links = []

  while next_page:
  #while current_page < 2:
    r = requests.get(f"https://genius.com/api/artists/28615/songs?page={current_page}&sort=popularity")

    if r.status_code != 200:
      print("Probleme d'url")
      return []
    
    response = r.json().get("response", {})
    next_page = response.get("next_page", {})

    songs = response.get("songs")
    for song in songs:
      url = song.get("url")
      links.append(url)

    print(f"{current_page} \n")
    current_page += 1
    
    if next_page == None:
      print("No more pages to fetch !")
      break
  return links


def extract_lyrics_and_title(url):
  r = requests.get(url)

  if r.status_code != 200:
    print("Page impossible à récupérer")
    return []
  
  soup = BeautifulSoup(r.content, 'html.parser')

  title_span = soup.find("span", class_="SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj")
  title = title_span.get_text(strip=True) if title_span else "Unknown Title"

  lyrics_div = soup.find("div", class_=re.compile(r"Lyrics__Container"))
  if lyrics_div:
      lyrics = ""
      for span in lyrics_div.find_all("span"):
          lyrics += span.get_text(separator="\n") + "\n"
      return title, lyrics.strip()
  else:
      print("Lyrics not found")
      return title, ""
  

def get_all_lyrics_list():
    url_list = get_all_urls()
    title_list = []
    all_lyrics_list = []
    for url in url_list:
      title, lyrics = extract_lyrics_and_title(url)
      title_list.append(title)
      all_lyrics_list.append(lyrics)

    return title_list, all_lyrics_list

def print_clean_lyrics_list(title_list, all_lyrics_list):
  if title_list and all_lyrics_list:
    for i in range(len(title_list)):
      print(f"Title: {title_list[i]}\n")
      flat_lyrics = "".join(all_lyrics_list[i]).replace("\n\n", "\n").strip()
      print(flat_lyrics)
      print("\n" + "="*40 + "\n")
    

def get_all_lyrics_to_dict():
    url_list = get_all_urls()
    all_songs_dict = {}
    for url in url_list:
        title, lyrics = extract_lyrics_and_title(url)
        if title and lyrics:
           all_songs_dict[title] = lyrics

    save_in_db(all_songs_dict)
    return all_songs_dict

def print_clean_lyrics_dict(all_songs_dict):
   for title, lyrics in all_songs_dict.items():
      print(f"Title: {title}\n")
      print(f"Lyrics:\n\n {lyrics}")
      print("\n" + "="*40 + "\n")

def save_in_db(objet):
  if object:
    DB.insert(objet)

def fetch_song_by_title(song_title):
    Song = Query()
    result = DB.search(Song[song_title].exists())
    if result:
        return result[0][song_title]
    else:
        print(f"Song '{song_title}' not found in the database.")
        return None

# Print all songs stored in the DB
def print_all_songs_from_db():
    all_songs_from_db = DB.all()  # Fetch all records from the database
    if all_songs_from_db:
        for song in all_songs_from_db:
            print_clean_lyrics_dict(song)
    else:
        print("No songs found in the database.")

def print_song_from_db(song_title):
  song_lyrics = fetch_song_by_title(song_title)
  if song_lyrics:
      print(f"\nTitle: {song_title}\n")
      print(f"Lyrics:\n\n {song_lyrics}\n")
   


if __name__=="__main__":

  # title, all_lyrics_list = get_all_lyrics_list()
  # print_clean_lyrics_list(title, all_lyrics_list)

  # Save to DB and print all songs from memory
  all_songs_dic = get_all_lyrics_to_dict()

  # print_song_from_db("Redemption Song")

  print_all_songs_from_db()

