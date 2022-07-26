# Le liste sono una struttura dati usatissima per fare un sacco di cose. 
# Capita dunque molto spesso di dover scorrere una lista soltanto per verificare una condizione, o prendere un elemento, ecc.

# Per questo motivo python offre uno zucchero sintattico chiamato list comprehension (LC in breve) che permette di creare una nuova lista 
# a partere da una esistente in maniera più rapida (dal punto di vista sintattico) e leggibile.

# Vediamo subito un esempio. Diciamo di avere una lista di frutti e voler prendere tutti quelli che contengono la lettera 'a'. 
# Con le nozioni che abbiamo, dovremmo scrivere:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# ma usando invece le LC:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] # questa è la list comprehension

print(newlist)

# il for è stato ridotto ad una riga sola, ed è anche più leggibile!

# la sintassi generica di una LC è la seguente:

"""
newlist = [expression for item in iterable if condition]
"""

# dove: 
# - newlist è la variabile che contiene la nuova lista
# - iterable è la lista (in realtà una qualunqe struttura dati iterabile) dalla quale partiamo
# - item è il singolo elemento della lista
# - condition è la condizione che viene testata, ed è opzionale
# - expression è una espressione che produrrà il nuovo elemento che verrà inserito in newlist

# vediamo un po' di esempi:

newlist = [x for x in fruits if x != "apple"] # prende solo gli elementi che non sono apple

newlist = [x for x in fruits] # prende ogni x nella lista, senza condizione. quindi li prende tutti e di fatto duplica la lista di partenza

newlist = [x for x in range(10)] # lista di valori da 0 a 9

newlist = [x for x in range(10) if x < 5] # come sopra, ma i valori accettati sono solo quelli minori di 5


# come accennato l'expression può contenere delle manipolazioni prima di fornire l'elemento che farà parte della nuova lista

newlist = [x.upper() for x in fruits] # tutti i frutti in maiuscolo

# possiamo anche creare cose più complicate, come ad esempio:

newlist = [x if x != "banana" else "orange" for x in fruits]

# che significa resitutisci il frutto se questo non è banana, altrimenti restituisci orange



# Le comprehension non esistono solo per le liste, ma anche per altre collezioni. 
# Per semplicità non le introduciamo, ma qui ci sono degli esempi: https://www.geeksforgeeks.org/comprehensions-in-python/ 




 





