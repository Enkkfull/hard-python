# Forniamo ora alcuni utili strumenti per la manipolazione di stringhe
# metodi più specifici verranno introdotti in seguito quando e se ne avremo necessità

# È possibile fare un sacco di cose sulle stringhe. 
# listo direttamente i metodi anche se non è necessario impararli a memoria ma è prezioso sapere che esistono



##################################################

# Escaping: usando il carattere \ si possono escapare certi caratteri speciali. Ad esempio \n fa andare a capo, \t aggiunge un tab, ecc
txt = "She said \"Never let go\"."
print(txt) # She said "Never let go".

##################################################

# utilizzo della sintassi "in"
game = "Popular Nintendo Game: Mario Kart"
print("l" in game) # Prints: True
print("x" in game) # Prints: False

##################################################

# indexing: le stringhe possono essere pensate come delle speciali liste di caratteri. Possiamo quindi accedere ad un singolo carattere usando:
txt = "yellow"
txt[0] # è "y"
# non è però possibile cambiarne il valore quindi txt[0] = "c" darà errore

# secondo lo stesso principio è possibile iterare su una stringa carattere per carattere 
txt = "hello"
for c in txt:
  print(c)

# inoltre .find() restituisce l'indice di un carattere e -1 se non lo trova

txt.find("e") # 1
txt.find("a") # -1

  
##################################################

# upper(), lower(), capitalize(), title() 
# modificano le maiuscole nella stringa. 
txt = "hello MY friend"
txt.upper() # HELLO MY FRIEND
txt.lower() # hello my friend
txt.capitalize() # Hello my friend
txt.title() # Hello My Friend

##################################################

# .strip() rimuove caratteri dall'inizio e fine di una stringa
text1 = '   apples and oranges   '
text1.strip()       # => 'apples and oranges'
 
text2 = '...+...lemons and limes...-...'
 
# Si rimuove solo il carattere "." 
text2.strip('.')    # => '+...lemons and limes...-'
 
# Si rimuove sia "." che "+" 
text2.strip('.+')   # => 'lemons and limes...-'

##################################################

# .replace() rimpiazza una porzione di stringa con un altra

fruit = "Strawberry"
fruit.replace('r', 'R') # StRawbeRRy


##################################################

# .split() trasforma una stringa in una lista, separandola (splittandola) per spazio o una porzione di testo fornita

text = "Silicon Valley"
 
print(text.split())     
# Prints: ['Silicon', 'Valley']
 
print(text.split('i'))  
# Prints: ['S', 'l', 'con Valley']


# al contrario, .join() usa una porzione di testo come congiunzione per unire una lista di stringhe
x = "-".join(["Codecademy", "is", "awesome"])
 
print(x) 
# Prints: Codecademy-is-awesome

##################################################

# È possibile formattare stringhe usando il metodo .format

msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
# => 'Fred scored 3 out of 10 points.'
 
msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
# => 'Fred tickled a fluffy hamster.'

# In realtà è addirittura possibile usare la funzione print per farlo direttamente in fase di stampa
# il tema della formattazione dell'output che piace tanto ai nerd a me annoia a morte ed è concettualmente bolso
# quindi quando e se necessario useremo un po' di queste cose, 
# se vi interessa approfondite qui https://www.geeksforgeeks.org/python-output-formatting/


##################################################

# SLICING! 

# una cosa importante che si può fare in python su ogni elemento indicizzato (quindi le stringhe, ma anche le liste in generale) è lo slicing. 

# anziché fornire un indice (che tral'altro vanno anche al contrario, quindi -1 è l'ultimo elemento) si fornisce un intervallo
# di indici nella forma [start:step:stop]
# questo crea delle fettine (da cui, slicing).
# per semplicità ignoriamo il valore step (che di default è 1), e consideriamo start come il primo indice che farà parte della fetta
# e come stop il primo ESCLUSO dalla fetta. quindi l'indice di stop NON è inserito nella slice.
# ergo, [1:5] prenderà gli elementi in indice 1, 2, 3 e 4.
# se start non viene specificato si parte dal primo indice disponibile, se stop non viene definito si considera l'ultimo indice +1 (così da darci l'ultimo elemento)
# quindi [:3] fornisce una slice contenente i primi tre elementi, [3:] fornisce una slice che va dal terzo elemento fino al fondo

my_str = 'yellow'
my_str[1]     # => 'e'
my_str[-1]    # => 'w'
my_str[4:6]   # => 'ow'
my_str[:4]    # => 'yell'
my_str[-3:]   # => 'low'

# come detto funziona anche sulle liste
my_list = ["ciao", "amici", "miei", "come", "state"]

my_list[:2] # ["ciao", "amici"]
