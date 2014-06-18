#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Know your PC — The machine settings.

Developed by Arsh Leak (https://github.com/4rsh/)
"""

import os
os.system("clear")
print " _____                                     _____ _____ "
print "|  |  |___ ___ _ _ _    _ _ ___ _ _ ___   |  _  |     |"
print "|    <    | . | | | |  | | | . | | |  _|  |   __|   --|"
print "|__|__|_|_|___|_____|  |_  |___|___|_|    |__|  |_____|"
print "                       |___| Developed by Arsh Leak     "
print "KNOW YOUR PC:\n"
print "[ Nome da Maquina: ]"
os.system("uname -n\n")
print "\n[ Nome do Kernel: ]"
os.system("uname -s")
print "\n[ Versão do Kernel: ]"
os.system("uname -v")
os.system("uname -r")
print "\n[ OS: ]"
os.system("uname -o")
print "\n[ Hardware da Maquina: ]"
os.system("uname -m")
print "\n[ Processador: ]"
os.system("uname -p")
print "\n[ Plataforma de Hardware: ]"
os.system("uname -i")

# Enjoy, Arsh Leak.
