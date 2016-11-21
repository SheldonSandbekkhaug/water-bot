#!/usr/bin/env python 

from secrets import *

import simple_tweet_source
import tweepy


def main():
    # Set up tweepy.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Get some content to tweet.
    tweet_content = simple_tweet_source.new_tweet()
    api.update_status(tweet_content)
    print 'Tweeted: ' + tweet_content
    
main()