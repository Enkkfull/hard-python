# Compito 01 (in live)

# Creare un programma che stampi tutte le mail degli utenti nel file `data/01_data.json`.
import json 

with open('lezione5/data/01_data.json', 'r') as f:
  file = json.load(f)

# ""
# print all emails
for di in file:
  print(di["email"])

# print number of friends of element that has this email: 
email = "hollandoliver@electonic.com"
for di in file:
  if di["email"] == email:
    print(len(di["friends"]))

