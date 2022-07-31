# Lezione 05

Creare per ogni compito e ogni soluzione un file.

# Compito 01 (in live)

Creare un programma che stampi tutte le mail degli utenti nel file `data/01_data.json`.

# Compito 02 (in live)

Creare un programma che chieda un numero maggiore di 10 ad un utente tramite `input` e gestisca sia l'eccezione derivante dall'inserimento di un dato che non sia un numero, sia lanci (e gestisca) una eccezione se il numero fornito non è maggiore di 10. 

# Compito 03 (in live)

Effettuare una request e analizzare il json in`https://jsonplaceholder.typicode.com/todos`. Stampare dunque per ogni utente (le cui informazioni sono ottenibili qui `https://jsonplaceholder.typicode.com/users`) una tabella (usando PrettyTable) per ogni utente, mostrando la lista dei task e una spunta (o X) a seconda che il task sia completato o meno. 

Esempio: 

```
+-----------+------------+
|   Marco   |    TODO    |
+-----------+------------+
| Lavarsi   |     X      |
| Spesa     |     ✓      |
|    ...    |      ...   |
+-----------+------------+
```

# Compito 03 (off live)
Creare un semplice sistema che fornisce la temperatura attuale in una provincia italiana richiesta dall'utente. 

Venga dunque richiesta ad un utente tramite `input` una provincia italiana e tramite le API di [Open Meteo](https://open-meteo.com/en/docs) ottenere la temperatura e temperatura percepita attuale e stamparle. C'è solo un problema: Open Meteo richiede di fornire latitudine e longitudine e non il nome della provincia. Nel file `data/province.json` potete trovare le latitudini e longitudini di ogni provincia.

Altri dettagli:
- Se l'input utente non è una provincia, lanciare una eccezione e raccoglierla terminando il programma fornendo un feedback all'utente (qualcosa tipo "Pronvincia non trovata").
- Siete invitati a leggere la documentazione di Open Meteo per capire qual è la chiamata giusta da fare e capire autonomamente come interpretare i dati per trovare la corretta temperatura. Queste API sono un po' ostiche, per gli sviluppatori neofiti suggerisco di leggere la soluzione riportata qui sotto. In ogni caso sarà necessario usare la libreria `datetime` che non abbiamo mai usato per ottenere l'ora attuale, necessaria per estrarre la temperatura corrente. Si ottiene così:

```
import datetime

# restituisce l'ora attuale come stringa. 
# Esempio: 12 se sono le 12.15, 15 se sono le 15.46, ecc.
hours = datetime.datetime.now().strftime("%H")


```


<details> 
  <summary>Qual è la call da fare?</summary>
   L'URL da usare è il seguente: https://api.open-meteo.com/v1/forecast?&hourly=temperature_2m,apparent_temperature&timezone=Europe/Rome&latitude=X&longitude=Y con X e Y da prendere nel file province.json a seconda della provincia richiesta. 	
</details>
<details> 
  <summary>Come interpreto la risposta della call?</summary>
	   I dati utili per il nostro scopo si trovano nei campi `temperature_2m` e `apparent_temperature`. Queste sono due liste che contengono tutte le rilevazioni e previsioni di sei giorni totali a partire dalla mezzanotte del giorno corrente. Se ne deduce che la temperatura attuale sarà l'i-esimo elemento della lista, dove i è l'ora attuale. In altre parole, se sono le 12:15, la temperatura sarà il 12-esimo elemento della lista (quella delle ore 12:00). Usare la libreria datetime come descritto sopra per ottenere l'ora attuale e dunque impiegarla come indice negli array di `apparent_temperature` e `temperature_2m` per avere le temperature.
</details>

&nbsp;
