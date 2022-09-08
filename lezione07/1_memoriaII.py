# Andiamo avanti con la visualizzazione dello stato in memoria durante l'esecuzione di codice python. Ricordo che facciamo uso del tool https://pythontutor.com/render.html
 
#################################################################################

# look at the parameters!
def sommetta(a,b):
	c = a+b
	a = 100
	b = 150
	return c

a = 10
b = 15
c = sommetta(a,b)

#################################################################################

l1 = [1,2,3]
l2 = [10,20,30]

# look at the parameters!

def sommetta(l1,l2):
	l3 = [0]*len(l1)
	for i in range(len(l1)):
		l3[i]	= l1[i]+l2[i]

	return l3

lresult = sommetta(l1,l2)
print(lresult)



#################################################################################

# scope 
l1 = [1,2,3]
l2 = [10,20,30]

# look at the parameters!
def sommetta(l1,l2):
    for i in range(len(l1)):
        l1[i]    = l1[i]+l2[i]

    return l1

lresult = sommetta(l1,l2)
print(lresult)


#################################################################################

# list compr

l = ["a", "b", "c", "d"]

lc = [x for x in l]