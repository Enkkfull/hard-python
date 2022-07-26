# le liste sono il caso d'uso perfetto per introdurre i for!
# i for in python sono un po' particolari rispetto ai for di altri linguaggi di programmazione. 
# possiamo infatti pensarli come for each, ossia "per ogni". 

# i for vengono infatti tipicamente usati per "scorrere" strutture dati, e fare qualcosa PER OGNI elemento di queste strutture dati

# prima di vedere come si fanno, proviamo a usare il while che già conosciamo per stampare
# ogni elemento di una lista

my_list = ["a", "b", "c"]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


# i è il nostro contatore che continua a far ciclare il while fino a che non raggiungiamo la fine della lista.
# l'i-esimo elemento è quindi raggiunto tramite my_list[i]
# perciò, ad ogni iterazione i verrà incrementato (sarà 0, poi 1, e poi 2) e ci permetterà
# di accedere a tutta la lista
# quando i diventa 3, però, non sarà più minore di len(my_list) (che è 3) e poiché 3 < 3 è falso
# il ciclo termina

# possiamo ottenere lo stesso identico risultato con una scrittura più semplice usando un for: 

my_list = ["a", "b", "c"]
for element in my_list: 
    print(element)

# sembra quasi una frase in inglese! stiamo dicendo che per ogni ELEMENTO nella LISTA vogliamo far qualcosa.
# element è una variabile, che è l'equivalente del my_list[i] di prima. La variabile i è completamente scomparsa, 
# "nascosta" all'interno del for.

# Possiamo anche scrivere qualcosa di più simile all'implementazione col while usando la funzione range():

my_list = ["a", "b", "c"]
for i in range(len(my_list)):
    print(my_list[i])

# la funzione range crea una lista di valori, da 0 fino a len(my_list) -1. In questo caso dunque sarà una lista:
# [0, 1, 2] che sono esattamente gli indici di my_list
# ad ogni iterazione la i assume uno dei valori di quella lista (in ordine ovviamente) e quindi possiamo usare
# my_list[i] per scorrere la lista interamente.

# si ricordi che OGNI ciclo while può essere convertito in un ciclo for e viceversa. È solo questione di comodità di scrittura


# ora un piccolo esercizietto che mette insieme un bel po' di cose che abbiamo imparato:


# scrivere un programma che, date due liste di interi di uguale lunghezza ne crei una che contenga
# la somma di ogni elemento, indice per indice (quindi l'i-esimo elemento della lista somma è l'addizione fra
# l'i-esimo elemento della prima lista e della seconda)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l_sum = []

for i in range(len(l1)):
    l_sum.append(l1[i] + l2[i])

print(l_sum)

# si noti l'uso dell'append, dato che la l_sum è inizialmente vuota




