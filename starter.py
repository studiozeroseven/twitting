
from pymongo import MongoClient
client = MongoClient('mongodb://localhost', 27017)

db = client.twits
posts = db.posts

file = open('txt/pokemon-results.txt','r')
for line in file:
    post_data = {
        'name': line
    }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))