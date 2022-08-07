n = input("Inserisci un numero maggiori di 10: ")

try:
	n_as_int = int(n)
	if n_as_int <= 10:
		raise Exception("Number must be bigger than 10")
except ValueError as er:
  print('Pls Insert an integer')
except Exception as ex:
  print(ex)