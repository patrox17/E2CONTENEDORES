
import requests
import csv
import urllib.request
from bs4 import BeautifulSoup


def Conseguirequipos():
    teams = []
    result = requests.get('https://www.lineups.com/nfl/rosters')

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    equipos = soup.find_all('a', attrs={'class': 'link-black-underline team-txt'})

    for equipos in equipos:
        teams.append(equipos.attrs['href'])
    i = 0
    for teams in teams:
        print(str(i) + " " + teams.replace('/nfl/roster/', ""))
        i = i + 1
    print("¿Que equipo desea investigar?")

    selec1 = input()

    e = 0
    for teams in teams:
        teams2 = []
        result = requests.get('https://www.lineups.com/nfl/rosters')

        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        equipos = soup.find_all('a', attrs={'class': 'link-black-underline team-txt'})
        for equipos in equipos:
            teams2.append(equipos.attrs['href'])

        if (int(selec1) == e):
            restodellink = teams2[e]
        elif(int(selec1)==31):
            restodellink = "/nfl/roster/washington-redskins"
        else:
            e = e + 1

    f = open('tablateams.csv', 'w', newline='')

    writer = csv.writer(f)

    soup = BeautifulSoup(urllib.request.urlopen("https://www.lineups.com" + restodellink).read(),
                         'lxml')

    tbody = soup('table', {"class": "multi-row-data-table t-stripped"})[0].find_all('tr')
    for row in tbody:
        cols = row.findChildren(recursive=False)
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)
    return selec1


def printnum(selec1):
    print(Conseguirequipos(selec1))

def buscanombres():
    teams = []
    result = requests.get('https://www.nfl.com/schedules/team-schedules')

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    equipos = soup.find_all('a', attrs={'data-link_type': '_all-teams'})

    for equipos in equipos:
        teams.append(equipos.attrs['data-link_name'])

    i = 0
    for teams in teams:
     print(str(i) + " " + teams)
     i = i + 1