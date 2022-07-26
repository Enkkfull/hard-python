# per rendere i nostri programmi più interattivi possiamo chiedere all'utente dei dati
# usando la funzione input()

a = input("Inserire dato: ")

# questa funzione prenderà un dato inserito dall'utente e lo assegnerà alla variabile a 

# OGNI dato preso da un input è di default una stringa. Sarà dunque necessario un casting
# se lo si vuole trattare come intero. Ad esempio:


print("La calcolatrice che fa solo le somme!")

a = input("Inserire primo intero: ")
b = input("Inserire secondo intero: ")

c = int(a) + int(b)

print("La somma è: "+str(c))

# questa è la calcolatrice più stupida del mondo che fa solo somme

# naturalmente l'utente potrebbe decide di inserire scritte a casaccio anziché un numero
# ma questo è un tema più avanzato che tratteremo in seguito.
# per ora diamo per scontato che l'utente sia gentile e non voglia distruggere il nostro povero
# programmino
