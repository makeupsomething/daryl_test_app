import time
import requests
from pprint import pprint

while True:
	try:
		r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2965535&APPID=fff6ce2f865b03b789b7c1f537b6518b')
		data = r.json()
		place = data["name"]
		country = data['sys']['country']
		curWeather = data["weather"][0]["main"]
		curTemp = int(data["main"]["temp"]) - 273.15
		display = 'The current weather in {0},{3} is {1} and the tempature is {2} celsius. Have a nice day.'.format(place, curWeather, curTemp, country)
		pprint(display)
	except Exception as ex1:
		print 'WEATHER DATA ERORR! ' + str(ex1)
	time.sleep(1550)
