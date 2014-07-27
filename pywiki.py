#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from urllib2 import urlopen
import requests
import BeautifulSoup
import os

"""

WARNING:
Make sure you have all the modules imported in this script.
If you think you can do better, make one from zero, thanks.

HowTo:
$ python filename.py --en YourQuery
or
$ python filename.py --en Your_Query

PyWiki - Developed by Arsh Leak. (github.com/4rsh)

"""


class bcolors:
    WARNING = '\033[0m'

script, lang, query = argv

def success(query):
	os.system("clear")
	print bcolors.WARNING + """
	\033[0;37m
	██████╗ ██╗   ██╗██╗    ██╗██╗██╗  ██╗██╗
	██╔══██╗╚██╗ ██╔╝██║    ██║██║██║ ██╔╝██║
	██████╔╝ ╚████╔╝ ██║ █╗ ██║██║█████╔╝ ██║
	██╔═══╝   ╚██╔╝  ██║███╗██║██║██╔═██╗ ██║
	██║        ██║   ╚███╔███╔╝██║██║  ██╗██║
	╚═╝        ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝
    	Developed by \033[1;37mArsh Leak.\033[0;37m (github.com/4rsh)

\033[1;37m[ %s ]\033[0m
	""" % query

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def wiki_ok(lang, query):
	search	=	requests.get("http://%s.wikipedia.org/wiki/%s" % (lang, query))
	if search.status_code != 200:
		print "\033[1;31mError in connection, or your search was not found.\033[0m\n"
	else:
		conn 	= 	BeautifulSoup.BeautifulSoup(search.content)

		for detect_class in conn.findAll(attrs={'class':'mw-content-ltr'}):
			success(query)

			if "may refer to:" in detect_class.p.text:
				print "\033[1;31mThe searches were not specified correctly.\033[0m"

			else:

				reps	=	{
				"[1]"	:	" ",
				"[2]"	:	" ",
				"[3]"	:	" ",
				"[4]"	:	" ",
				"[5]"	:	" ",
				"[6]"	:	" ",
				"[7]"	:	" ",
				"[8]"	:	" ",
				"[9]"	:	" "
				}

				complete	=	replace_all(detect_class.p.text, reps)
				print "\033[0;37m", complete.upper().capitalize(), "\n \033[0m"

def wiki_error():
	print "\nSomething is wrong, you used:\nfilename.py --yourtld Query ?\n"

if "--" in lang:
	lang	=	lang.replace("--", "")
	wiki_ok(lang, query)

else:
	wiki_error()


# Enjoy, Arsh Leak.
