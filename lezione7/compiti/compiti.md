Creare per ogni compito e ogni soluzione un file.

# Compito 01 (in live)

Creare un semplice programma che costruisca un database (in formato json) di tutte le morti illustri dal 1990 al 2021. Salvare il file in `data/deadge.json`. Il database dovrà contenere: 

- Data di morte
- Nome e cognome del deceduto

Questo database sarà poi usato nei prossimi compiti.

Ottenere questi dati utilizzando le API di Wikipedia (interrogabili tramite [questo pacchetto](https://pypi.org/project/Wikipedia-API/)). 
In particolare si osservi come sono costruite queste pagine e trovare l'algoritmo di esplorazione delle pagine più efficente ed automatizzato. Ecco alcune pagine interessanti per il compito:

- https://en.wikipedia.org/wiki/Lists_of_deaths_by_year
- https://en.wikipedia.org/wiki/1990#Deaths

# Compito 02 (off live)

Integrare il database del compito precedente aggiungendo l'età di ciascun deceduto/a. Ci sono almeno due modi per farlo, uno più preciso ma complicato e l'altro più impreciso e veloce. Vi lascio l'aiuto qui sotto.


<details> 
  <summary>Dove trovo l'età?</summary>
È possibile ottenere tale informazione in maniera precisa andando alla pagina Wikipedia di ciascun morto, oppure è possibile usare la dicitura (`(b. 1905)`) che si trova nelle pagine delle morti di ciascun anno. Naturalmente in questo caso l'età potrà essere sbagliata di un anno, ma va comunque bene. Inoltre quella dicitura non è sempre disponibile.
</details>

&nbsp;

