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

  # while next_page:
  r = requests.get(f"https://genius.com/api/artists/28615/songs?page={current_page}&sort=popularity")

  # if r.status_code != 200:
  #   print("Probleme d'url")
  #   return
  
  pprint(r.json().get("response", {}))
  # response = r.json().get("response", {})
  # next_page = response.get("next_page", {})

  # songs = response.get("songs")
  # for song in songs

  # current_page += 1
  # links.append()

  # if next_page == None:
  #   print("No more pages to fetch !")
  #   break

get_all_urls()