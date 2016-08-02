from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

#client = MongoClient("mongodb://127.0.0.1:27019")
client = MongoClient()

db = client.test

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

cursor = db.restaurants.find()

cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
for document in cursor:
    print(document)

result = db.restaurants.update_one(
    {"name": "Vella"},
    {
        "$set": {
        "address.street": "East 31st Street"
	},
        "$currentDate": {"lastModified": True}
    }
)

cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
for document in cursor:
    print(document)


result = db.restaurants.delete_many({"name": "Vella"})

print "The number of rows deleted ",  result.deleted_count

