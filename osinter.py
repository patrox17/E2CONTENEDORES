from bs4 import BeautifulSoup as bs
import re


def patron(clave, expresion, paginas):
	analisis = re.findall(expresion, paginas)

	return analisis


def anchors(paginas, parametros, expresion):
	listaDatos = list()
	analisis = list()
	soup = list()
	a = list()
	for i in range(len(paginas)):
		soup.append(list())
		soup[i] = bs(paginas[i], "html.parser")
		for j in soup[i].findAll("a", {"class": "nfl-o-roster__player-name nfl-o-cta--link"}):
			a.append(j["href"])

	return a


def division(paginas, parametros, expresion):
	listaDatos = list()
	analisis = list()
	soup = list()
	div = list()
	for i in range(len(paginas)):
		soup.append(list())
		soup[i] = bs(paginas[i], "html.parser")
		for j in soup[i].findAll("div"):
			print(j)
			div.append(j)

	return div


def images(paginas, parametros, expresion):
	listaDatos = list()
	analisis = list()
	soup = list()
	imgs = list()
	aux = ""
	for i in range(len(paginas)):
		soup.append(list())
		soup[i] = bs(paginas[i], "html.parser")
		aux = soup[i].findAll("img")
		try:
			for j in aux:
				print(f"link imagen encontrada: {j['src']}")

				imgs.append(j["src"])

		except:
			return imgs

	return imgs



