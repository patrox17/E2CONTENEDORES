from ScraPY import *
from SearchPY import *
from osinter import *
from weather import *
from gugul import *
from scrap import *
import requests
import re
import csv
import urllib.request
from bs4 import BeautifulSoup



def imagenes(images,diccionario,expresion, url)
paginas = getHtml(getPage())
print("obteniendo links")
imagenes = (images(paginas, diccionario, expresion))
print("obteniendo paginas")

# baja formato de imagenes conocidos, si no se reconoce, lo guarda con la extension de los ultimos 4 caracteres contando el punto
for i in range(len(imagenes)):
    try:
        if "https://" in imagenes[i]:
            print(f"obteniendo: {imagenes[i]}")

            if ".jpg" in imagenes[i]:
                urllib.request.urlretrieve(imagenes[i], "imagenRecuperada" + str(i) + ".jpg")

            elif ".gif" in imagenes[i]:
                urllib.request.urlretrieve(imagenes[i], "imagenRecuperada" + str(i) + ".gif")

            elif ".png" in imagenes[i]:
                urllib.request.urlretrieve(imagenes[i], "imagenRecuperada" + str(i) + ".png")

            elif ".tiff" in imagenes[i]:
                urllib.request.urlretrieve(imagenes[i], "imagenRecuperada" + str(i) + ".tiff")

            elif ".bmp" in imagenes[i]:
                urllib.request.urlretrieve(imagenes[i], "imagenRecuperada" + str(i) + ".bmp")
            else:
                urllib.request.urlretrieve(imagenes[i], "imagenRecuperada" + str(i) + imagenes[i][-4:])

        else:
            print(f"obteniendo: {url + imagenes[i][1:]}")

            if ".jpg" in imagenes[i]:
                urllib.request.urlretrieve(url + imagenes[i], "imagenRecuperada" + str(i) + ".jpg")

            elif ".gif" in imagenes[i]:
                urllib.request.urlretrieve(url + imagenes[i], "imagenRecuperada" + str(i) + ".gif")

            elif ".png" in imagenes[i]:
                urllib.request.urlretrieve(url + imagenes[i], "imagenRecuperada" + str(i) + ".png")

            elif ".tiff" in imagenes[i]:
                urllib.request.urlretrieve(url + imagenes[i], "imagenRecuperada" + str(i) + ".tiff")

            elif ".bmp" in imagenes[i]:
                urllib.request.urlretrieve(url + imagenes[i], "imagenRecuperada" + str(i) + ".bmp")
            else:
                urllib.request.urlretrieve(url + imagenes[i], "imagenRecuperada" + str(i) + imagenes[i][-4:])