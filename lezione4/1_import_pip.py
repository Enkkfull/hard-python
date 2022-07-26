# La maggiorparte delle cose che vorrete fare sarà già stata fatta.

# Per questo motivo prima di iniziare un grande progetto conviene *sempre* googlare e trovare soluzioni altrui.

# Se siamo fortunati, parte del nostro problema non solo è già stato risolto e ne troviamo il codice, 
# ma quel codice è anche stato debitamente impacchettato, distribuito e noi dobbiamo solo *importarlo* nel codice.

# python (come ogni linguaggio di programmazione) ci permette di fare questo tramite il comando

import NOME 

# dove NOME corrisponde al modulo o pacchetto che vogliamo importare, comprensivo delle sue funzionalità. 

# Sarebbe necessario fare una distizione precisa fra moduli e pacchetti, ma per semplicità diciamo semplicemente che i pacchetti contengono multipli moduli.

# alcuni pacchetti sono già inclusi dentro python quando lo installiamo, quindi ci basterà davvero solo fare l'import per poter usare 
# le funzionalità nel nostro codice

# se invece il pacchetto dovesse essere esterno, da terminale possiamo installarlo. Ci sono tanti modi per installare pacchetti, 
# si suggerisce di usare "pip" (package installer for python), che dovreste già aver installato. 

# da terminale potete dare

# pip install nome_pacchetto

# e poi eseguire l'import senza problemi. 

# Il sito web https://pypi.org/project/pip/ offre una miriade di pacchetti, e in alto trovate il comando da dare (il nome del pacchetto necessario)

# ogni pacchetto poi presenterà le sue "istruzioni" (detta documentazione) su come usare le funzionalità.


# Le funzionalità di import non si limitano soltanto a pacchetti/moduli esterni ma possono (e devono) essere usate anche per importare le nostre funzionalità
# che magari abbiamo implentato in altri file

# se il file `uno.py` si trova nella stessa cartella del file `due.py` potremo importare il primo nel secondo usando semplicemente

# import uno

# Il tema degli import e dei packages è piuttosto complicato, quindi non ci addentriamo troppo. 
# Per poterne parlare dignitosamente dovremmo anche introdurre il concetto di oggetti e classi che per ora è troppo avanzato.

# Lascio comunque un link https://realpython.com/python-import/ che fornisce una spiegazione completa e dettagliata