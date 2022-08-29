# Hard Python

File e dettagli in merito al corso "Hard Python", presentato su Twitch da [Enkk](https://twitch.tv/Enkk) e [StudyTme](https://twitch.tv/StudyTme). Le lezioni sono ricaricate su [questa playlist Youtube](https://www.youtube.com/playlist?list=PLMP9hIwoX2DtrBeIDXggVbo49Uxr6ymxT).

Il corso si divide in due parti. La prima è una introduzione rapida al linguaggio Python, mentre la seconda costituisce il progetto vero e proprio e si andranno ad introdurre i primi rudimenti di NLP analizzando una grande collezione di Tweet.

In particolare si vuole analizzare titoli e descrizioni di articoli di giornale pubblicati su Twitter da parte delle maggiori testate giornalistiche italiane in un periodo di tre anni. Le testate considerate sono: 

- [@fattoquotidiano](https://twitter.com/fattoquotidiano)
- [@repubblica](https://twitter.com/repubblica)
- [@ilgiornale](https://twitter.com/ilgiornale)
- [@lastampa](https://twitter.com/lastampa)
- [@corriere](https://twitter.com/corriere)
- [@open_gol](https://twitter.com/open_gol)
- [@avvenire_nei](https://twitter.com/avvenire_nei)
- [@ilmessaggeroit](https://twitter.com/ilmessaggeroit)
- [@libero_official](https://twitter.com/libero_official)

Periodo considerato: dal 1 Giugno 2019 al 1 Giugno 2022. 

Ecco un esempio di Tweet:

```json
"created_at": "2022-06-18 19:25:33",
"description": "Giornata storica per l'Italia nella rassegna di Antalya. A completare il trionfo, il secondo e terzo gradino del podio per Rossella Fiamingo e Mara Navarri…",
"hashtags": [],
"id": 1538241525116567552,
"text": "Europei di scherma, tripletta maschile nel fioretto: Garozzo oro, Marini argento, Avola bronzo https://t.co/QWeIhyhVvo",
"title": "Europei di scherma, tripletta maschile nel fioretto: Garozzo oro, Marini argento, Avola bronzo",
"user": "repubblica"
```

## Note in corso d'opera
Scrivo questa parte dopo la quarta lezione. Grazie ai preziosi feedback della community le lezioni dalla quarta in poi saranno meno "pesanti" dal punto di vista teorico e di introduzione di cose, e più orientate a fare esercizi insieme. Alcuni saranno fatti live durante la lezione, mentre l'esercizio a casa sarà più semplice e meno time consuming. Inoltre il corso si espanderà (ritardando la parte di elaborazione di Twitter) volendo anche includere spiegazioni di cose teoricamente più avanzate, ma preziose anche per chi già sa programmare (anche in altri linguaggi). 

Scrivo questa parte dopo la settima lezione. Gli argomenti teorici che vorrei trattare sono ormai quasi terminati, nominalmente manca qualcosa in merito alla rappresentazione dei dati (grafici ad esempio) e il grande argomento degli oggetti/classi. Ho deciso di introdurre alcuni progetti un po' più grossi che vedremo in live mano a mano, utilizzando API di servizi utili e che potreste decidere di usare per sviluppare dei vostri progetti. Poi, finalmente, ci muoveremo verso il progetto di Twitter.


## File di supporto

Ogni lezione è contenuta in una cartella di questo github e contiene vari file numerati, uno per ogni argomento. Inoltre c'è una cartella `compiti` che contiene la consegna e le varie soluzioni implementate da Giulia (in live, durante la settimana). I compiti vengono sempre corretti nel video della lezione successiva. 

## Sulla lingua

Le lezioni sono in italiano, così come i compiti e i commenti che guidano le varie lezioni. Il codice invece è tendenzialmente in inglese dato che programmare in qualunque altra lingua è una pratica poco suggerita (il codice deve essere potenzialmente comprensibile da tutti). 

## Mini progetti 
Dalla lezione 7 iniziano dei mini progetti che durano più lezioni. Per comodità li riporto qui con le lezioni pertinenti, così da poterli consultare separatamente dal resto. 

- **Parsing wikipedia: il wikimorti dataset**: creazione di un dataset contenente tutti i morti "celebri" dal 1992 al 2021 parsificandoli da Wikipedia e studiare un po' di statistiche in merito. Lezioni #7, #8.


## Riassunto lezioni

### Lezione #1 (26/06/2022)
 
- Installazione di python e pip e Visual Studio Code.
- Stampa
- Variabili 
- Tipi di variabili (`int`, `float`, `string`, `boolean`) 
- Operatori e operandi artimetici
- Variabili boolean e espressioni booleane
- Il costrutto `if`
- Prendere dati dall'utente: funzione `input`

### Lezione #2 (03/07/2022)
 
- Correzione dei compiti
- I cicli: while
- Strutture dati: le liste
- I cicli: il for 
- Strutture dati: i dizionari

### Lezione #3 (10/07/2022)
 
- Altre strutture dati: sets e tuple
- String manipulation e stampe
- Le funzioni

### Lezione #4 (24/07/2022)

- Import e pip 
- List comprehension
- Files
- Esercizi

### Lezione #5 (31/07/2022)

- JSON
- Requests
- Exceptions
- Esercizi

### Lezione #6 (07/08/2022)

- La memoria: stack & heap (parte I)
- Indovina il musicista: un esercizio realistico

### Lezione #7 (21/08/2022)

- La memoria: stack & heap (parte II)
- Inizio progetto "Parsing Wikipedia: il wikimorti dataset"

### Lezione #8 (28/08/2022)

- Continua "Parsing Wikipedia: il wikimorti dataset" 