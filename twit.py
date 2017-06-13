from TwitterSearch import *



print('What do you want to search for?')
search = input()

f = open(search + '.txt',"w+")



try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords([search]) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'xxxxxxxxxx',
        consumer_secret = 'xxxxxxxxxx',
        access_token = 'xxxxxxxxxx-xxxxxxxxxx',
        access_token_secret = 'xxxxxxxxxx'
     )


     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s' % ( tweet['user']['screen_name'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)