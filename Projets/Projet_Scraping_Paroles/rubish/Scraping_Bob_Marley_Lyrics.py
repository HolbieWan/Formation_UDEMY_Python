from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re


def get_all_urls():

  current_page = 1
  next_page = current_page + 1
  links = []

  while next_page < 4:
    r = requests.get(f"https://genius.com/api/artists/28615/songs?page={current_page}&sort=popularity")

    if r.status_code != 200:
      print("Probleme d'url")
      return []
    
    #pprint(r.json().get("response", {}))
    response = r.json().get("response", {})
    next_page = response.get("next_page", {})

    songs = response.get("songs")
    for song in songs:   # equivalent: links.extend([song.get("url") for song in songs])
      url = song.get("url")
      links.append(url)

    current_page += 1
    print(current_page)

    if next_page == None:
      print("No more pages to fetch !")
      break

  return links
  #pprint(links)
  #print(len(links))

def extract_lyrics(url):

  lyrics_list = []
  r = requests.get(url)
  if r.status_code != 200:
    print("Page impossible à récupérer")
    return []
  #soup = BeautifulSoup(r.content, 'html.parser')
  #print(r.content)
  #lyrics = soup.find("div", class_="")
  # paragraphs = soup.find_all('p')
  # for p in paragraphs:
  #   lyrics_list.append(p.get_text())

  soup = BeautifulSoup(r.content, 'html.parser')
  lyrics_div = soup.find("div", class_=re.compile(r"Lyrics__Container"))

  if lyrics_div:
      lyrics = ""
      for span in lyrics_div.find_all("span"):
          lyrics += span.get_text(separator="\n") + "\n"
      lyrics_list.append(lyrics.strip())
      #print(lyrics.strip())
      #pprint(lyrics_list)
      return lyrics_list
     
  else:
      print("Lyrics not found")
      return lyrics_list


def get_all_lyrics():
    url_list = get_all_urls()
    
    all_lyrics_list = []
    for url in url_list:
      lyrics = extract_lyrics(url)
      # print(lyrics)
      all_lyrics_list.append(lyrics)
    return all_lyrics_list
    

def to_dict(Title : str = "Song Title", lyrics_list : list = []) -> dict:
   return {Title : [lyrics_list]}


def print_clean_lyrics(all_lyrics_list):
    for lyrics_list in all_lyrics_list:
        if lyrics_list:  # Check if lyrics_list is not empty
            # Flatten the list (if needed) and join the strings
            flat_lyrics = " ".join(lyrics_list).replace("\n\n", "\n").strip()

            print(flat_lyrics)
            print("\n" + "="*40 + "\n")


#get_all_urls()
#extract_lyrics(url="https://genius.com/Bob-marley-and-the-wailers-redemption-song-lyrics")

all_lyrics = get_all_lyrics()
print_clean_lyrics(all_lyrics)