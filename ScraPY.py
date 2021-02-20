from bs4 import BeautifulSoup as bs
import requests


#modulo para conseguir las paginas
def getPage():
	paginas = list()
	req = list()
	f = open("paginas.txt", "r").readlines()
	paginas = [line.rstrip('\n') for line in f]
	
	for i in range(len(paginas)):
		print(f"obteniendo pagina: {i}")
		if "https://" in paginas[i]:
			if paginas[i]:	
				req.append(list())
				req[i] = requests.get(paginas[i])
	
	return req

def getStatus(paginas):
	status = list()
	for i in range(len(paginas)):
		status.append(paginas[i].status_code)
	return status

def getHeaders(paginas):
	headers = list()
	if type(paginas) == list:
		for i in range(len(paginas)):
			headers.append(paginas[i].headers)
	return headers

def getHtml(paginas):
	soup = list()
	aux = ""
	for i in range(len(paginas)):
		soup.append(bs(paginas[i].text, "html.parser"))
		soup[i] = soup[i].prettify().encode('cp1252', errors='ignore')
	return soup

def makePretty(paginas):
	soup = list()
	for i in range(len(paginas)):
		#print(type(paginas[i]))
		soup.append(bs(paginas[i], "html.parser"))
		soup[i] = soup[i].prettify()
		print(f"haciendo mas facil de leer archiv: {i}")

	return soup



if __name__ == "__main__":
	rPaginas = getPage()
	print(rPaginas)



