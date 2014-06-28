#!/usr/bin/python
# coding: utf-8

"""
Array Generator. — Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""

name	=	raw_input("Enter the name of your array.\n>	")
items	=	raw_input("Enter your strings.\n>	")
array	=	items.split()
print "\n\n%s Array:\n" % name
print name + "	=	%s" % array
