# lezione un po' particolare: non impariamo niente di nuovo, ma entriamo nel dettaglio delle cose che abbiamo appreso fin ora. In particolare studiamo come python tratta e interpreta il codice. 

# visualizziamo il codice in https://pythontutor.com/render.html

# parliamo di stack e heap! 

# stack è una pila sulla quale vengono messe le variabili, mentre l'heap è la zona nella quale vengono piazzati gli oggetti che sono riferiti dalle variabili tramiti puntatori (seguire la lezione su youtube per comprendere appieno questi concetti importanti)

# lascio qui sotto i pezzettini di codici che abbiamo visto in live

#################################################################################

a = 10
b = 15
c = a+b

#################################################################################

l = [1,2,"something"]
d = {"id":100, "username": "enkk"}
ld = {"id":100, "username": "enkk", "friends":["studytme", "homyatol", "trump"]}

ld["friends"].append("obama")

other_friends = ["panetty", "violet"]
ld["friends"] = other_friends

#################################################################################

l = ["a", "b", "c", "d"]

# simple loop
for i in range(len(l)):
	print(l[i])
	

# simple for each
for elem in l:
    elem = "z"


l = [["a"], ["b"], ["c"], ["d"]]

# not accessing pointer
for elem in l:
    new_elem = ["z"]
    elem = new_elem

# accessing pointer
for elem in l:
    elem[0] = "z"


