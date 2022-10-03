# Lezione 11

## Introduzione agli oggetti: definizioni e costruttore
Con la lezione undici apriamo un capitolo teorico *fondamentale*. Ricordo che quando ero giovane (anni fa) questo argomento mi ha letteralmente (ma non letteralmente) aperto il cervello e ha instillato nel mio cranio alcuni principi fondamentali del mondo della programmazione, dell'informatica e perché no della vista stessa.

Upselling much? 

Parliamo di _classi_ e _oggetti_. 

Iniziamo col dire che una classe è un costrutto della programmazione che permette di creare una definizione per delle _istanze di oggetti_. Possiamo usare la classica metafora della linea produttiva: una classe è lo stampino tramite il quale possiamo produrre (in programmatico _istanziare_) degli oggetti.

Una classe, oltre a fungere da prototipo (stampino) per generare istanze di oggetti, definisce anche intrinsecamente un tipo (come int, double, ecc) che è il tipo degli oggetti che instanziamo tramite la classe.

L'ultilità di tutto questo è una, ma fondamentale: gli _oggetti_ che generiamo sono completamente personalizzabili, poiché offrono variabili e metodi ad hoc. Pertanto, gli oggetti sono parte integrante e fondamentale di qualunque progetto "sostanzioso" dato che sono delle _strutture dati personalizzabili_, oltre che offrire funzionalità ben separate dal resto del programma. Inoltre, utilizzare gli oggetti ci da accesso all'intero meccanismo dell'ereditarietà (non quella di Amadeus) di cui però parleremo solo in seguito. Ma è potentissimo.

Siamo sicuramente confusi, ma con un esempio pratico possiamo almeno iniziare a fare chiarezza. Immaginiamo di voler creare un software che svolga il ruolo di rubrica. Sarebbe utile poter avere la rappresentazione in python di un "Contatto", che ipotizziamo abbia nome, cognome e numero di telefono. Ciascuno di questi dati costituirebbero una variabile semplice (ipoteticamente due stringhe e un intero) ma dobbiamo trovare un modo di metterli insieme in un "nucleo" unico. Una soluzione potrebbe essere quella di creare una lista di dizionari, qualcosa del tipo:

```
rubrica = [
	{"nome":"Giancarlo","cognome": "Salcarri","numero": 696969696},
 	{"nome":"Stefania","cognome": "Fava","numero": 2939923932},
	...
]
```

Questa rappresentazione ha ovvie limitazioni. Prima di tutto c'è un sacco di overhead dato dalla ripetizioni delle chiavi, inoltre, se uno desiderasse performare operazioni quali rimozione, controllo dei duplicati, ecc. una struttura poco formale come quella di un dizionario costituirebbe un problema. Senza immaginare che per rappresentazioni molto più complesse l'accesso ai dati diverrebbe sempre più complesso.

Rimane una soluzione utilizzabile per semplici casi, ma c'è bisogno di qualcosa di più potente. Gli oggetti, appunto.

In python potremmo infatti creare una classe Contatto:

```
class Contatto:
```

e metterci all'interno le variabili che definiscono un contatto, dette _variabili di classe_ o _stato_ o _proprietà_ della classe:

```
class Contatto:
	nome = ""
	cognome = ""
	numero = 0
```

Ecco il nostro stampino. È quasi pronto per iniziare a produrre contatti, abbiamo soltanto bisogno (tecnicamente no, ma ad ogni fine pratico sì) di un cosidetto _costruttore_. Un metodo speciale che istruisca come la classe deve istanziare i propri oggetti. 

Scriviamolo dunque:


```
class Contatto:
	nome = ""
	cognome = ""
	numero = 0

	def __init__(self, nome, cognome, numero):
		self.nome = nome
		self.cognome = cognome
		self.numero = numero
 
```

Eccoci! ora possiamo creare tutti i contatti che vogliamo semplicemente scrivendo (direttamente in uno script)

```
contatto_1 = Contatto("Giancarlo", "Salcarri", 696969696)
```

La variabile `contatto_1` contiene una istanza di classe `Contatto` ed è quindi di tipo `Contatto`.

Il costruttore della classe (che ha sempre lo stesso nome, `__init__`) viene invocato quando usiamo la scrittura `NOME_CLASSE()`. Al costruttore passiamo i nostri nome, cognome, numero che vengono assegnati all'interno dell'istanza di oggetto che stiamo generando. 

Questo è possibile grazie all'uso del parametro speciale `self`, che identifica la *particolare* istanza di oggetto sul quale il costruttore sta lavorando. 

Grazie alle nostre conoscenze dello stato della memoria, possiamo addirittura dire che `self` contiene il puntatore all'oggetto che sta venendo generato. 

In python è addiritura superfluo specificare le proprietà in alto nella classe, poiché queste possono essere dinamicamente aggiunte e dunque anche la scrittura è legittima (ma la sconsiglio per i neofiti). 

```
class Contatto:

	def __init__(self, nome, cognome, numero):
		self.nome = nome
		self.cognome = cognome
		self.numero = numero
 
```

Andiamo a vedere in memoria cosa succede quando eseguiamo il codice qui riportato per intero così da far chiarezza usando il solito tool [qui](https://pythontutor.com/visualize.html#code=class%20Contatto%3A%0A%0A%20%20%20%20def%20__init__%28self,%20nome,%20cognome,%20numero%29%3A%0A%20%20%20%20%20%20%20%20self.nome%20%3D%20nome%0A%20%20%20%20%20%20%20%20self.cognome%20%3D%20cognome%0A%20%20%20%20%20%20%20%20self.numero%20%3D%20numero%0A%0Acontatto_1%20%3D%20Contatto%28%22Giancarlo%22,%20%22Salcarri%22,%20696969696%29%0Acontatto_2%20%3D%20Contatto%28%22Stefania%22,%20%22Fava%22,%20932020302%29%0A%0Arubrica%20%3D%20%5Bcontatto_1,%20contatto_2%5D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).


```
class Contatto:

	def __init__(self, nome, cognome, numero):
		self.nome = nome
		self.cognome = cognome
		self.numero = numero

contatto_1 = Contatto("Giancarlo", "Salcarri", 696969696)
contatto_2 = Contatto("Stefania", "Fava", 932020302)

rubrica = [contatto_1, contatto_2]


```


## Manipolare gli oggetti: metodi di classe e accesso alle proprietà

Ok, ora siamo in grado di "produrre" (istanziare) oggetti. Ma sembra molto più complicato di fare un semplice dizionario... quali sono i vantaggi? Dobbiamo parlare di come questi oggetti possono essere letti e manipolati. 

Iniziamo col voler -ad esempio- ottenere il numero di telefono di un contatto. Possiamo semplicemente scrivere: 

```
contatto_1 = Contatto("Giancarlo", "Salcarri", 696969696)
print(contatto_1.numero)
```

Si noti l'uso del punto `.` per _accedere_ all'istanza dell'oggetto (serbata nella variabile `contatto_1`). Vi accediamo e prendiamo il valore `numero`. 

Ma possiamo fare molto di più. Infatti, possiamo anche aggiungere alla classe (il nostro stampino) le definizione di cosiddetti _metodi di classe_, i quali vengono eseguiti su una specifica istanza di oggetto (quindi col `.`). 

Se ad esempio volessimo avere una bella stampa ordinata di un contatto, potremmo aggiungere alla classe `Contatto` un metodo `stampa()`

```
class Contatto:

	def __init__(self, nome, cognome, numero):
		self.nome = nome
		self.cognome = cognome
		self.numero = numero

	def stampa(self):
		print("Nome", self.nome)
		print("Cognome", self.cognome)
		print("Numero", self.numero)

contatto_1 = Contatto("Giancarlo", "Salcarri", 696969696)

contatto_1.stampa()
```

Notiamo l'importantissima presenza del self, che permette a python di sapere su quale istanza dovrà essere eseguito il metodo stampa (indagheremo meglio guardando la memoria per il prossimo esempio). 

Possiamo anche modificare i valori interni ad una istanza. Supponiamo di voler rinominare un contatto, cambiandone il nome. Possiamo dichiarare il metodo `cambia_nome()` all'interno della classe e poi usarlo proprio per questo scopo:

```
class Contatto:

	def __init__(self, nome, cognome, numero):
		self.nome = nome
		self.cognome = cognome
		self.numero = numero

	def stampa(self):
		print("Nome", self.nome)
		print("Cognome", self.cognome)
		print("Numero", self.numero)

	def cambia_nome(self, nuovo_nome):
		self.nome = nuovo_nome

contatto_1 = Contatto("Giancarlo", "Salcarri", 696969696)

contatto_1.cambia_nome("Gian Carlo")
```

Controlliamo lo stato in memoria durante l'esecuzione, così da comprendere l'importanza del self e della nozione di istanza di oggetto [qui](https://pythontutor.com/visualize.html#code=class%20Contatto%3A%0A%0A%20%20%20%20def%20__init__%28self,%20nome,%20cognome,%20numero%29%3A%0A%20%20%20%20%20%20%20%20self.nome%20%3D%20nome%0A%20%20%20%20%20%20%20%20self.cognome%20%3D%20cognome%0A%20%20%20%20%20%20%20%20self.numero%20%3D%20numero%0A%0A%20%20%20%20def%20stampa%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22Nome%22,%20self.nome%29%0A%20%20%20%20%20%20%20%20print%28%22Cognome%22,%20self.cognome%29%0A%20%20%20%20%20%20%20%20print%28%22Numero%22,%20self.numero%29%0A%0A%20%20%20%20def%20cambia_nome%28self,%20nuovo_nome%29%3A%0A%20%20%20%20%20%20%20%20self.nome%20%3D%20nuovo_nome%0A%0Acontatto_1%20%3D%20Contatto%28%22Giancarlo%22,%20%22Salcarri%22,%20696969696%29%0A%0Acontatto_1.cambia_nome%28%22Gian%20Carlo%22%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

## Gli oggetti sono ovunque
Ora che abbiamo finalmente introdotto la nozione di oggetti possiamo finalmente comprendere alcune delle misteriose scritture che abbiamo usato in passato. Infatti, abbiamo già usato decine di volte oggetti e metodi di classe.

Ad esempio, il classico `split`:

```
x = "ciao come stai"
x_arr = x.split(" ")
```

Qui siamo al cospetto di un oggetto di tipo stringa, e `split` è un suo metodo di classe. Usiamo infatti il `.` per dire di applicare il metodo esplicitamente all'istanza di stringa che si trova in x.

Anche in questo caso abbiamo usato un oggetto senza saperlo:

```
dizionario = {"chiave":"valore"}
dizionario.keys()
```
Il metodo `keys()` è infatti un metodo della classe `PyDictObject`, che il tipo definito dalla classe che implementa i nostri cari vecchi dizionari.

Trattandosi di tipi (classi) offerti già da python, la loro inizializzazione è inusuale/ha dello zucchero sintattico che ci permette di crearli più velocemente, ma questi sono a tutti gli effetti oggetti non differenti da quelli che possiamo creare noi. OGNI volta che vediamo un `.` sappiamo che stiamo lavorando su un oggetto. 

Rimane da dire che la distinzione fra tipi primitivi e tipi non primitivi (oggetti) in python è molto nebulosa, infatti, tecnicamente _tutti_ i tipi python sono oggetti. In altri linguaggi più tipati come Java la distinzione è invece netta.

Risulta dunque più semplice pensare che in python esistono una serie di tipi (classi) built-in (interi, booleani, float, liste, tuple, dizionari, stringhe, ecc) mentre tutti gli altri derivano da librerie oppure li possiamo definire noi. Quelli built-in hanno dello zucchero sintattico che ne rendono l'istanziazione più immediata, ma di fatto sono oggetti anch'essi. Ad uso pratico, comunque, tocca fare attenzione ai puntatori. Su questo dobbiamo semplicemente ricordare che tutti gli oggetti tranne quelli numerici, booleani e stringhe sono supportati da puntatori e dobbiamo farci attenzione.

Si conclude qui la prima parte relativa agli oggetti. Ancora tanti segreti sono da svelare, ma prima dobbiamo abituarci a ragionare "ad oggetti" e fare un po' di esercizio.




