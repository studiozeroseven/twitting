# twitting

### What should this app be doing.
It should do a twitter search based off a single keyword.
It then takes the tweet results and pulls out all the twitter handles (@username)
and checks to see if they already exist in the DB, if not it will add them to the MongoDB.


## What you need for this to work

### Twitter
You will need twitter api keys, get them and store them in keys.py in the root of your project (this file is not included for obvious reasons)

### MongoDB
You need a local setup of Mongo. See https://www.mongodb.com/ for installation

I think thats about it.


### Running Script
Just clone the files
Make the keys.py in the root dir
Make the Database (localhost, 27017)
Enter your search keyword (top of twit.py)
Run the twit.py
I use Robo 3T (https://robomongo.org/) for viewing the MongoDB
