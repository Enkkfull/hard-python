# Compito 02 (in live)
# Creare una funzione che presi come parametri i path di due file (`data/file_03_1.txt` e `data/file_03_2.txt`) 
# ne generi uno (`data/file_03_3.txt`) che contenga solo le righe *comuni* fra i due file, 
# indipendentemente dalla loro posizione. 
# Nel file risultante le righe comuni dovranno apparire in ordine inverso rispetto alla loro presenza nel file `data/file_03_1.txt`.

F1_PATH = "lezione4/data/file_03_1.txt"
F2_PATH = "lezione4/data/file_03_2.txt"
F3_PATH = "lezione4/data/file_03_3.txt"

f1_list = []
f2_list = []
# f3_list = []

with open(F1_PATH, 'r') as f:
    f1_list = [word.strip("\n") for word in f.readlines()]
with open(F2_PATH, 'r') as f:
    f2_list = [word.strip("\n") for word in f.readlines()]


# for word in f1_list:
#     if word in f2_list:
#         f3_list.append(word)

# print(f3_list)
# print(len(f3_list))

f3_list = [word for word in f1_list if word in f2_list]
print(f3_list)

max_i = len(f3_list)-1
min_i = 0

# scrivi un programma che scriva tutti i numeri da 10 a 0

f3_list_reverse = []

for i in range(max_i,-1,-1):
    f3_list_reverse.append(f3_list[i])

with open(F3_PATH, 'w') as f:
    for line in f3_list_reverse:
        f.write(line)
        f.write('\n')