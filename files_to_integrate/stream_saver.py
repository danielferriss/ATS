consumer_key = 'KatYMh46agxOxPOosTZAlu7Gx'
consumer_secret = 'CRFhThIBE3bgLkVem5BGOuwACeVUPPYVszjnpL10tqZF4nPVN9'
access_token = '922936042570899456-ZSH2PirUXsKBSigj5yivZHodHo4xmPo'
access_token_secret = 'dFCExwOFcBQlmwywoUGU2ROYt2iYxe6F9DtmvIYZN9Vbb'

# Authenticate Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
import tweepy
class MyStreamListener(tweepy.StreamListener):
    # This method will be called when new tweets come in
    def on_status(self, status):
        if (('RT') not in status.text and ('RT @') not in status.text):
                print(str(status.text))
                
            


def stream_saver(stock1, stock2):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    b = myStream.filter(track=[stock1, stock2], async=False)
