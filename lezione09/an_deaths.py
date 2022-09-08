import json
import matplotlib.pyplot as plt


years = ['1991', '1992', '1993']
deaths = [10, 20, 50]

plt.plot(years, deaths)
plt.suptitle('Morti per anno')
plt.show()

with open('lezione9/deadge.json', 'r') as f:
  data = json.load(f)

# in che mese é morto raimondo vianello

x = input("Chi é morto? ")

for year in data.keys():
	for month in data[year].keys():
		for day, deaths_of_day in data[year][month].items():
			for person in deaths_of_day:
				if x in person["name"]:
					print(person)
					print(year, month, day)


count_deaths = 0

for year in data.keys():
	for month in data[year].keys():
		for day, deaths_of_day in data[year][month].items():
			count_deaths += len(deaths_of_day)
			
print(count_deaths)