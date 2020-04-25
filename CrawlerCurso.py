import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import nltk

def SeparaPalavras(texto):
    stop = nltk.corpus.stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer()
    splitter = re.compile('\W+')
    lista_palavras = []
    lista = [p for p in splitter.split(texto) if p != ""]

    for p in lista:
        if p.lower() not in stop:
            if len(p) > 1:
                lista_palavras.append(stemmer.stem(p).lower())
    return lista_palavras

teste = SeparaPalavras('Este lugar é apavorante')
for t in teste:
    print(t)

def GetTexto(soup):
    for tags in soup(['script', 'style']):
        tags.decompose()

    return ' '.join(soup.stripped_strings)

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
    
def GetData(listaPag, profundidade):
    for i in range(profundidade):
        novas_paginas = set()
        for pagina in listaPag:
            dataPag = crawl(pagina)
            links = GetSoup(dataPag)
            count =1
            for link in links:
                # print(str(link.contents) + " - " + str(link.get("href")))
                if('href' in link.attrs):
                    url = urljoin(pagina, str(link.get('href')))
                    # if url != link.get('href'):
                    #     print("\n\n"+url+"\n\n")
                    #     count +=1
                    url = url.split("#")[0]
                    if url[0:4] == 'http':
                        novas_paginas.add(url)
                    if url.find("'") != -1:
                        continue
                
                    count +=1
            listaPag = novas_paginas
                    
    print(count)

NumOfPag = 1
listaPaginas = ['https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o']

GetData(listaPaginas, 2)
