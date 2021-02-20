import re
import os
from bs4 import BeautifulSoup
import requests

infoUsers = []
def scrappy(urls):
    i = 0 
    global infoUsers 
    for url in urls:
        print("Getting Links")
        print(url[:-1])
        r = requests.get(url[:-1])
        soup = BeautifulSoup(r.content, 'html.parser')    
        print(f"Num{i}\n")
        name=f"page{i}.html"
        path = os.getcwd()
        with open(path+"\\"+name,"w+") as txt:
            txt.writelines(f"{soup.encode('utf-8')}")
            txt.close()
        i+=1
    for i in range(i-1,-1,-1):
        #print(i)
        name=f"page{i}.html"
        with open(path+"\\"+name,"r") as txt:
            for line in txt.readlines():
                temp = str(line.replace("b'","")[:-1])
                Socialms = ['facebook','twitter','instagram','twitch']
                for sm in Socialms:
                    scanner = re.compile(fr"https://{sm}.com/[a-zA-Z0-9]*")#Expresion regular para buscar redes sociales 
                    infoUsers.append(scanner.findall(temp))
                    #dd/mm/yyyy o d-mm-yyy
                    #scanner = re.compile(r"^(?:3[01-31]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$") #Listo 
                    #infoUsers.append(scanner.findall(temp))
                    # mm-dd-aaaa
                    #scanner = re.compile(r"^(?:0?[1-12]|1[1-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])\1\d{4}$")#Listo
                    #infoUsers.append(scanner.findall(temp))
                    #aaaa-mm-dd
                    #scanner = re.compile(r"^\d{4}([\-/.])(0?[1-9]|1[1-2])\1(3[01]|[12][0-9]|0?[1-9])$")
                    #infoUsers.append(scanner.findall(temp))
    return infoUsers
