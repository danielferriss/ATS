import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'piD5ZRtp7ptVqw4RsidYFrAJe'
consumer_secret = '1MmS2JfsHNNOHC1bdp4JoLv1Ze0obvJXbWrWKlIo227diIOiLi'
access_token = '783065971326128128-WfCrUOarn92O6NS9PG8yLZrMFWgtvDw'
access_token_secret = 'HyAYWhw8dGGOXq30SXMjcrbailw9wrIOxyktuJrVXeukz'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# ticker1 and ticker2 being each of the two stocks in String form
stockResultsOne = api.search(q=ticker1 + "stock")
stockResultsTwo = api.search(q=ticker2 + "stock")

print("Stock #1 Tweets")

for result in stockResultsOne:
	print (result.text)

print("--------------------------------")


print("Stock #2 Tweets")

for result in stockResultsTwo:
        print (result.text)

