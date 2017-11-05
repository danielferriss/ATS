class MyStreamListener(tweepy.StreamListener):
    
    # This method will be called when new tweets come in
    def on_status(self, status):
        if (('RT') not in status.text and ('RT @') not in status.text):
            print(status.text)
            print(status.user.name)
            print(status.created_at)
            print(status.id)
            with open(filename, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([status.text, status.user.name, status.created_at, status.id])
import csv
a = ['element','death','halloween']
def stream_saver(search_terms, filename):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    b = myStream.filter(track=search_terms, async=False)
stream_saver(a, 'filename.csv')
