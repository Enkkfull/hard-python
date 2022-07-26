# Per ora ci siamo limitati a trattare dati in input presi da linea di comando, ma naturalmente è possibile elaborare
# dati presi da file presenti sul filesystem.


# leggere il contenuto di un file da python è semplicissimo:

f = open("demofile.txt", "r")
print(f.read())

# open è una funzione che prende come parametro il path del file (percorso) e la modalità di lettura
# la funzione read legge il file per intero e lo restituisce come stringa

# è possibile anche leggere il file riga per riga

f = open("demofile.txt", "r")
for x in f:
  print(x)


# terminata l'elaborazione del file è necessario chiuderne l'accesso con la funzione

f.close()

# per semplicità è anche possibile usare la keyword `with` che ci da accesso al file e lo chiude quando finisce il suo scope

with open('readme.txt', 'w') as f:
    f.read()

# la scrittura è altrettanto semplice
lines = ['writeme', 'How to write text files in Python']
with open('writeme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


# esistono anche altre funzioni che rendono la scrittura/lettura lievemente più comoda, come readlines() e writelines() che lavorano con liste di stringhe

# ecco degli esempi

lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.writelines(lines)

lines = []
with open('readme.txt', 'r') as f:
    lines = f.readlines()

# Per sapere come trovare, definire e gestire i path dei file su vari OS: https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

