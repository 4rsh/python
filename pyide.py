import os

"""

PyIDE — Developed by Arsh Leak.
$ wget https://github.com/4rsh/

"""

# Naming the file.
name		=	raw_input("Type a name for your file.\n")
if len(name) < 4:
	print "Try again.\n"
else:
	file_name 	=   open(name, "a")

	# Writing.
	coding		=	True
	os.system("clear")
	print "[Code: %s]" % name
	print "\n\n"
	while coding:

		code		=	raw_input("")
		file_name.write(code + "\n")
		pass

	print "\n\n\nSaved >> %s" % name
