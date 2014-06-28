# -*- encoding: UTF-8 -*-
import os
import re
"""
PyIDE — Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""

filename = raw_input("Type a name for your file.\n")
test = re.match("[a-zA-Z]+([a-zA-Z]*[0-9]*)*(\.[a-zA-Z])", filename)
if not test:
	print "Invalid filename"
else:
	count = 0
	f = open(filename, 'a')
	coding = True
	os.system("clear")
	print "[File: %s]" % filename
	print "\n"
	while coding:
		code = raw_input("> ")
		if code == "exit()":
			coding = False
		f.write(code + "\n")
		count += 1

	print "\nSaved >> %s %d alterations" % (filename, count)
	f.close()
