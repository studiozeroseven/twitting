from pymongo import MongoClient



client = MongoClient("localhost", 27017, maxPoolSize=50)
db=client.localhost
collection=db['chain']
cursor = collection.find({})
for document in cursor:
      print(document)