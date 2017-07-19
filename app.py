import time
import requests
import datetime
from pprint import pprint

while True:
	try:
		r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2965535&APPID=fff6ce2f865b03b789b7c1f537b6518b')
		data = r.json()
		place = data["name"]
		country = data['sys']['country']
		curWeather = data["weather"][0]["main"]
		curTemp = int(data["main"]["temp"]) - 273.15
		now = datetime.datetime.now()
		nowString = now.strftime("%I:%M%p on %B %d, %Y")
		display = '[DEV]The current weather at {4} in {0},{3} is {1} and the tempature is {2} celsius'.format(place, curWeather, curTemp, country, nowString)
		pprint(display)
		#pprint("daryl test)
	except Exception as ex1:
		print 'WEATHER DATA ERORR! ' + str(ex1)
	time.sleep(1030)
