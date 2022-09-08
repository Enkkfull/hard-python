# introduciamo ora un altra struttura dati fondamentale, i dizionari.

# i dizionari sono un INSIEME di copppie chiave-valore, ottimi per ospitare ogni sorta di dato

# un dizionario si dichiara così:

my_dic = {"name": "Enrico", "nickname": "Enkk"}

# mentre per accedere ai singoli valori, si devono usare le chiavi così come nelle liste si usavano
# gli indici:

print(my_dic["name"])  # è Enrico

# possiamo ovviamente sovrascrivere i valori allo stesso modo:

my_dic["name"] = "Giulia"

# a differenza delle liste possiamo direttamente aggiungere una coppia chiave valore senza usare l'append:

my_dic["new key"] = "new value"

# Possiamo stampare dizionari per intero, sapere il loro tipo e la loro lunghezza (la quantità di chiavi-valore)

print(my_dic)
print(type(my_dic))
print(len(my_dic))


# possiamo anche avere solo le chiavi direttamente oppure i valori:
print(my_dic.keys())
print(my_dic.values())

# possiamo sapere se una chiave esiste fra le chiavi
print("nickname" in my_dic.keys())
# o un valore fra i valori 
print("Enkk" in my_dic.values())

# si noti l'uso della keyword "in" 


# infine, possiamo ciclare su un dizionario usando la funzione items() che ci da insieme le coppie chiave-valore, che vengono
# poi scomposte in due variabili (chiamate qui key e value)
for key,value in my_dic.items():
    print(key)
    print(value)


# anche qui possiamo rimuovere una coppia chiave-valore da un dizionario:

del my_dic["name"]

# altri metodi di rimozione: https://note.nkmk.me/en/python-dict-clear-pop-popitem-del/ 


# -------------------

# dizionari e liste funzionano ovviamente anche insieme, quindi posso avere un dizionario che contiene liste. Ad esempio immaginiamo
# un utente di un social network che ha un nickname e anche una lista di amici

{"nickname": "enkk", "friends": ["adriana", "giulia", "homyatol"]}

# la chiave "friends" contiene qui una lista di amici!


