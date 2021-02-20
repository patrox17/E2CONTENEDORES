import requests  
import json  #from datetime 
from datetime import datetime
import os

def wheatherInfo():
    api_key = "78d915775a7dcbfaf453861066d284b3"
    path = os.getcwd()
    wheatherInfos = []
    name="sites.txt" #Archivo donde se ingresan las paginas a buscar 
    with open(path+"\\"+name) as txt:
        for line in txt.readlines():
            #print(line)
            page = requests.get (f"http://api.openweathermap.org/data/2.5/weather?q={line}&units=metric&appid={input('ApiKey: ')}")
            weatherData = json.loads(page.content)
            #print(json.dumps(weatherData, indent=4, sort_keys=True)) 
            #Utilizando los datos recabados en wheatherData en la clave timezone_offset que son -5 horas; esto por el horario de verano
            #pero igual cuando el horario cambie la zona horaria igual cambiará en Openweather y por consiguiente en el get realizado.
            temp_min = str(int(weatherData['main']['temp_min']))+"°C"
            temp_max = str(int(weatherData['main']['temp_max']))+"°C"
            time = weatherData['weather'][0]['main']
            print(f"City: {line},Max: {temp_max},Min: {temp_min},Time: {str(time)}")
            wheatherInfos.append(f"City: {line},Max: {temp_max},Min: {temp_min},Time: {str(time)}")
            #print ("sunrise", datetime.utcfromtimestamp(int(weatherData["current"]["sunrise"]) + tzo).strftime("%d-%m-%Y %H:%M:%S"))  
            #print ("dt",datetime.utcfromtimestamp(int(weatherData["current"]["dt"]) + tzo ).strftime("%d-%m-%Y %H:%M"))  
            #print ("sunset",datetime.utcfromtimestamp(int(weatherData["current"]["sunset"]) + tzo).strftime("%d-%m-%Y %H:%M:%S"))  
    return wheatherInfos