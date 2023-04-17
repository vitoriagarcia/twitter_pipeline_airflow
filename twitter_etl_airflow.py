from asyncio.windows_utils import pipe
from datetime import datetime
import json
import pandas as pd
import s3fs
import tweepy
from config import *

def run_twitter_etl():

    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='@EllenDeGeneres',
                            # 200 is max count allowed
                            count = 200,
                            # rts = retweets
                            include_rts = False,
                            tweet_mode = 'extended'
                            )

    tweet_list = []
    for tweet in tweets:
        text = tweet._json['full_text']

        refined_tweet = {'user': tweet.user.screen_name,
                        'text': text,
                        'favorite_count': tweet.favorite_count,
                        'retweet_count': tweet.retweet_count,
                        'created_at': tweet.created_at
        }

        tweet_list.append(refined_tweet)
    

    df = pd.DataFrame(tweet_list)
    df.to_csv('s3://twitter-airflow-vitoria/ellen_degeneres_twitter_data.csv') 

run_twitter_etl()