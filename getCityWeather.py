#by luis.bazo@gmail.com

import pyowm
import json
from pymongo import MongoClient
from datetime import datetime
import sys,getopt
import threading
import time

def getWeatherDataForCity(city,times,offset):
	print "Gathering weather data for city of ", city, " ", times, " times every ", offset, " seconds"
	# Search for current weather in London (UK)
	for i in range(times):
		observation = owm.weather_at_place(city)
		w = observation.get_weather()

		#Add city to JSON weather
		jsonweather = w.to_JSON()

		jsonloads = json.loads(jsonweather)
		jsonloads['city']=city


		client.test.weather.insert_one(jsonloads)
		time.sleep(offset)

try:
	opts, args = getopt.getopt(sys.argv[1:],"hc:t:o:a:",["cities=,times=,offset=,api="])
except getopt.GetoptError:
	print 'getCityWeather.py -c city1|city2 -t 100 -o 5 -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	print 'Example: getCityWeather.py -c "London,uk|Madrid,sp" -t 100 -o 5 -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print 'getCityWeather.py -c city1|city2 -t 100 -o 5 -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		print 'Example: getCityWeather.py -c "London,uk|Madrid,sp" -t 100 -o 5 -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		sys.exit()
	elif opt in ("-c", "--cities"):
		cities = arg
	elif opt in ("-t", "--times"):
		times = int(arg)
	elif opt in ("-o", "--offset"):
		offset = int(arg)
	elif opt in ("-a", "--api"):
		api = arg

if (times <= 0 or offset <= 0):
	print 'time and offset should be greater than 0'
	print 'getCityWeather.py -c city1|city2 -t 100 -o 5 -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	print 'Example: getCityWeather.py -c "London,uk|Madrid,sp" -t 100 -o 5 -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	sys.exit()

owm = pyowm.OWM(api)
client = MongoClient()

array_cities = cities.split("|")
threads = list()
for city in array_cities:
    t = threading.Thread(target=getWeatherDataForCity, args=(city,times,offset,))
    threads.append(t)
    t.start()
