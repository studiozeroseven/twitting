import os
from TwitterSearch import *
from keys import *



print('What do you want to search for?')
search = input()
file_results = 'txt/' + search + '-results.txt'
search_results = 'txt/' + search + '.txt'
r = open(search_results, "a+")
f = open(file_results, "w+")

has_user = ''


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

        file_size = os.stat('txt/teppen-results.txt').st_size
        print(file_size)

        if file_size <= 0:
            f.write('@%s' % (username + '\n'))
            print('HERE')
        else:
            with open("txt/" + search + '-results.txt') as rfile:
                for line in rfile:
                    if username in line:
                        print("-----")
                    else:
                        f.write('@%s' % (username + '\n'))
                        print('Added New Username: ' + username)
        # print(username)


except TwitterSearchException as e:                                 # take care of all those ugly errors if there are some
    print(e)


# class RunCompare():
#
#     def __init__(self):
#         with open("txt/" + search + '-results.txt') as file:
#             for line in file:
#                 with open("txt/" + search + '.txt') as search_file:
#                     for other_line in search_file:
#                         if other_line in line:
#                             print(
#                                 'Added: ' + username)  # This line is just to see the output in the console for testing                print('Exists: ' + username)
#                         else:
#                             r.write('@%s' % (
#                             username + '\n'))  # Write each of the twitter @username to a line and then next line
#
# RunCompare()
