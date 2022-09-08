
import requests 
import json
import random

def get_albums(artistid): 
  a_url = "https://api.deezer.com/artist/{}".format(artistid)
  response = requests.get(a_url)
  response_json = response.json()
  a_album = response_json["nb_album"]
  return a_album

def get_fans(artistid):
  a_url = "https://api.deezer.com/artist/{}".format(artistid)
  response = requests.get(a_url)
  response_json = response.json()
  nb_fan = response_json["nb_fan"]
  return nb_fan

	
with open("lezione6/data/artists.json", "r") as f:
	artists_dic = json.load(f)
	artists_name = artists_dic.keys()
keep_asking = "Y"

while keep_asking.upper() == "Y":
	# estrarre autori a caso 
  two_artists_fan = random.sample(artists_name, 2)
  
  # creare input chiedendo 2 autori 
  user_answer = input("Who has the most fans between '{}' (1) and '{}' (2)?\n".format(two_artists_fan[0], two_artists_fan[1]))

  # limitare le risposte con exception
  if user_answer not in ["1", "2"]:
    raise Exception("Risposta non accettata.") 
  
  	
  # accedere api e ricavare i dati per i due artisti
  # ricavo il numero di album dell'artista 1
  artist1id = artists_dic[two_artists_fan[0]]
  artist2id = artists_dic[two_artists_fan[1]]
  
  a1_fans = get_fans(artist1id)
  a2_fans = get_fans(artist2id)
  
  # confrontare i valori e trovare la risposta giusta
  solution = "1" if a1_fans > a2_fans else "2"
  # confrontare la risposta giusta a quella dell'utente
  # dare esito e chiedere se andare avanti
  
  sol_feedback = "Correct!" if solution == user_answer else "Not correct!"
  
  sol_feedback += f" {two_artists_fan[0]} has {a1_fans} fans, while {two_artists_fan[1]} has {a2_fans} fans. Wanna continue? (Y)\n"
  
  keep_asking = input(sol_feedback)
