# Prima di parlare dell'altra tipologia di loop (i for) introduciamo una struttura dati importantissima: le liste.
# le liste sono semplicemente una "serie" di valori, messi uno dopo l'altro. 
# i valori possono essere di qualunque tipo (anche diverso fra loro). Una lista si definisce come segue:

my_list = ["un_bel_dato", "un altro dato", 1, True, 2.4]

# La lista in questione viene messa nella variabile my_list. Possiamo:

print(my_list) # stampare la lista
print(type(my_list)) # sapere il tipo della lista (<list>)
print(len(my_list)) # sapere la lunghezza (numero di elementi) della lista


# Gli elementi di una lista sono automaticamente indicizzati da python e sono riferibili tramite il loro indice.
# quindi se volessimo stampare il secondo elemento della lista potremmo scrivere

print(my_list[1])

# Si osservi che l'indice è 1 nonostante sia il SECONDO elemento della lista. Questo perché in programmazione
# le liste e altre strutture dati sono comunemente indicizzate a partire da 0 e non da 1. Quindi per esempio nella lista:

l = ["primo", "secondo", "terzo"]

# l[0] contiene "primo"
# l[1] contiene "secondo"
# l[2] contiene "terzo"

# questa scrittura nome_lista[INDICE] può essere usata ovviamente anche per scrivere dentro le liste.

# ad esempio
l[0] = "nuovo primo"

# sovrascrive il valore "primo" sostituendolo con "nuovo primo". La lista risultante è dunque :
# ["nuovo primo", "secondo", "terzo"]

# Non è possibile riferirsi (usare l'indice) di un elemento che non esiste. Ad esempio, qui:

l = ["a", "b"]

# avremo un errore se proviamo a scrivere 

l[2] = "c"

# poiché non esiste nessun terzo elemento (indice 2) da sovrascrivere. La lista è solo lunga 2!

# dobbiamo invece ricorrere alla funzione .append() 

l.append("c")

# modificando così la lista in

l = ["a", "b", "c"]

# ora possiamo tranquillamente scrivere

print(l[2]) 

# senza temere errori


#infine possiamo anche rimuovere elementi da una lista usando la funzione
l = ["a", "b", "c"]

del l[1]

# che rimuove b dalla lista. Ci sono altre funzioni di rimozione: https://note.nkmk.me/en/python-list-clear-pop-remove-del/
