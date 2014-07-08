# -*- coding utf-8 -*-
import requests
import BeautifulSoup

query	=	"php" # O que será pesquisado.
r = requests.get('https://www.google.com.br/search?q=%s' % (query))
soup = BeautifulSoup.BeautifulSoup(r.content) # Codigo fonte do Google.

for link in soup.findAll(attrs={'class':'g'}): # Div classe = "g"

    for l in link.findAll(attrs={'class':'rc'}): # Div classe = "rc"
    	print l.h3.text, "\n" # Aqui printa o titulo da resposta. Ex: PHP: Hypertext Preprocessor
