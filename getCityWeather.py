#by luis.bazo@gmail.com

import pyowm
import json
from pymongo import MongoClient
from datetime import datetime
import sys,getopt
import threading
import time
from optparse import OptionParser

def getWeatherDataForCity(city,offset):
	print "Gathering weather data for city of ", city, " ", " every ", offset, " seconds"
	# Search for current weather in London (UK)
	while(True):
		observation = owm.weather_at_place(city)
		w = observation.get_weather()

		#Add city to JSON weather
		jsonweather = w.to_JSON()

		jsonloads = json.loads(jsonweather)
		jsonloads['city']=city

		if(saveData):
			client.test.weather.insert_one(jsonloads)
		time.sleep(offset)

parser = OptionParser()
parser.add_option("-c", "--cities", dest="cities",help="Cities to get weather from: Example: London,uk", metavar="CITY,COUNTRY_CODE")
parser.add_option("-o", "--offset", dest="offset", help="how fast in seconds weather has to be retrieved")
parser.add_option("-a", "--api", dest="api",help="api key to get access to openweather")
parser.add_option("-s", "--saveData",action="store_true",dest="saveData",default=False, help="Whether to store data on mongoDB or not")
#parser.add_option("-w","--watsoniot",action="store_true",dest="sendToWatsonIoT",default=False, help="Whether to send data to WatsonIoT or not")
#parser.add_option("-l","--watsoniotoptions",type="string", nargs=4, dest="woptions",help="Watson IoT Connection Options: org sense_type sense_id token",metavar="org sense_type sense_id token")

(opts, args) = parser.parse_args()
cities = opts.cities
offset=float(opts.offset)
api=opts.api
saveData=opts.saveData

owm = pyowm.OWM(api)
print "Save data is ", saveData

if(saveData):
	client = MongoClient()

array_cities = cities.split("|")
threads = list()
for city in array_cities:
    t = threading.Thread(target=getWeatherDataForCity, args=(city,offset,))
    threads.append(t)
    t.start()
