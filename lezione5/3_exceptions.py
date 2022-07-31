# Un programma python termina quando incontra un errore. In python vi sono due grandi famiglie di errori: syntax errors e exceptions. I primi sono errori di sintassi derivanti da un codice scritto male:

# print("ciao")) 

# c'è una parentesi di troppo, dunque otterremo un "SyntaxError: invalid syntax"

# se invece proviamo a fare 

# print(0/0) 

# non avremo errori di sintassi bensì una exception


# Python offre la possibilità di gestire le exception ed in particolare di "sollevare" le nostre exceptions e anche di catturare quelle che possono accadere durante l'esecuzione. Iniziamo a vedere come possiamo lanciare delle custom exceptions


############## GENERARE EXCEPTIONS #######################

# Diciamo di aspettarci in input un valore maggiore di cinque:

x = int(input("Inserisci un valore maggiore di 5"))
if x < 5:
    raise Exception("Ti avevo detto maggiore di cinque")

# grazie alla dicitura "raise Exception()" possiamo lanciare una nostra eccezione generica con un testo configurabile e così facendo interrompere l'esecuzione del codice


# possiamo anche fare delle asserzioni che -se riscontrate false- interromperanno l'esecuzione del programma. Ecco come farlo:

import sys
assert ('linux' in sys.platform), "This code runs on Linux only."

# in questo caso stiamo asserendo che il sistema sul quale deve girare il programma deve essere Linux. Se lo è, procederemo senza problemi, altrimenti incapperemo in una AssertionError exception

############## CATTURARE EXCEPTIONS #######################

# oltre che generare le nostre exception, abbiamo anche bisogno di catturare quelle del sistema. 
# un esempio tipico è la lettura di file che potrebbero non essere presenti sul sistema. Vediamolo.

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

# se il file 'file.log' non dovesse esistere, la funzione open lancia una FileNotFoundError exception che
# qui intercettiamo. Il blocco di codice che può produrre l'exception deve essere incluso nella 'try', mentre l'except contiene il codice che viene eseguito SE l'eccezione viene lanciata. 

# È buon costume restringere l'except al tipo esatto di eccezione che vogliamo catturare. Nel nostro caso:

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

# specificando il tipo FileNotFoundError dopo l'except e indicando che vogliamo salvarla nella variable fnf_error, possiamo direttamente stamparla e la nostra except verrà eseguita SOLO se l'exception sollevata nella try è di tipo FileNotFound. È possibile accodare più except, a seconda del tipo di exception sollevata

"""
try: 
	una_funzione_che_potrebbe_lanciare_due_tipi_di_exceptions()
except Tipo1 as error:
	print(error)
  fare_qualcosa()
except Tipo2 as error:
	print(error)
  fare_qualcosaltro()
"""

# qui a seconda del tipo di eccezione eseguiamo il metodo fare_qualcosa() o fare_qualcosaltro()


# è possibile anche specificare un blocco di codice che venga eseguito se nessuna exception è lanciata (tramite l'else) e un blocco di codice che venga eseguito indipendentemente dalle exception (magari una funzione di pulizia finale) tramite il finally. Lascio qui come sempre un riferimento completo: https://realpython.com/python-exceptions/