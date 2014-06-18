 #!/bin/python

"""
Based on WebMap: https://github.com/4rsh/python/blob/master/webmap.py

DNSMap - Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""

# Colours
D  = "\033[0m";  
W  = "\033[01;37m";  
O  = "\033[01;33m"; 
SUCESS = "\033[01;32m";
FAIL = "\033[01;31m";

import socket
import sys
import os
os.system("clear")
print O+ "+----------------------------------------------------------------------------+"
print "|                                      DNSMap                                |"
print "+----------------------------------------------------------------------------+"
print "|                            Development by Arsh Leak.                       |"
print "|                         $ Wget > http://github.com/4rsh                    |"
print "+----------------------------------------------------------------------------+"
print W+""
domain = raw_input("Set domain: ") # www.domain.com
 
try:
    ip = socket.gethostbyname( domain )
 
except socket.gaierror:
    print FAIL+'Invalid Domain.\n\n\n\n\n\n\n'
    sys.exit()
print SUCESS+"+-------------------------+"
print SUCESS+"| DNS   : " +ip+ "     |"
print SUCESS+"+-------------------------+"
