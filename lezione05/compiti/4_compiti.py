import json
import requests
import datetime
# input province
province = input("Insert an Italian province: ")

# find province in the file, if not found, raise error, otherwise save lat and long

with open("lezione5/data/province.json", "r") as f:
  province_dic = json.load(f)

if province.capitalize() not in province_dic.keys():
  raise Exception("Please, insert an Italian province")

given_province_dic = province_dic[province.capitalize()]

lat = given_province_dic["lat"]
lon = given_province_dic["lon"]

#connect to api and find all data
province_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=apparent_temperature&current_weather=true".format(lat,lon)

response = requests.get(province_url)

response_json = response.json()
# print(response_json)


#find the row with lat and long correct and give back temperatura e temperatura percepita attuale

current_weather = response_json["current_weather"]
current_temp =  current_weather["temperature"]

# print("The current temperature in "+ province.capitalize() + " is " + str(current_temp) + "°C")

time_list = response_json["hourly"]["time"]
ap_temperature_list = response_json["hourly"]["apparent_temperature"]

now = datetime.datetime.now().strftime("%H")

ap_temperature = ap_temperature_list[int(now)]
# ap_temperature = 0
# for i in range(len(time_list)):
#   if time_list[i][11:13]:
#     ap_temperature = ap_temperature_list[i]

# just to be clear: your solution WAS ok. (well not the comparison part lmao, cos the time thing provides like 6 days so the now would have been the prediction at 6 days... )
# but the idea is good. EEEH 


print("and apparent temperature is " + str(ap_temperature))

# Hello. I promised i would not join discord, so...
# Look at this. 

# times = [00:00, 01:00, 02:00, ...]
# temps = [5, 6, 7, 5, ...]

# ok. So. Let's say its 2 in the morning. How do you read the temp? 
# ok good. Now... do you notice ANY pattern
# in the time list?
# can you write here the indexes of the list time?

# write the indexes. here. complete

# times = [00:00, 01:00, 02:00, 03:00, 04:00]

# times[0] --> 00:00
# times[1] --> 01:00
# times[2] --> 02:00
# please complete. write the content of each var.

# DO. YOU. SEE. ANY. PATTERN.

# the i-th element of the list is the i-th hour.
