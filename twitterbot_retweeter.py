import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#examplehastag').items():
    try:
        # Add \n for to clear it up
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet found tweet
        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow user that tweeted
        if not tweet.user.following:

                tweet.user.follow()
                print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

