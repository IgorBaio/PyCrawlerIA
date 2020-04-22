import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def crawl(pagina):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    try:
        dados_pagina = http.request('GET', pagina)
    except:
        print("Erro ao abrir a página"+pagina)
    
    return dados_pagina


def GetSoup(dados_pagina):
    soup = BeautifulSoup(dados_pagina.data, "lxml")
    return soup.find_all('a')
    
def GetData(listaPag):
    # pagina = 'https://fitgirlrepacks.co/all-my-repacks-a-z/'+str(NumOfPag)
    count =1
    novas_paginas = set()
    for pagina in listaPag:
        dataPag = crawl(pagina)
        links = GetSoup(dataPag)
        for link in links:
            # print(str(link.contents) + " - " + str(link.get("href")))
            if('title' in link.attrs):
                url = urljoin(pagina, str(link.get('href')))
                if url != link.get('href'):
                    print("\n\n"+url+"\n\n")
                    count +=1
                print(link.attrs)
                count +=1
                if url[0:4] == 'http':
                    novas_paginas.add(url)
                if url.find("'") != -1:
                    continue
    print(count)
    return novas_paginas

def GetNumeroDePaginas(listaPag):
    domain = 'https://fitgirlrepacks.co/all-my-repacks-a-z/'
    pagina = domain+str(NumOfPag)
    dataPag = crawl(pagina)
    links = GetSoup(dataPag)
    count =1
    for link in links:
        # print(str(link.contents) + " - " + str(link.get("href")))
        # print(link.attrs)
        if('href' in link.attrs):
            url = urljoin(pagina, str(link.get('href')))
            if url == domain+str(count+1):
                print("\n\n"+url+"\n\n")
                count +=1
                listaPag.append(url)
            # print(link.attrs)
            if url.find("'") != -1:
                continue
    print(count)

def saveFile():
    file = open("/home/igorbaio/Documentos/PyCrawlerIA/PyCrawlerIA/paginas.txt", "w")
    for pagina in NovasPaginas:
        file.write(pagina+"\n")
NumOfPag = 1
listaPaginas = []
# NumDePaginas = g
GetNumeroDePaginas(listaPaginas)

NovasPaginas = GetData(listaPaginas)
