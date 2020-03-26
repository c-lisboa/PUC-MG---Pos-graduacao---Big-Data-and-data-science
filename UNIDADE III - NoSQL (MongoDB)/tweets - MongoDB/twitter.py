from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pymongo
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('#server', 'port')
db = client.tweet
collection1 = db.tweet



consumer_key="#yourkeys"
consumer_secret="#yourkeys"


access_token="#yourkeys"
access_token_secret="#yourkeys"

class StdOutListener(StreamListener):
      
    def on_data(self, data):   
        a = json.loads(data)
        collection1.insert_one(a).inserted_id
        return True
        

    def on_error(self, status):
        print(status)


if __name__ == '__main__':  
# Handle Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['#tag'])

