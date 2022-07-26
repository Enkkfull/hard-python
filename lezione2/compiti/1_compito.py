# Dichiarare due liste di numeri con cinque elementi ciascuna e 
# creare una lista concatenata che le includa entrambe. 


# Prima, risolvo il compito senza il BONUS.

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

# Dato che Enkk é un po' puntiglioso, useremo il for per aggiungere ogni valore
# della lista 2 alla fine della lista 1

for i in l2:
    l1.append(i)

print(l1)

# Ma ció si poteva fare anche con una semplice formula:
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

l3 = l1 +l2

print(l3)

# *BONUS: prendere gli elementi delle due liste dall'utente chiedendoli uno per uno*

l1 = []
l2 = []

i = 0

while i < 5:
    a = int(input("Choose a number: "))
    l1.append(a)
    i += 1

while i < 10:
    a = int(input("Choose a number: "))
    l2.append(a)
    i += 1

print(l1)
print(l2)

for i in l2:
    l1.append(i)

print(l1)
