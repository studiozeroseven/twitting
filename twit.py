from TwitterSearch import *
from keys import *


print('What do you want to search for?')
search = input()

f = open('txt/' + search + '.txt',"w+")


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


    ts = TwitterSearch(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
     )


     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        f.write('@%s' % ( tweet['user']['screen_name'] + "\n"))
        print( '@%s' % ( tweet['user']['screen_name'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)