#!/usr/bin/python
# coding: utf-8

"""
Good Luck or Not. — Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""

import random
import time

sorte	=	["yes", "nope"]

print "Good luck... or not.\n\n"
time.sleep(5.5)
if (random.choice(sorte)) == sorte[0]:
	print "You're in luck!"
else:
	print "You're outta luck."

# Enjoy, Arsh Leak.
