# Compito 1
# Creare uno script di python che simuli il login ad un sito di casino.
# - si chieda all'utente: nome, cognome, ed età 

print(" - - - Login del casino - - - \n\n")

name = input("Inserisci il nome: ")
surname = input("Inserisci il cognome: ")
age = int(input("Inserisci l'etá: "))

# - si verifichi che il nome e il cognome siano più lunghi di un carattere e che l'età sia maggiore o uguale di 18 anni
# - se tutto è corretto stampare una string di conferma altrimenti comunicare l'errore all'utente
# - si consideri che l'utente fornirà sempre dati di tipo corretto

## V1 
# following all the small steps to get to the solution for the name

name_len = len(name)
surname_len = len(surname)

is_ok_name = name_len > 1
is_ok_surname = surname_len > 1

both_ok = is_ok_name and is_ok_surname 

if both_ok:
    print("Name and surname are correct")
    print("Welcome in " + name.capitalize() + " " + surname.capitalize())
else: 
    print("Name or surname are too short")

# now to the age part 

f = age >= 18

if f:
    print(str(age) + " yo is good enough. You are a big person now! Go enjoy the world")
else: 
    print("I think u need to grow up a little")

# *BONUS: stampare resoconto dei dati assicurandosi che nome e cognome inizino con la maiuscola*