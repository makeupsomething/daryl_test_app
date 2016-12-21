import time
import sys
#sys.path.append("/usr/local/lib/python2.7/site-packages/")
import requests
import json
from pprint import pprint

while True:
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2965535&APPID=fff6ce2f865b03b789b7c1f537b6518b')
	data = r.json()
	place = data["name"]
	curWeather = data["weather"][0]["main"]
	curTemp = int(data["main"]["temp"]) - 273.15
	print 'The current weather in {0} is {1} and the tempature is {2} celsius'.format(place, curWeather, curTemp)

	time.sleep(500)