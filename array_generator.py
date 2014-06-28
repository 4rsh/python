#!/usr/bin/python
# coding: utf-8

"""
Array Generator. — Developed by Arsh Leak.
$ wget https://github.com/4rsh/

HOW IT WORKS:
$ python array_generator.py
	Enter the array name:
	>  name

	Enter your string:
	>  array filled with string splitted

  Result:
	Array name
	name = ['array', 'filled', 'with', 'string', 'splitted']

"""

name = raw_input("\nEnter the name of your array.\n>")
items = raw_input("\nEnter your strings.\n>")
array = items.split()
print "\n\nArray name: ", name
print name, " = ", array
