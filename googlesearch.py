# coding: utf-8
# coding: latin-1

"""
WARNING
Ensure that your system has "requests" and "BeautifulSoup". If not, it will not run.

GoogleHardcore
"""

import requests
import BeautifulSoup

d  = "\033[0m";  
white  = "\033[01;37m";  
o  = "\033[01;33m";
red = "\033[01;31m";
green = "\033[01;32m";

query	=	raw_input("Digite sua pesquisa:	").red
r = requests.get('https://www.google.com.br/search?q=%s' % (query))
if r.status_code != 200:
        print "Error\n"
else:
	soup = BeautifulSoup.BeautifulSoup(r.content)

	for link in soup.findAll(attrs={'class':'g'}):

		for a in link.findAll('h3', attrs={'class':'r'}):
			title	=	a.text
			title	=	title.title()

		for l in link.findAll(attrs={'class':'s'}):
			print title, "\n", l.cite.text, "\n\n"
