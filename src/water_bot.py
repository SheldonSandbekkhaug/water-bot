#!/usr/bin/env python 

from secrets import *

import os
import markov_tweet_source
import simple_tweet_source
import tweepy


def main():
    # Set up tweepy.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweet_content = markov_tweet_source.markov_tweet()
    if tweet_content and len(tweet_content) <= 140:
        api.update_status(tweet_content)
        print 'Tweeted: ' + tweet_content
    else:
        print 'Nothing tweeted.'
    
def simple_tweet():
    tweet_content = simple_tweet_source.new_tweet()
    
main()