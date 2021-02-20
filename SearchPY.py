from googlesearch import search

def busqueda(frase, longitud):

	URL = search(frase, num_results=longitud)

	f = open("paginas.txt", "w")
	for i in URL:
		f.write(i + "\n")
	
	
if __name__ == "__main__":
	buscar = input("que quieres buscar?")
	busqueda(buscar)
