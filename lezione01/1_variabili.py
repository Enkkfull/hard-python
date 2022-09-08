#  In Python la struttura dati base più semplice è la variabile
# le varibili ospitano un dato soltanto e ogni dato ha un tipo.

# le variabili si dichiarano usando il simbolo `=` 

# dichiariamo una variabile che si chiama a e ci mettiamo dentro
# il valore 5
a = 5

# per stampare a terminale variabili (e non solo) possiamo usare la funzione 
# built-in print(). Verrà stampato il valore dato fra parentesi

print(5)
print(a)

# per stampare a terminale il tipo di una variabile possiamo usare la funzione 
# type dentro una print

print(type(a))

# i tipi più comuni sono i seguenti:

a = 5 # numero intero, integer (int)
b = "ciao" # testo, string (str)
c = 1.5 # numero con virgola, float (float) 
d = True # tipo booleano (dettagli in merito in seguito)

# ---------------------------------------------------------

# Naturalmente le variabili possono essere combinate usando degli operatori
# Variabili numeriche usano operatori aritmetici, ad esempio

a = 5
b = 10
c = a + b # il valore di c è la somma del contenuto delle variabili a e b

# ci sono molti operatori artimetici:

c = a - b
c = a / b
c = a * b
c = a ** b # elevazione a potenza

# per le stringhe alcuni operatori aritmetici si possono riutilizzare, ad esempio

a = "ciao"
b = " come stai"
c = a + b # "ciao come stai"

# in questo caso la somma diventa concatenazione di stringhe


# Per le stringhe esistono anche altre funzioni utili, fra cui len() che da la lunghezza
# di una stringa

a = "ciao come stai"
print(len(a)) # stamperà 14

# ---------------------------------------------------------

# Fra i tipi di variabili vi sono quelle booleane. Le variabili booleane assumono
# soltanto due valori: True o False 

a = True
b = False

# le variabili booleane sono fondamentali per modificare il "flow" dei nostri programmi
# e come vedremo in seguito sono necessarie per determinare il risultato di computazioni ecc.

# anche le variabili booleane hanno i loro operatori:

c = a and b
d = a or b
e = not a

# abbiamo appena assegnato alle variabili c, d ed e delle ESPRESSIONI booleane che vengono
# valutate e restituiscono un valore booleano. In particolare: 
# a and b => è vero se e solo se sia a che b sono veri
# a or b => è vero se e solo se ALMENO uno fra a e b è vero
# not a => inverte il valore (se era True diventa False se era False diventa True)
# maggiori dettagli: https://it.wikipedia.org/wiki/Tabella_della_verit%C3%A0

# Possiamo creare espressioni booleane anche a partire da numeri, ad esempio:

a = 10 > 5 

# assegnerà ad a il valore booleano True


# ---------------------------------------------------------

# un argomento avanzato ma che possiamo toccare al volo è quello del CASTING
# come detto, le variabili hanno un tipo associato ma è possibile convertire
# variabili da un tipo all'altro usando appunto il casting. Ad esempio:

a = int("5") #casto una stringa a intero
print(type(a)) # restituirà int

# oppure 

a = str(5) #casto un intero a stringa
print(type(a)) # restituirà str





