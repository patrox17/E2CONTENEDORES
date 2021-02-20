from osinter import *
from weather import *
from gugul import *
from scrap import *
from TEAMS import *
from clima import *
from EQUIPOS import *

def menuFiltrado(paginas, diccionario):
	urls = list()
	expresion = "/players/.\w+ \w+/"
	jugadores = list()

	while(True):
		opcion = input("1.-Equipos Disponibles para analizar\n2.-Descargar Imagenes Del Equipo\n3.-Noticias de los equipos\n4.Proximos Juegos con clima pronosticado\n5.-salir:\n")

		if opcion == '1':
			Conseguirequipos()
			buscanombres()


		elif opcion == '2':
			print("coming soon")

		elif opcion == '3':
			googlin()
			f = open("urls.txt", "r")
			for i in f.readlines():
				urls.append(i)
			f.close()
			scrappy(urls)


		elif opcion == '4':
			buscanombres()

		elif opcion == '5':
			break


		else:
			print("opcion invalida")



if __name__ == "__main__":
	paginas = list()
	diccionario = list()
	menuFiltrado(paginas, diccionario)
