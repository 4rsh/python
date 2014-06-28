import os

"""

PyIDE — Developed by Arsh Leak.
$ wget https://github.com/4rsh/

"""


name = raw_input("Type a name for your file.\n")
if len(name) < 1:
	print "The filename cannot be empty.\n"
else:
	file = open(name)
	# Writing.
	coding = True
	os.system("clear")
	print "[Code: %s]" % name
	print "\n\n"
	while coding:
		code = raw_input("> ")
		if code == "exit()":
			coding = False
		file.write(code + "\n")

	print "\n\n\nSaved >> %s" % name
	file.close()
