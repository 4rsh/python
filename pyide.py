import os

"""

PyIDE — Developed by Arsh Leak.
$ wget https://github.com/4rsh/

"""

while True:
	name = raw_input("Type a name for your file.\n")
	if len(name) < 4:
		print "Try again.\n"
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
