import requests
import random

"""
A Simple Brute Force Script. Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""

user			=	["user", "admin"]	# Users for test.
user_force		=	random.choice(user)

password		=	"passwd"			# Password for test.
website			=	"http://httpbin.org/basic-auth/user/passwd"	# Website.
r = requests.get(website, auth=(user_force, password))			# Infos.

if r.status_code == 200:		# If OK.
	print "\nAllowed Access!\n\nLink:	%s\nUser:	%s\nPass:	%s\nState:	%s" % (website, user_force, password, r)
else:							# Else.
	print "\nAcess Denied!\n"

# Enjoy, Arsh.
