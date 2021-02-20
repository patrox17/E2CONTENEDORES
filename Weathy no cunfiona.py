import requests
import json

def imprimirDatos(datos):

	for i in datos:
		if type(datos[i]) == dict:

			imprimirDatos(datos[i])
			print('\n' * 3)
		elif type(datos[i]) == list:
			#print('-' * 180)
			#print(len(datos[i]))
			for j in datos[i]:
				print(f"informacion de manera: {i}")
				imprimirDatos(j)
			#print('-' * 180)
		else:
			print(f"{i}: -> {datos[i]}")
	

key = ""
lat = ""
lon = ""

#clima = requests.get(url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely&appid={key}")
file = open("infoClima.txt", "r")
data = file.readlines()
#data = json.loads(clima.text)
climas = json.loads(data[0])

#text = open("infoClima.txt", "a")
#text.write(clima.text)

#imprimirDatos(climas)
for j in range(len(climas["daily"])):

	for i in climas["daily"][j]["temp"]:
		#imprimirDatos(i)
		#print('-'*50)
		print(f"{i}: {climas['daily'][j]['temp'][i]/10}°C")
		#print(i)
	print('-'*150)
	



