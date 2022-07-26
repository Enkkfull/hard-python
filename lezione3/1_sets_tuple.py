# Per completezza, parliamo brevemente di altre due strutture dati che fanno parte delle "collections": sets e tuple

# I set sono insiemi di elementi non ordinati, i suoi elementi sono unici e immutabili

my_set = {"uno", "tre", "cinque"} 

#come tutte le altre stutture dati che abbiamo visto possiamo usare:

len(my_set)
type(my_set)
print(my_set)
"qualcosa" in my_set

# ma NON possiamo accedere direttamente ad un elemento di un set, essendo questi non indicizzati né ordinati. 

# possiamo in compenso aggiungere e rimuovere elementi:
my_set.add("nuovo elem")
my_set.remove("uno")

# ecco tutti i metodi usabili su un set: https://www.programiz.com/python-programming/methods/set




# Le tuple sono invece insieme di elementi ordinati e sono immutabili. Si dichiarano così:
# Quando si dice "ordinato" si intende che cambiando l'ordine degli elementi si ha una tupla different.
set = {5, 2, 3}
my_tuple = ("uno", "due", "tre")
l = [1, 2, 3]

# sono utili per stabilire magari tutti i valori legali di un certo input, come ad esempio: 

gender = ("Maschio", "Femmina", "Altro") 
input_gender = input("Gender:")
if input_gender not in gender:
    print("Valore non accettato")


# essendo immutabili non è possibile aggiungere o rimuovere elementi, e dispongono solo di due metodi: https://www.programiz.com/python-programming/methods/tuple


#####################################

# Con questo abbiamo introdotto tutte le strutture dati più utili in Python. 
# A questo link trovate un utile raffronto fra liste, sets, tuple e dizionari : https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python
# in ogni caso liste e dizionari sono i più usati mentre in certi casi i set risultano particolarmente utili. le tuple sono per usi molto specifici.

