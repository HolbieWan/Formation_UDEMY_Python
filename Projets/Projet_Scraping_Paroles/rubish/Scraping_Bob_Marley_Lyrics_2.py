from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re

def get_all_urls():

  current_page = 1
  next_page = current_page + 1
  links = []

  while current_page < 2:
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
    
    all_lyrics_list = []
    for url in url_list:
      lyrics = extract_lyrics_and_title(url)
      # print(lyrics)
      all_lyrics_list.append(lyrics)

    return all_lyrics_list
    

def get_all_lyrics_to_dict():
    url_list = get_all_urls()
    all_songs_dict = {}
    for url in url_list:
        title, lyrics = extract_lyrics_and_title(url)
        if title and lyrics:
           all_songs_dict[title] = lyrics

    return all_songs_dict

def print_clean_lyrics_dict(all_songs_dict):
   for title, lyrics in all_songs_dict.items():
      print(f"Title: {title}\n")
      print(f"Lyrics:\n\n {lyrics}")
      print("\n" + "="*40 + "\n")
   

def print_clean_lyrics_list(all_lyrics_list):
    for lyrics_list in all_lyrics_list:
        if lyrics_list:  # Check if lyrics_list is not empty
            # Flatten the list (if needed) and join the strings
            flat_lyrics = " ".join(lyrics_list).replace("\n\n", "\n").strip()

            print(flat_lyrics)
            print("\n" + "="*40 + "\n")


#all_songs_dic = get_all_lyrics_to_dict()
#print_clean_lyrics_dict(all_songs_dic)

all_lyrics_list = get_all_lyrics_list()
print_clean_lyrics_list(all_lyrics_list)