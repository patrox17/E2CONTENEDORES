import os
from googlesearch import search
from scrap import *

def googlin():
    titulos = []
    urls = []
    htmls = {
    "Titulo": titulos,
    "Url": urls
}
    #query = "tsm esports" #
    query = str(input("Ingresa el nombre del equipo para buscar noticias relevantes:"))  #Esta variable se usa para ingresar el equipo que se va a buscar
    j = 0
    #Aqui busca las paginas web en google y las agrega a un archivo de texto 
    for i in search(query,tld = 'com',lang = 'en',num = 3, stop = 3, pause = 5):
        titulos.append(f"Miguelon{j}")
        urls.append(i)
        j +=1
    htmls = {
        "Titulos" : titulos,
        "Urls" : urls
    }
    #Crea el archivo donde se guardan las paginas web 
    path = os.getcwd()
    name= "urls.txt"
    with open(path+"\\"+name,"w") as txt:
        temp = ""
        for url in urls:        
            temp += url+"\n"
        txt.writelines(temp)


