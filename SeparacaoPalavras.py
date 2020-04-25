import re
import nltk
# nltk.download()

stop1 = ['é']
stop2 = nltk.corpus.stopwords.words('portuguese')

splitter = re.compile('\W+')
stemmer = nltk.stem.RSLPStemmer()
lista_palavras = []
string = "Este lugar é apavorante a b c c++"
lista = [p for p in splitter.split(string) if p != ""]

for p in lista:
    if p.lower() not in stop2:
        if len(p) > 1:
            lista_palavras.append(stemmer.stem(p).lower())
    
for i in lista_palavras:
    print(i)

print(stemmer.stem('nova'))
print(stemmer.stem("novamente"))