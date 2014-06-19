#!usr/bin/python
# -*- coding: iso-8859-15 -*-

"""

AutoLinux — Developed by Arsh Leak.
$ wget https://github.com/4rsh/

"""


# Se as cores não funcionarem, insira "import colorama" (sem aspas) na linha 27.

# Colours
D  = "\033[0m";  
WHITE  = "\033[01;37m";  
O  = "\033[01;33m";
RED = "\033[01;31m";
GREEN = "\033[01;32m";

import os
import socket
import time
import sys

space = "                "
space2 = "          "
space3 = "                          "
resolv = socket.gethostbyname(socket.gethostname())

def comandar():
  comand = raw_input("\n" + space3 + GREEN+"Select an option:\n" + space3 + "> ")
  if comand == "1":
    instalar()
  elif comand == "2":
    salvar_web()
  elif comand == "3":
    conf()
  elif comand == "4":
    meuip()
  elif comand == "5":
    atualizar()
  elif comand == "6":
    ipresolver()
  elif comand == "7":
    contato()
  elif comand == "8":
    os.system("clear")
    print "\n\n\n\n\t\t\t\tBye ...\n\n\n\n"
    time.sleep(2)
    exit()
  else:
    print RED+"\t\t\tInvalid option.\n"
    time.sleep(1)
    logado()

def instalars():
  opcao = raw_input("\n\t" + GREEN+"Choose your option: (Press ENTER if you want to return to the menu.)\n" + space3 + "> ")
  if opcao == "8":
    os.system("clear")
    os.system("apt-get install nmap")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > nmap"
    saida = raw_input(space2 + "         " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  if opcao == "7":
    os.system("clear")
    os.system("apt-get install mpg321")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > mpg321"
    saida = raw_input(space2 + "         " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  if opcao == "6":
    os.system("clear")
    os.system("apt-get install wpscan")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > wpscan"
    saida = raw_input(space2 + "         " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  if opcao == "5":
    os.system("clear")
    os.system("wget -O slowloris.pl http://pastebin.com/raw.php?i=8072nGis")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > slowloris.pl"
    saida = raw_input(space2 + "         " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  if opcao == "4":
    os.system("clear")
    os.system("wget -O webmap.py http://pastebin.com/raw.php?i=6sB37AAM")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > webmap.py"
    saida = raw_input(space2 + "         " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  elif opcao =="3":
    os.system("clear")
    os.system("wget -O dnsmap.py http://pastebin.com/raw.php?i=hmkbYnpQ")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > dnsmap.py"
    saida = raw_input(space2 + "         " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  elif opcao =="2":
    os.system("clear")
    os.system("apt-get install gimp")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > gimp"
    saida = raw_input(space2 + "     " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  elif opcao =="1":
    os.system("clear")
    os.system("apt-get install flasm")
    os.system("clear")
    banner_central()
    print "               " + "File received successfully! > flasm"
    saida = raw_input(space2 + "      " + RED+"Press ENTER to return to menu.\n")
    if saida == "":
      instalar()
      instalars()
  elif opcao =="":
    logado()
def sistemas():
  print RED+"              (1) Install Scripts              (5) System Update\n              (2) Save Web Page                (6) Find IP of a Website\n              (3) Linux Settings               (7) Contact\n              (4) View my IP                   (8) Exit"
  comandar()

def salvar_web():
  os.system("clear")
  banner_central()
  web = raw_input(GREEN+"                     Enter the page that will save.\n                     > ")
  print "\n"
  if web == "":
    logado()
  else:
    fname = raw_input("       What is the name of the file you want to save? in: index.html\n                           > ")
    if fname == "":
      logado()
    else:
      print "\n\n"
      os.system("wget -O "+fname+ " "+web)

def banner_central():
  print WHITE+"\n"
  print "                                       ( ("
  print "                                        ) )"
  print "                                      ........"
  print "                                      | Arsh  |]"
  print "                                      \ Leak /"
  print "                                       `----*"
  print "          ---------------------------------------------------------------"
  print "          |                    AutoLinux - by Arsh Leak                  |"
  print "          ---------------------------------------------------------------"

def banner_central2():
  print WHITE+"\n"
  print "                                       ( ("
  print "                                        ) )"
  print "                                      ........"
  print "                                      | Arsh  |]"
  print "                                      \ Leak /"
  print "                                       `----*"
  print "          ---------------------------------------------------------------"

def meuip():
  print "\n"
  print "                       " + "< Your IP: " + resolv + " >"
  saida = raw_input(space2 + "            " + RED+"Press ENTER to return to menu.\n")
  if saida == "":
    logado()

def atualizar():
  os.system("clear")
  banner_central()
  opc = raw_input(RED+"              1) Update        2) Upgrade        3) Update and Upgrade\n\n              "+ GREEN+"> ")
  if opc == "1":
    os.system("apt-get update")
  elif opc == "2":
    os.system("apt-get upgrade")
  elif opc == "3":
    os.system("apt-get update")
    os.system("apt-get upgrade")
  elif opc == "":
    logado()
def contato():
  os.system("clear")
  banner_central2()
  print space2 + "               " + "GitHub: http://github.com/4rsh\n"
  saida = raw_input(space2 + "          " + RED+"Pressione ENTER para voltar ao Menu.\n")
  if saida == "":
    logado()

def instalar():
  os.system("clear")
  banner_central()
  print O+"              Installation Script\n"
  print RED+ space2 + "    " + "(1) Flasm" + space + "         ""(5) Slowloris"
  print RED+ space2 + "    " + "(2) Gimp" + space + "          " + "(6) WpScan"
  print RED+ space2 + "    " + "(3) DNS-Map" + space + "       ""(7) mpg321"
  print RED+ space2 + "    " + "(4) WebMap" + space + "        " + "(8) Nmap"
  instalars()

def ipresolver():
  os.system("clear")
  banner_central()
  domain = raw_input(WHITE+"                    Enter a domain: ") # www.domain.com
 
  try:
      ip = socket.gethostbyname( domain )
 
  except socket.gaierror:
      print RED+'Invalid Domain.\n\n\n\n\n\n\n'
      sys.exit()
  print space2 + "\t    "+domain + " - " + ip
  saida = raw_input(RED+"                  Press ENTER to return to menu.\n")
  if saida == "":
    logado()

def conf():
  os.system("clear")
  print "\n[ Machine Name: ]"
  os.system("uname -n\n")
  print "\n[ Kernel Name: ]"
  os.system("uname -s")
  print "\n[ Kernel Version: ]"
  os.system("uname -v")
  print "\n[ Kernel Release: ]"
  os.system("uname -r")
  print "\n[ Hardware: ]"
  os.system("uname -m")
  print "\n[ Processor: ]"
  os.system("uname -p")
  print "\n[ Hardware Platform: ]"
  os.system("uname -i")
  print "\n"
  saida = raw_input(RED+"Press ENTER to return to menu.\n")
  if saida == "":
    logado()


def logado():
    os.system("clear")
    banner_central()
    print O+ "              " "Welcome.\n"
    sistemas()

logado()

# Enjoy, Arsh Leak.
