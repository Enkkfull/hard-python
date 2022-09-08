# Effettuare una request e analizzare il json in`https://jsonplaceholder.typicode.com/todos`. Stampare dunque per ogni utente (le cui informazioni sono ottenibili qui `https://jsonplaceholder.typicode.com/users`) una tabella (usando PrettyTable) per ogni utente, mostrando la lista dei task e una spunta (o X) a seconda che il task sia completato o meno. 

# Esempio: 

# ```
# +-----------+------------+
# |   Marco   |    TODO    |
# +-----------+------------+
# | Lavarsi   |     X      |
# | Spesa     |     ✓      |
# |    ...    |      ...   |
# +-----------+------------+
# ```

import requests
from prettytable import PrettyTable

# work on the users
url= "https://jsonplaceholder.typicode.com/users"
users = requests.get(url).json()

# get for each user id its username
userid_to_name = {}
for user in users: 
	userid_to_name[str(user["id"])] = user["username"]

# now get the todos
url = "https://jsonplaceholder.typicode.com/todos"

todos = requests.get(url).json() # list of todos (every todo is a dictionary)

#divide todos by user 
users_todo = {} 

for todo in todos:
	name = userid_to_name[str(todo["userId"])]
	if name in users_todo.keys():
		users_todo[name].append(todo)
	else:
		users_todo[name] = [todo]

print(users_todo)

for user,todos in users_todo.items():
	p = PrettyTable()
	p.field_names = [user, "TODO"]
	for todo in todos:
		p.add_row([todo["title"], todo["completed"]])
	print(p)



