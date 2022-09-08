# # Compito 03 (off live)

# Creare una programma che prenda in input un file contenente due righe, ciascuna rappresentante una lista di di interi maggiori di `0`.

# Esempio di file:
# ```
# 2,1,3
# 3,1,5
# ```

# Le liste sono comma separated e di uguale lunghezza.

# Si generi dunque una matrice (una lista di liste) che abbia sulla diagonale principale la somma delle due liste e in tutte le altre posizioni `0`. Esempio:

# ```
# # sono estratte dal file
# l1 = [2,1,3]
# l2 = [3,1,5]

# Matrice risultante:

# 5 0 0
# 0 2 0 
# 0 0 8

# ```

# La matrice risultante deve essere stampata all'interno di un altro file.

# Si usino diversi metodi di supporto per organizzare appropriatamente il programma (esempio, il caricamento da file, la generazione della matrice, la stampa su file). 

with open("lezione4/data/file_02.txt", 'r') as f:
    line1 = f.readline()
    line2 = f.readline()


l1 = [int(x) for x in line1.strip("\n").split(",")]
l2 = [int(x) for x in line2.strip("\n").split(",")]
l3 = []
matrix = []


#ez solution for someone who doesnt know how to code
for i in range(len(l1)): # 0, 1, 2
  temp_list = [0] * len(l1)
  temp_list[i] = l1[i] + l2[i]
  matrix.append(temp_list)

# classic approach
matrix2 = []
for i in range(len(l1)):
	matrix2.append([0] * len(l1))
	for j in range(len(l2)):
		if i == j:
			matrix2[i][j] = l1[i] + l2[j]

print(matrix)
print(matrix2)
			
# lets just see if it works
for line in matrix:
	print(" ".join([str(x) for x in line]))

# now write into file
with open("lezione4/data/file_03.txt", 'w') as f:
	for line in matrix:
		f.write(" ".join([str(x) for x in line]))
		f.write('\n')
