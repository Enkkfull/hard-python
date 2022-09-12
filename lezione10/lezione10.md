# Lezione 8
## Parsing Wikipedia: il wikimorti dataset

*... si continua il progetto dalla lezione 8...*

Creare un semplice programma che costruisca un database (in formato json) di tutte le morti illustri dal 1992 al 2021. Salvare il file in `deadge.json`. Il database dovrà contenere: 

- Data di morte
- Nome e cognome del deceduto
- Età del deceduto

Se possibile anche altri dati relativi alla morte (laddove ci siano consistenze).

Questo database sarà poi usato nei prossimi compiti.

Ottenere questi dati utilizzando le API di Wikipedia (interrogabili tramite [questo pacchetto](https://pypi.org/project/Wikipedia-API/)). 
In particolare si osservi come sono costruite queste pagine e trovare l'algoritmo di esplorazione delle pagine più efficente ed automatizzato. Ecco alcune pagine interessanti per il compito:

- https://en.wikipedia.org/wiki/Lists_of_deaths_by_year
- https://en.wikipedia.org/wiki/1990#Deaths

----------

Una volta raccolti i dati si prepari un secondo script che calcoli qualche statistica.

Sbizzarritevi, ma ecco alcuni esempi:

- I decessi totali per mese in tutti questi anni.
- I 20 nomi più comuni fra i deceduti.
- L'età media di morte.
- Il morto più giovane.
- Il morto più vecchio.

E poi interrogarsi su questa domanda *difficile*: quanti uomini e quante donne sono morte ogni anno? Esiste un modo per stabilire se una persona è un uomo o una donna? 


Calcolare anche il numero di decessi per ogni anno, e visualizzarlo con un plot. Si fa così:

```
import matplotlib.pyplot as plt


years = ['1991', '1992', '1993']
deaths = [10, 20, 50]

plt.plot(years, deaths)
plt.suptitle('Morti per anno')
plt.show()
```


&nbsp;

