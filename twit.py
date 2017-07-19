from pymongo import MongoClient
from TwitterSearch import *
from keys import *

# print('What do you want to search for?')
#TODO: Change this back to what it was, I forgot how to do it
search = "pokemon"

file_results = 'txt/' + search + '-results.txt'

client = MongoClient("localhost", 27017)
db2 = client.twits
posts = db2.posts

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords([search]) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    # Made a separate file called keys.py (not included) that I store the keys for my twitter app
    #
    #     keys.py file format:
    #
    #     consumer_key = 'XXXXXXXXXXXXXXXXXXXX'
    #     consumer_secret = 'XXXXXXXXXXXXXXXXXXXX'
    #     access_token = 'XXXXXXX-XXXXXXXXXXXXXXXXXXXX'
    #     access_token_secret = 'XXXXXXXXXXXXXXXXXXXX'

    #Setting up API
    ts = TwitterSearch(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
     )

     #This is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):

        username = "@" + tweet['user']['screen_name']
        # print(username)


        #Checking for duplicates
        duplicates = 0
        for document in posts.find({}):
            thename = document['name']
            if document['name'] == username:
                duplicates += 1
                print('dup')

        #If no duplicates, append
        if duplicates == 0:
            post_data = {
                'name': username
            }
            result = posts.insert_one(post_data)
            print('Added!')

        # print(users)


# (Takes care of all those ugly errors if there are some)
# No! It's catching only TwitterSearchException, other errors won't be handled
except TwitterSearchException as e:
    print(e)