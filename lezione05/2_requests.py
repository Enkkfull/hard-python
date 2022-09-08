# Un programma ha spesso necessità di collegarsi a siti esterni per ottenere informazioni
# che poi processerà per ottenere un risultato.

# Vi sono diversi modi per farlo, ma uno dei più comuni dei recenti anni sono le cosiddette
# API REST. Le API rest ci permettono di ottenere programmaticamente dati da siti web in maniera sicura e veloce

# La comunicazione con API REST avviene attraverso il protocollo HTTP (di cui non parleremo qui)
# ma ci limitiamo a dire che si tratta una comunicazione stateless di "pacchetti di dati" le cui parti fondamentali sono head e body. Nell'head si forniscono informazioni relative al tipo di pacchetto e autorizzazioni, mentre nel body ci sono i dati effettivi. Le comunicazioni HTTP non sono tutti uguali, ma ci sono diversi metodi: GET, POST, PUT e altri. Tralasciamo comunque queste complicatezze e limitiamoci a pastrocchiare con qualche API. 

# Poiché come detto l'accesso alle API avviene col protocollo HTTP, dobbiamo effettuare una *richiesta http* in python e ciò è possibile usando le funzionalità del pacchetto requests

import requests

# https://pypi.org/project/requests/

# Le requests sono generiche richieste HTTP (le stesse che facciamo col browser), quindi ci permettono di fare di più che solo usare API web. 

# ad esempio:

response = requests.get('https://github.com')

# ci fornirà nella variabile response il sito web di github

# se però stampiamo direttamente la response otterremo soltanto un codice (200), che ci indica che la richiesta è andata a buon fine

print(response)

# possiamo accedere all'effettivo contenuto della risposta così:

print(response.content)

# gli header invece sono accessibili tramite:

print(response.headers)

##########################################################################################

# Vediamo ora come usare le request per ottenere dati da un ipotetico servizio

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.content)

# possiamo notare che la risposta a questa request è in JSON! Infatti le API REST comunicano sempre in 
# JSON, motivo per il quale è un formato così importante. Infatti, possiamo fare:

response_but_json = response.json()
print(response_but_json)

# per avere i dati forniti dal sito web in json direttamente trattabile in python
# come si vede, stiamo usando il metodo *get* delle request, quindi è una richiesta di ottenere qualcosa.
# possiamo anche - volendo - fornire noi stessi dati al gestore delle API (ad esempio potremmo voler postare un tweet su twitter via APIs). In tal caso dobbiamo ricorrere al metodo POST .post() o .put() a seconda della definizione delle API in questione

# infine, un altro tema importante: la sicurezza. Naturalmente se vogliamo postare un Tweet su Twitter o se vogliamo avere il numero di subscribers da Twitch via API, dobbiamo autenticarci. Queste informazioni non sono di dominio pubblico. L'autenticazione si può svolgere in diversi modi (alcuni anche piuttosto complessi). Uno dei modi più semplici consiste nell'avere una API KEY che deve essere inserita nell'header di ogni chiamata.

#Ecco un esempio

# definire token e url
token = "LMAO-IL-TOKENONE"
url = "URL_PER_LA_RICHIESTA"

# l'header è un dizionario!
headers = {'Authorization': "Bearer {}".format(token)}

# finalmente fare la richiesta
response = requests.get(url, headers=headers)

# il tema è complesso e ci sono moltissimi use case. Lascio qui una guida completa per chi è interessato ad approfondire: https://realpython.com/api-integration-in-python/




