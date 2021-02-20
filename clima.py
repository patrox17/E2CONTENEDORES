import requests as requests
from pr import *
import json
import os
from pr import buscanombres
import requests
from bs4 import BeautifulSoup

def climacha2():
    teams2 = []
    results = requests.get('https://www.nfl.com/schedules/team-schedules')

    srcs = results.content
    soup3 = BeautifulSoup(srcs, 'lxml')

    equipos3 = soup3.find_all('a', attrs={'data-link_type': '_all-teams'})

    for equipos3 in equipos3:
        teams2.append(equipos3.attrs['data-link_name'])
    i = 0
    print(i)
    for teams2 in teams2:
        print(str(i) + " " + teams2)
        i = i + 1


def climacha():



    print("¿De que equipo quiere buscar partidos?")
    selec2 = input()

    teams = []
    result = requests.get('https://www.nfl.com/schedules/team-schedules')

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    equipos = soup.find_all('a', attrs={'aria-label': 'Schedule - Opens new window'})

    for equipos in equipos:
        teams.append(equipos.attrs['href'])

    e = 0

    for equipos in equipos:

        if (int(selec2) == 0):
            restodellink2 = "https://www.baltimoreravens.com/schedule/"
            ciudad = "Baltimore"
        elif (int(selec2) == 1):
            restodellink2 = "https://www.bengals.com/schedule/"
            ciudad = "Cincinnati"
        elif (int(selec2) == 2):
            restodellink2 = "https://www.clevelandbrowns.com/schedule/"
            ciudad = "Cleveland"
        elif (int(selec2) == 3):
            restodellink2 = "https://www.steelers.com/schedule/"
            ciudad = "Pittsburgh"
        elif (int(selec2) == 4):
            restodellink2 = "https://www.buffalobills.com/schedule/"
            ciudad = "Orchard Park"
        elif (int(selec2) == 5):
            restodellink2 = "https://www.miamidolphins.com/schedule/"
            ciudad = "Miami Gardens"
        elif (int(selec2) == 6):
            restodellink2 = "https://www.patriots.com/schedule/"
            ciudad = "Foxborough"
        elif (int(selec2) == 7):
            restodellink2 = "https://www.newyorkjets.com/schedule/"
            ciudad = "East Rutherford"
        elif (int(selec2) == 8):
            restodellink2 = "https://www.houstontexans.com/schedule/"
            ciudad = "Houston"
        elif (int(selec2) == 9):
            restodellink2 = "https://www.colts.com/schedule/"
            ciudad = "Indianapolis"
        elif (int(selec2) == 10):
            restodellink2 = "https://www.jaguars.com/schedule/"
            ciudad = "Jacksonville"
        elif (int(selec2) == 11):
            restodellink2 = "https://www.tennesseetitans.com/schedule/"
            ciudad = "Nashville"
        elif (int(selec2) == 12):
            restodellink2 = "https://www.denverbroncos.com/schedule/"
            ciudad = "Denver"
        elif (int(selec2) == 13):
            restodellink2 = "https://www.chiefs.com/schedule/"
            ciudad = "Kansas City"
        elif (int(selec2) == 14):
            restodellink2 = "https://www.raiders.com/schedule/"
            ciudad = "Paradise"
        elif (int(selec2) == 15):
            restodellink2 = "https://www.chargers.com/schedule/"
            ciudad = "Inglewood"
        elif (int(selec2) == 16):
            restodellink2 = "http://chicagobears.com/schedule"
            ciudad = "Chicago"
        elif (int(selec2) == 17):
            restodellink2 = "https://www.detroitlions.com/schedule"
            ciudad = "Detroit"
        elif (int(selec2) == 18):
            restodellink2 = "https://www.packers.com/schedule"
            ciudad = "Green Bay"
        elif (int(selec2) == 19):
            restodellink2 = "https://www.vikings.com/schedule"
            ciudad = "Minneapolis"
        elif (int(selec2) == 20):
            restodellink2 = "https://www.dallascowboys.com/schedule"
            ciudad = "Arlington"
        elif (int(selec2) == 21):
            restodellink2 = "https://www.giants.com/schedule"
            ciudad = "East Rutherford"
        elif (int(selec2) == 22):
            restodellink2 = "https://www.philadelphiaeagles.com/schedule"
            ciudad = "Philadelphia"
        elif (int(selec2) == 23):
            restodellink2 = "https://www.washingtonfootball.com/schedule/"
            ciudad = "Landover"
        elif (int(selec2) == 24):
            restodellink2 = "https://www.atlantafalcons.com/schedule"
            ciudad = "Atlanta"
        elif (int(selec2) == 25):
            restodellink2 = "https://www.panthers.com/schedule"
            ciudad = "Charlotte"
        elif (int(selec2) == 26):
            restodellink2 = "https://www.neworleanssaints.com/schedule"
            ciudad = "New Orleans"
        elif (int(selec2) == 27):
            restodellink2 = "https://www.buccaneers.com/schedule"
            ciudad = "Tampa"
        elif (int(selec2) == 28):
            restodellink2 = "https://www.azcardinals.com/schedule/"
            ciudad = "Glendale"
        elif (int(selec2) == 29):
            restodellink2 = "https://www.therams.com/schedule/"
            ciudad = "Inglewood"
        elif (int(selec2) == 30):
            restodellink2 = "https://www.49ers.com/schedule"
            ciudad = "Santa Clara"
        elif (int(selec2) == 31):
            restodellink2 = "https://www.seahawks.com/schedule"
            ciudad = "Seattle"

    print(restodellink2)

    def crear_archivo(cuidad):
        archil = open("sites.txt", "w")
        archil.write(cuidad)
        archil.close()

    def wheatherInfo():
        api_key = ""
        path = os.getcwd()
        wheatherInfos = []
        name = "sites.txt"  # Archivo donde se ingresan las paginas a buscar
        with open(path + "\\" + name) as txt:
            for line in txt.readlines():
                # print(line)
                page = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q={line}&units=metric&appid={input('ApiKey: ')}")
                weatherData = json.loads(page.content)
                # print(json.dumps(weatherData, indent=4, sort_keys=True))
                # Utilizando los datos recabados en wheatherData en la clave timezone_offset que son -5 horas; esto por el horario de verano
                # pero igual cuando el horario cambie la zona horaria igual cambiará en Openweather y por consiguiente en el get realizado.
                temp_min = str(int(weatherData['main']['temp_min'])) + "°C"
                temp_max = str(int(weatherData['main']['temp_max'])) + "°C"
                time = weatherData['weather'][0]['main']
                print(f"City: {line},Max: {temp_max},Min: {temp_min},Time: {str(time)}")
                wheatherInfos.append(f"City: {line},Max: {temp_max},Min: {temp_min},Time: {str(time)}")
                # print ("sunrise", datetime.utcfromtimestamp(int(weatherData["current"]["sunrise"]) + tzo).strftime("%d-%m-%Y %H:%M:%S"))
                # print ("dt",datetime.utcfromtimestamp(int(weatherData["current"]["dt"]) + tzo ).strftime("%d-%m-%Y %H:%M"))
                # print ("sunset",datetime.utcfromtimestamp(int(weatherData["current"]["sunset"]) + tzo).strftime("%d-%m-%Y %H:%M:%S"))
        return wheatherInfos

    crear_archivo(ciudad)
    wheatherInfo()





