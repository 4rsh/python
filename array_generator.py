#!/usr/bin/python
# coding: utf-8

"""
Array Generator. — Developed by Arsh Leak.
$ wget https://github.com/4rsh/

HOW WORKS:
$ python array_generator.py
	Enter the name of your array.
	>       name

	Enter your strings.
	>       Archiving Items Automatically

  Result:
	name Array:
	name    =       ['Archiving', 'Items', 'Automatically']

"""

name	=	raw_input("\nEnter the name of your array.\n>	")
items	=	raw_input("\nEnter your strings.\n>	")
array	=	items.split()
print "\n\n%s Array:" % name
print name + "	=	%s" % array
