# Lezione 06

Creare per ogni compito e ogni soluzione un file.

# Compito 01 (in live)

Generare un semplice (lmao) programma-quiz che, dati due autori estratti a caso dal file `data/authors.json` li proponga all'utente domandandogli quale dei due ha pubblicato più album. Qualcosa del tipo:

```
Chi ha pubblicato più album fra 'Bello Figo' (1) e 'Queen' (2)?
```

L'utente dovrà rispondere con 1 o 2 e il sistema gli dirà se ha vinto o no. Gestire tramite eccezioni l'inserimento di un valore non corretto (né 1, né 2).

Utilizzare le [API di Deezer](https://developers.deezer.com/api/artist) per capire qual è la risposta corretta e restituire un feedback all'utente. L'API in questione richiede l'`id` dell'artista, che vi è astutamente fornito nel file `data/authors.json`.

Insieme a questo feedback, chiedere anche all'utente se vuole continuare (inserendo il carattere `Y`) oppure terminare il programma (qualunque altro carattere).

# Compito 02 (off live)

Disegnare lo stato della memoria, riga per riga, del seguente programma:

```
def doubler(l):
	for i in range(len(l)):
		l[i] = l[i]*2
	
l1 = [1,2,3]
doubler(l)

```


# Compito 03 (off live)

Modificare il Compito 1 in modo da chiedere di indovinare chi ha più fan e non chi ha più album. Aggiungere anche nuovi artisti e testare che le chiamate API funzionino.  

Per trovare l'd ID di altri artisti è necessario utilizzare l'API search di deezer. Dato che vi voglio bene ho già preparato uno script che potete modificare qui: `get_artists_ids.py`. Cambiate la lista degli artisti da cercare e copincollate il risultato della computazione nel file `data/artists.json`. Potete anche modificare lo script in modo da scrivere direttamente il json dentro `artists.json`!
