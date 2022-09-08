# Ripetere porzioni di codice è peccato. Uno dei principi fondamentali della programmazione è il cosidetto LOW COUPLING
# ossia il tentativo di tenere le parti di codice indipendenti 

# le funzioni sono porzioni di codice richiamabili da altre parti del codice. 
# sono riutilizzabili e sono contraddistinte da un nome, lista di argomenti e ritorno.

# abbiamo già usato un sacco di funzioni. Ad esempio print() e len() sono funzioni dette 
# BUILT-IN, cioè già offerte da python.


# vediamo invece come possiamo creare delle funzioni tutte nostre!

# dichiariamo una funzione du-aria (con due argomenti) chiamata la_mia_funzione

def la_mia_funzione(arg1, arg2):
    # faccio cose interessanti coi miei argomenti
    x = "qui c'è il gran risultato della computazione"
    return x # il mio ritorno
    

# alle funzioni vengono dati dei parametri che finiscono dentro i nostri argomenti,
# e una volta terminata l'elaborazione restituiscono il valore della computazione

#una funzione viene semplicemente richiamata usando il suo nome e fornendo i parametri necessari

risultato = la_mia_funzione("parametro1", "parametro2")
print(risultato) # ora risultato contiene il ritorno di la_mia_funzione

# Sia i parametri che il ritorno sono in realtà opzionali, dunque:

def una_fun():
    print("non faccio niente lmao")

# è una funzione legittima

############################################################## 

# Esistono anche altri tipi di funzioni, dette funzioni di classe o metodi. Queste non possono essere richiamate così, direttamente
# ma devono essere richiamati su una *istanza di oggetto*

# la questione si fa complicata e al momento eclissiamo sull'intero argomento, ma impariamo una definizione importante: quando una funzione è richiamata
# SU un variabile, quella funzione è in realtà un metodo di classe
# ne abbiamo usate tante! ad esempio

x = "ciao amici"
x.split()

#come si vede, benché split sia una funzione a tutti gli effetti, necessita di essere chiamata SU una variabile di tipo stringa (x in questo caso)
#e lo si nota dall'uso del punto frapposto fra il nome di metodo e il nome di variabile

# non so se parleremo mai di classi e istanze, ma questo dovrebbe bastare


##############################################################

# ci sarebbero tante cose da dire in merito alle funzioni (https://www.datacamp.com/tutorial/functions-python-tutorial qui c'è un ottimo tutorial)
# ma concentriamoci soltanto sugli argomenti per un istante.

# è possibile dare dei valori di default ad un parametro, così che quando la funzione viene chiamata non sia obbligatorio fornire un valore
# e anche usare direttamente le keyword degli argomenti per effettuare il passaggio di parametri

def funzioncina(a, b="default"):
    print("faccio cose")

#possiamo chiamare questa funzione in vari modi
funzioncina("primo parametro")
funzioncina("primo parametro", "secondo parametro")
funzioncina(b="secondo parametro", a="primo parametro")


# l'ultima cosa importante di cui dobbiamo parlare è il cosiddetto scope delle variabili: infatti una variabile non esiste ovunque e sempre, 
# ma a seconda di dove viene dichiarata avrà una sua "zona di esistenza" (detta scope, appunto).

# le variabili che dichiariamo fuori da ogni metodo sono dette globali e sono accessibili ovunque
# mentre quelle dichiarate dentro un metodo sono dette locali e scompaiono con la fine di computazione del metodo

# variabile globale `init`
init = 1

def plus(args):
  # variabile locale `total`
  total = 0
  for i in args:
    total += i
  return total
  
# Accediamo senza problemi alla variabile globale
print("this is the initialized value " + str(init))

# Questo invece non possiamo farlo
print("this is the sum " + str(total))


############################################

# ultima cosa: non si possono richiamare funzioni che non siano state dichiarate PRIMA nel codice. questo può essere un problema se
# si vuole ad esempio avere tutte le funzioni del nostro programma al fondo del file per comodità.

# si ricorre allora a questa scrittura:

def main():
  hello()
  print("This is a main function")

# questa posso metterla ovunque!
def hello():
    print("hello")
  
# Execute `main()` function 
if __name__ == '__main__':
    main()

# si definisce una funzione MAIN (ereditando l'abitudine da altri linguaggi di programmazione) che viene chiamata al lancio dello script
# controllando il valore della variabile speciale __name__, la quale assume il valore __main__ quando lo script è chiamato da riga di comando



############################################

# infine ricordiamo che dentro una funzione possiamo ovviamente richiamare altre funzioni (e addirittura sé stessa... ricorsione!)