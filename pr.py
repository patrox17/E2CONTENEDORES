import requests
import requests as requests
from bs4 import BeautifulSoup


def buscanombres():
    teams5 = []
    result = requests.get('https://www.nfl.com/schedules/team-schedules')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    equipos5 = soup.find_all('a', attrs={'data-link_type': '_all-teams'})

    for equipos5 in equipos5:
        teams5.append(equipos5.attrs['data-link_name'])

    l = 0
    for teams5 in teams5:
        print(str(l) + " " + teams5)
        l = l + 1
