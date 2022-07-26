# Come anticipato i booleani sono fondamentali per cambiare il 'flow' del nostro programma
# questo è possibile tramite il costrutto 'if'

# in generale si scrive così:

# if CONDIZIONE:
    # RAMO VERO
# else: 
    # RAMO FALSO

# RAMO VERO e RAMO FALSO sono due blocchi di codice (possono essere lunghi a piacere)
# purché siano indentati di uno all'interno ripetto all'if
# la condizione invece deve essere un espressione booleana che resituisca un 
# valore booleano oppure direttamente un valore booleano. Ad esempio:

if True:
    print("ramo vero")
else: 
    print("ramo falso")

# questo if eseguirà sempre il ramo vero, poiché abbiamo inserito direttamente un valore booleano
# come condizione dell'if

# un esempio più sensato è il seguente:

a = 10
b = 15 

if a > b:
    print("a è maggiore di b")
else:
    print("a non è maggiore di b")

# il ramo else è opzionale, quindi si può anche scrivere soltanto:

if a > b:
    print("a è maggiore di b")
