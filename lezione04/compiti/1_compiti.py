# Compito 01 (in live)
# Creare un programma che stampi la quarta riga di un file di testo chiamato `data\file_01.txt`. 

lines = []

with open("lezione4/data/file_01.txt", 'r') as f:
    lines = f.readlines()

print(lines[3])

