#!/usr/bin/python
import requests

r = requests.get('https://www.offsec.com/offsec/game-hacking-intro/')

print(r.status_code)
print(r.text)
