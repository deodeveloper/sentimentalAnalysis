# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:14:12 2016

@author: Satya
"""

from tweepy import OAuthHandler
import tweepy
import urllib.request
import json
from unidecode import unidecode




CKEY = "QdjZPGYPwd99r72qQfyZyZEcO"
CSECRET = "yUgsvYUSFtNQIEgLW1aY9DMJRRxYajxfYC2pg3RzFhR3rkcl5L"
ATOKEN = "174336590-kvtw1cqrwuH75LIMKqXZkKSeoU9BfEAB9QBnMIoI"
ATOKENSECRET = "KdnYcVNI0h6ny7i9ACzNw3I0h0hLSlqdjXTSDoYpgDXc5"

URL_SENTIMENT140 = "http://www.sentiment140.com/api/bulkClassifyJson"
d = dict(parameter1="value1", parameter2="value2")

COMPANYNAME = "AAPL"
LIMIT = 2500
LANGUAGE = 'es'  # Sentiment140 API only support English or Spanish.


def parse_response(json_response):
    negative_tweets, positive_tweets = 0, 0
    for j in json_response["data"]:
        if int(j["polarity"]) == 0:
            negative_tweets += 1
        elif int(j["polarity"]) == 4:
            positive_tweets += 1
    return negative_tweets, positive_tweets


def main():
    auth = OAuthHandler(CKEY, CSECRET)
    auth.set_access_token(ATOKEN, ATOKENSECRET)
    api = tweepy.API(auth)
    tweets = []

    for tweet in tweepy.Cursor(api.search,
                               q=COMPANYNAME,
                               result_type='recent',
                               include_entities=True,
                               lang=LANGUAGE).items(LIMIT):
        aux = {"text": unidecode(tweet.text.replace('"', '')), "language": LANGUAGE, "query": COMPANYNAME,
               "id": tweet.id}
        tweets.append(aux)

    result = {"data": tweets}

    data = urllib.parse.urlencode(d).encode("utf-8")
    req = urllib.request.Request(URL_SENTIMENT140)
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req, str(result))
    json_response = json.loads(response.read())
    negative_tweets, positive_tweets = parse_response(json_response)
    print
    "Positive Tweets: " + str(positive_tweets)
    print
    "Negative Tweets: " + str(negative_tweets)


if __name__ == '__main__':
    main()