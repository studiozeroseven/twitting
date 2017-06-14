from TwitterSearch import *
from keys import *


print('What do you want to search for?')
search = input()
fileresults = 'txt/' + search + '-results.txt'
f = open(fileresults, "w+")

def name_checker():
    f = open(fileresults,'r')
    for line in iter(f):
        print(line)
    f.close()

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
        username = tweet['user']['screen_name']
        f.write('@%s' % (username + '\n'))
        # print(username)
        name_checker()
        # with open("txt/" + search + '.txt') as file:
        #     for line in file:
        #         print(line)
                # if username in line:
                #     print('Exists: ' + username)
                # else:
                #     f.write('@%s' % (username + '\n'))  # Write each of the twitter @username to a line and then next line
                #     print('Added: ' + username)  # This line is just to see the output in the console for testing



except TwitterSearchException as e:                                 # take care of all those ugly errors if there are some
    print(e)