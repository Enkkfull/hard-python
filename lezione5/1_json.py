# Finiamo di parlare di file, introducendo un formato di file particolarmente utile. 


# Alcuni file di testo sono codificati in modo da essere facilmente trattati da linguaggi di programmazione sia in input che output 
# questo formato si chiama JSON (https://www.json.org/json-en.html)
# nel quale dizionari, liste, interi e stringhe sono facilmente codificati come testo
# in python è prima di tutto necessario importare il modulo json

import json

# È possibile lavorare con json sia a partire da stringhe che da file. Se lavoriamo con stringhe possiamo:

my_json_string = '{"name": "Bob", "languages": ["Python", "Java"]}'
now_its_an_object = json.loads(my_json_string) # converte una stringa in formato json in un oggetto python classico

# oppure, all'inverso

person_dict = {'name': 'Bob', 'age': 12, 'children': None }
person_json = json.dumps(person_dict) #converte un oggetto di python in un json equivalente

 
# https://www.programiz.com/python-programming/json

# La stessa cosa è possibile utilizzando direttamente dei file json.

# lettura:
with open('path_to_file/person.json', 'r') as f:
  data = json.load(f)

# scrittura
with open('path_to_file/person.json', 'w') as f:
	json.dump(data, f, indent=3)
