import os
from TwitterSearch import *
from keys import *

# print('What do you want to search for?')
search = "teppen"

file_results = 'txt/' + search + '-results.txt'
f = open(file_results, "w+")

username_list = []

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords([search]) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    # Made a separate file called keys.py (not included) that I store the keys for my twitter app
    #
    # keys.py file format:
    #
    # consumer_key = 'XXXXXXXXXXXXXXXXXXXX'
    # consumer_secret = 'XXXXXXXXXXXXXXXXXXXX'
    # access_token = 'XXXXXXX-XXXXXXXXXXXXXXXXXXXX'
    # access_token_secret = 'XXXXXXXXXXXXXXXXXXXX'

    ts = TwitterSearch(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
        )

    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):

        username = "@" + tweet['user']['screen_name']
        # print(username)

        counter = 0

        # with open(file_results) as file:
        #     for line in file:
        #         if line is username:
        #             counter += 1
        #             print("IT EXISTS")

        for usern in username_list:
            if usern is username:
                counter += 1
                print("IT EXISTS")

        if counter == 0:
            username_list.append(username)
            # f.write(str(username_list))




except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)


print(username_list)