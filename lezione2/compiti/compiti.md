# Lezione 02
Creare per ogni compito e ogni soluzione un file.

## Compito 1
Dichiarare due liste di numeri con cinque elementi ciascuna e creare una lista concatenata che le includa entrambe. 

*BONUS: prendere gli elementi delle due liste dall'utente chiedendoli uno per uno*

## Compito 2
Immaginiamo di dover creare un registro di utenti per un Casinò. Creare uno script che chieda da terminale i dati di `N` utenti (`N` è una variabile) e salvare ogni utente in un dizionario. I dizionari relativi ad ogni utente devono essere contenuti in una lista. Il programma deve rifiutare una inserizione (e terminare) se il nickname di uno degli utenti è già presente nel sistema. Non terminare il programma usando la funzione `exit()` ma assicurarsi che sia il flow del programma a gestire questo caso.  

I dati dell'utente sono:
- `Nickname`
- `Eta`
- `Gender` (per semplicità solo `M` o `F`)

Si dia per scontato che l'utente inserisca sempre dati coerenti (non sono da implementare i controlli di validità dei dati inseriti). 

Si cerchi di rendere l'interfaccia testuale il più comprensibile possibile, ad esempio, anziché chiedere semplicemente `Inserire nickname` si chieda `Inserire nickname per account i-esimo` dove `i` sarà naturalmente compreso fra `1` ed `N`. Aggiungere anche stampe quali `Utente i-esimo inserito!` e poi procedere con il prossimo. 

Terminato l'inserimento degli `N` utenti si stampi un resoconto. Alcuni esempi possono essere: la quantità di utenti maschi e femmine, il massimo, minimo e media di età, e la lunghezza media dei nickname. In python esistono funzioni built-in per fare queste cose: evitare di usarle e re-implementare il codice per trovare massimo, minimo e media. 

Si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione del problema, come ad esempio liste temporanee. 