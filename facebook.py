import json
import requests

# Facebook API - Developed by Arsh Leak. (github.com/4rsh).

user 	=	raw_input ("\033[1mDigite o username:\033[0m \n")
url		=	requests.get('http://graph.facebook.com/%s/' % (user))
if url.status_code == 200:
    facebook_api = json.loads(url.content)
    for table in facebook_api:
    	print "-" * int(len(table)+2)
    	print "\033[1m%s:\033[0m %s" % (table.upper(), facebook_api[table])
else:
	print "Error."

# Enjoy, Arsh.
