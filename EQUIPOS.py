
import requests as requests
from bs4 import BeautifulSoup

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
