#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Based on GooFile.
Coded by: Arsh Leak.
Greetz: dxhj (dxhj@hotmail.com).

Save this file as webmap.py

$ Wget > https://github.com/4rsh
"""

import string
import httplib
import sys
import re
import getopt
import os
import time

D  = "\033[0m";  
W  = "\033[01;37m";  
W2  = "\033[00;37m";  
R  = "\033[31m"; 
G  = "\033[32m,01"; 
O  = "\033[01;33m"; 
B  = "\033[00;34m";
SUCESS = "\033[01;32m";
FAIL = "\033[01;31m";

global result
result =[]
os.system("clear")

print O+ "+----------------------------------------------------------------------------+"
print "|                                      WebMap                                |"
print "+----------------------------------------------------------------------------+"
print "|                            Development by Arsh Leak.                       |"
print "|                         $ Wget > http://github.com/4rsh                    |"
print "+----------------------------------------------------------------------------+"
def usage():
 print W+ "                                  OPTIONS:"
 print B+"                                -d: Domain"
 print "                            -f: File (ex. php)"
 print "                  Ex:./webmap.py -d target.com -f php\n"
 print W+ ""

 sys.exit()

def run(url,file):

	h = httplib.HTTP('www.google.com')
	h.putrequest('GET',"/search?num=500&q=site:"+url+"+filetype:"+file)
	h.putheader('Host', 'www.google.com')
	h.putheader('User-agent', 'Internet Explorer 6.0 ')
	h.putheader('Referrer', 'www.github.com/4rsh/')
	h.endheaders()
	returncode, returnmsg, headers = h.getreply()
	data=h.getfile().read()
	data=re.sub('<b>','',data)
        for e in ('>','=','<','\\','(',')','"','http',':','//'):
		data = string.replace(data,e,' ')
	r1 = re.compile('[-_.a-zA-Z0-9.-_]*'+'\.'+file)	
	res = r1.findall(data) 
	return res 
	

def search(argv):
	global limit
	limit = 100
	if len(sys.argv) < 2: 
		usage() 
	try :
	      opts, args = getopt.getopt(argv,"d:f:")
 
	except getopt.GetoptError:
  	     	usage()
		sys.exit()
	
	for opt,arg in opts :
    	   	if opt == '-f' :
			file=arg
		elif opt == '-d':
			url=arg

	print W+"TARGET: "+url+"\nFILE: "+ file
	print "+----------------------------------------------------------------------------+"


	cant = 0

	while cant < limit:
		res = run(url,file)
		for x in res:
			if result.count(x) == 0:
        			result.append(x)
		cant+=100
			

	print SUCESS+"Listing results ..."
	print "+----------------------------------------------------------------------------+"
	time.sleep( 2 )
	t=0
	if result==[]:
		print FAIL+"No results. :/"
		print W+""
	else:
		print SUCESS+"LINKS FOUND!"
		for x in result:
			x= re.sub('<li class="first">','',x)
			x= re.sub('</li>','',x)
			print "[ + ] " + x + "\n"
			t+=1
	print "+----------------------------------------------------------------------------+\n"
	

if __name__ == "__main__":
        try: search(sys.argv[1:])
	except KeyboardInterrupt:
		print "\nYou interrupt the process."
	except:
		sys.exit()

# Enjoy, Arsh Leak.
