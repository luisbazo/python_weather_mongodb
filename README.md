# python_weather_mongodb
This is an example of python program that reads weather data on a range of time, stores data in a mongoDB and performs some weather analysis over data stored.

The project is composed by 3 python scripts

1. getCityWeather: Python script to get weather data from a city or list of cities. Data is stored in a mongoDB.
  
  python getCityWeather.py -c "London,uk|Madrid,sp" -t 10 -o 1
  
  It gets 3 parameters: 

                       -c the list of cities to get weather data
                       -t the amount of data to be collected (times)
                       -o how often data should be collected (offset)
                       -a API key to get data from OpenWeather http://openweathermap.org/appid
  
2. calculateCityTemperatureAverage: Python script to calculate given city temperature average from data stored in mongoDB.
 
  python calculateCityTemperatureAverage.py -c "London,uk" 
 
  It gets 1 parameter: 
                      
                        -c the city to be calculated the average temperature.
3. resetCityData: Python script to delete all the weather data stored of a given city.
  
  python resetCityWeather.py -c "Madrid,sp"
  
  It gets 1 parameter: 

                        -c the city to be reset all weather data stored.

Prerequisites

  Python Libraries

  Use library pymongo to connect the mongoDB. To install execute command
  
        pip install pymongo
  
  For more related information please visit: https://docs.mongodb.com/getting-started/python/
  Use library pyown to get weather data from http://openweathermap.org/. To install execute command 
      
      pip install pyowm
    
  MongoDB

  
  It is needed to have a mongoDB server installed with a "test" database created. Change the scripts and database name on your convenience.
  Install mongoDB instructions: https://docs.mongodb.com/manual/administration/install-community/
  Once the database server is installed to create a db called "test" execute the steps documented in,
     http://www.tutorialspoint.com/mongodb/mongodb_create_database.htm
  
  Extensions

  More calculations and analysis could be introduced as part of this project. At this initial version it is only provided a mechanism to perform temperature average analysis in a given city. 
  
