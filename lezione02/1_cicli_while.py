# Introduciamo ora i loop (o cicli in italiano), fondamentali per ripetere blocchi di codici. 
# I loop si possono implementare tramite while e for, iniziamo con i while

# Questa è la struttura base di un while:

condizione = True

while condizione:
    print("riga uno del blocco")
    print("riga due del blocco")


# dove condizione è una espressione booleana o un booleano, esattamente come per gli if
# il funzionamento è ovvio: finché la condizione è vera, il while continuerà ad eseguire
# il blocco di codice che gli sta sotto
# questo while in particolare dunque ciclerà all'infinito poiché la condizione è sempre vera
# dato l'assegnamento condizione = True

# È dunque pacifico che un codice sensato dovrà avere una condizione che cambia nel tempo 
# o che viene modificata direttamente dentro al while, così da poterne permettere la terminazione
# l'implementazione più ovvia di questa idea è la seguente


count = 0
while count < 10:
    print(count)
    count = count + 1 # si può scrivere anche count += 1

# count è una variabile comunemente detta "contatore" ed è un semplice intero
# che viene incrementato (aumentato di uno) ad ogni iterazione del while
# la condizione di terminazione del while controlla il valore di questo contatore
# e dopo esattamente 10 "giri" termina, poiché il contatore sarà diventato
# 10, rendendo la condizione 10 < 10 falsa (interrompendo dunque il while)
# solitamente le variabili contatori sono chiamate "i". 

# I cicli sono usatissimi e si possono usare per tante cose diverse. Ad esempio
# potremmo migliorare la soluzione del Compito 1 continuando a chiedere dati all'utente
# finché non risultano essere corretti

name = input("Insert name: ")
surname = input("Inserisci il cognome: ")
age = int(input("Inserisci l'etá: "))

while len(name) <= 1 or len(surname) <= 1 or age < 18:
    print("Something is wrong")
    name = input("Insert name: ")
    surname = input("Inserisci il cognome: ")
    age = int(input("Inserisci l'etá: "))

print("All is correct")

# qui abbiamo un while che continua appunto a chiedere input finché una qualunque delle tre 
# condizioni di "scorrettezza" dei dati
# len(name) <= 1 
# len(surname) <= 1
# age < 18
# si verifica (sono infatti in or)


