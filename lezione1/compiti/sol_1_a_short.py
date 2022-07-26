# Compito 1
# Creare uno script di python che simuli il login ad un sito di casino.
# - si chieda all'utente: nome, cognome, ed età 

name = input("Inserisci il nome: ")
surname = input("Inserisci il cognome: ")
age = int(input("Inserisci l'etá: "))

# - si verifichi che il nome e il cognome siano più lunghi di un carattere e che l'età sia maggiore o uguale di 18 anni
# - se tutto è corretto stampare una string di conferma altrimenti comunicare l'errore all'utente
# - si consideri che l'utente fornirà sempre dati di tipo corretto


if len(name) > 1 and len(surname) > 1 and age >= 18:
    print("Access Confirmed")
    print("Welcome in", name.capitalize(), surname.capitalize())
    print(str(age), "yo is good enough. You are a big person now! Go enjoy the world")

else: 
    print("Access Denied")


# *BONUS: stampare resoconto dei dati assicurandosi che nome e cognome inizino con la maiuscola*