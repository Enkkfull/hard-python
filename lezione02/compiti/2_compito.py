# Immaginiamo di dover creare un registro di utenti per un Casinò. 
# Creare uno script che chieda da terminale i dati di `N` utenti (`N` è una variabile) 
# e salvare ogni utente in un dizionario. 
# I dizionari relativi ad ogni utente devono essere contenuti in una lista. 
# Il programma deve rifiutare una inserizione (e terminare) se il nickname di uno degli 
# utenti è già presente nel sistema. Non terminare il programma usando la funzione `exit()`
# ma assicurarsi che sia il flow del programma a gestire questo caso.  

# I dati dell'utente sono:
# - `Nickname`
# - `Eta`
# - `Gender` (per semplicità solo `M` o `F`)

print("--Benvenuti al GambleTme Casinó--\n\n")

n = int(input("Quanti account vuoi registrare oggi? "))
users = []
users_nicks = []

for i in range(n):
# Dobbiamo creare una lista di dizionari con all'interno i valori ddati dall'input (list > dict > input )\
    nickname = input("Inserire nickname per account {}°: ".format(i+1))

    while nickname in users_nicks:
        print("Accesso Negato. Nickname giá esistente")
        nickname = input("Inserire nickname per account {}°: ".format(i+1))
    users_nicks.append(nickname)     

    eta = int(input("Inserire l'etá dell'account {}°: ".format(i+1)))
    gender = input("Inserire il gender dell'account {}°: ".format(i+1)).capitalize()
    games = input("Inserire i giochi preferiti divisi da virgola dell'account {}°: ".format(i+1)).split(",")

    for i in range(len(games)):
        games[i] = games[i].strip()

    new_user = {"nickname" : nickname, "etá" : eta, "gender" : gender , "giochi": games}
    users.append(new_user)
    print("\n\n Utente {}° inserito! \n\n".format(i+1))

print("\n Inserimento completato! \n A seguire qualche informazione riguardo gli account creati:")
print("Hai inserito {} account.".format(len(users)))
eta = []
gender = []

for user in users:
    eta.append(user["etá"])
    gender.append(user["gender"])

gender_f = 0
for one_gender in gender:
    if one_gender == 'F':
        gender_f +=1

sum_eta = 0
for one_eta in eta:
    sum_eta += one_eta


print("L'etá media é di {:.2f} anni.".format(sum_eta/len(users)))
print("Hai inserito {} accounts di gender femminile.".format(gender_f))

# ora come feedback mostreremo il min e il max dell'etá degli users (senza le formule incluse in python)
mini= eta[0]
for x in eta:
    if x < mini:
        mini = x
print("L'etá minima é di {:.2f} anni.".format(mini))

maxi= eta[0]
for x in eta:
    if x > maxi:
        maxi = x
print("L'etá massima é di {:.2f} anni.".format(maxi))



# creare una struttura dati che contenga il numero di preferenze associato ad ogni gioco