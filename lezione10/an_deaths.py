import json
import matplotlib.pyplot as plt

# Load data
with open('lezione10/deadge.json', 'r') as f:
    data = json.load(f)


tot_morti_mese = {} # totale morti per ogni mese di ogni anno
tot_morti_anno = {} # totale morti per ogni anno
tot_morti_per_mese_acc = {} # accumulatore di morti per mese di ogni anno 

for anno, anno_vals in data.items():
	morti_anno_value = 0
	for mese, mese_vals in data[anno].items():
		morti_mese_value = 0
		if mese not in tot_morti_per_mese_acc.keys():
			tot_morti_per_mese_acc[mese] = 0
			
		for giorno, giorno_vals in mese_vals.items():
			morti_anno_value += len(giorno_vals)
			morti_mese_value += len(giorno_vals) 
			tot_morti_per_mese_acc[mese] += len(giorno_vals) 
		tot_morti_mese[anno + " " + mese] = morti_mese_value
	tot_morti_anno[anno] = morti_anno_value


# calcola medie per mese	
tot_morti_per_mese = {key:value/len(data.keys()) for (key,value) in tot_morti_per_mese_acc.items()}

#avg_morti_mese
avg_morti_mese = sum(tot_morti_mese.values())/len(tot_morti_mese.values())
print("Avg morti al mese: ", avg_morti_mese)



x = tot_morti_per_mese.keys()
y = tot_morti_per_mese.values()

plt.plot(x, y)
plt.plot(x, [avg_morti_mese]*len(x))
plt.xticks(rotation=45)
plt.suptitle('Morti per anno')
plt.show()

