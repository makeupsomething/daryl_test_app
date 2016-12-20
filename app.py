import time
import sys
#sys.path.append("/usr/local/lib/python2.7/site-packages/")
import requests
from pprint import pprint

while True:
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2965535&APPID=fff6ce2f865b03b789b7c1f537b6518b')
	pprint(r.json())
	time.sleep(500)