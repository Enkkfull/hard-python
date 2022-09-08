# Compito 02 (in live)

# Creare un programma che chieda un intero maggiore di 10 ad un utente tramite `input` e gestisca sia l'eccezione derivante dall'inserimento di un dato che non sia un intero, sia lanci (e gestisca) una eccezione se il numero fornito non è maggiore di 10. 

n = input("Inserisci un numero maggiori di 10: ")

try:
	n_as_int = int(n)
	if n_as_int <= 10:
		raise Exception("Number must be bigger than 10")
except ValueError as er:
  print('Pls Insert an integer')
except Exception as ex:
  print(ex)