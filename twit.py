import os.path
from TwitterSearch import *
from keys import *

# print('What do you want to search for?')
#TODO: Change this back to what it was, I forgot how to do it
search = "pokemon"

file_results = 'txt/' + search + '-results.txt'
if os.path.isfile(file_results):
    f = open(file_results, 'r')
    users = [line.strip() for line in f]
    f.close()
    print(users)
else:
    users = []
f = open(file_results, 'w')

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
        for user in users:
            if user == username:
                duplicates += 1

        #If no duplicates, append
        if duplicates == 0:
            users.append(username)

        # print(users)

    #Writing user names to the text file
    for user in users:
        f.write("%s\n" % user)

# (Takes care of all those ugly errors if there are some)
# No! It's catching only TwitterSearchException, other errors won't be handled
except TwitterSearchException as e:
    print(e)