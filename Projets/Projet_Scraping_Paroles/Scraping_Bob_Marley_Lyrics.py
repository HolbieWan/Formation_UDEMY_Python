from bs4 import BeautifulSoup
import requests
from pprint import pprint

# html_content = "<html><body><h1>Hello, BeautifulSoup!</h1></body></html>"
# soup = BeautifulSoup(html_content, 'lxml')  # Ou 'html.parser' si vous n'avez pas installé lxml
# print(soup.h1.text)

def get_all_urls():

  current_page = 1
  next_page = current_page + 1
  links = []

  while next_page < 5:
    r = requests.get(f"https://genius.com/api/artists/28615/songs?page={current_page}&sort=popularity")

    if r.status_code != 200:
      print("Probleme d'url")
      return
    
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
  
  pprint(links)
  print(len(links))
  #get_all_urls()

def extract_lyrics(url):
  lyrics_list = []
  r = requests.get(url)
  if r.status_code != 200:
    print("Page impossible à récupérer")
    return []

  soup = BeautifulSoup(r.content, 'html.parser')
  print(r.content)
  lyrics = soup.find("div", class_="ReferentFragmentmobile__Highlight-sc-1y6pdqn-1 dvKMNT")
  lyrics_list.append(lyrics)
  print(lyrics)
  print(lyrics_list)



#get_all_urls()
extract_lyrics(url="https://genius.com/Bob-marley-and-the-wailers-redemption-song-lyrics")
