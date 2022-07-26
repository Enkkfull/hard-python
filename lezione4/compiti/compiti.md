# Lezione 04

Creare per ogni compito e ogni soluzione un file.

# Compito 01 (in live)

Creare un programma che stampi la quarta riga di un file di testo chiamato `data/file_01.txt`. 

# Compito 02 (in live)

Creare una funzione che presi come parametri i path di due file (`data/file_03_1.txt` e `data/file_03_2.txt`) ne generi uno (`data/file_03_3.txt`) che contenga solo le righe *comuni* fra i due file, indipendentemente dalla loro posizione. Nel file risultante le righe comuni dovranno apparire in ordine inverso rispetto alla loro presenza nel file `data/file_03_1.txt`.

# Compito 03 (off live)

Creare una programma che prenda in input un file contenente due righe, ciascuna rappresentante una lista di di interi maggiori di `0`.

Esempio di file:
```
2,1,3
3,1,5
```

Le liste sono comma separated e di uguale lunghezza.

Si generi dunque una matrice (una lista di liste) che abbia sulla diagonale principale la somma delle due liste e in tutte le altre posizioni `0`. Esempio:

```
# sono estratte dal file
l1 = [2,1,3]
l2 = [3,1,5]

Matrice risultante:

5 0 0
0 2 0 
0 0 8

```

La matrice risultante deve essere stampata all'interno di un altro file.

Si usino diversi metodi di supporto per organizzare appropriatamente il programma (esempio, il caricamento da file, la generazione della matrice, la stampa su file). 