#!/usr/bin/env python3

import markovify
import tweepy



# Get raw text as string.
with open("trump.txt") as f:
    text = f.read()

# Authenticate to Twitter
auth = tweepy.OAuthHandler("hwKC5YHpox2n1OhnEkVRj0kgV", "3CGDdBgfPboB40Z5NrpH7YZQhiuc18dBjpvnUsaX9NvqzuBqtq")
auth.set_access_token("1314907291934748673-FZh4mJF0Ul7QPFWCz46TfpXHjGAErk", "VZ5sfcTWmAh9m2LBM1RihCg26lhbIGUckxqRwRAFVoLix")

# AAAAAAAAAAAAAAAAAAAAAJEBIgEAAAAAlGxFVxAXGWX2ADWkEbbg177PM44%3DWS8J0p15Ny7BENOSeOrHoiMhQBGPtO9SvJAHLeSNXnR5s6UwsI
# curl -X GET -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAJEBIgEAAAAAlGxFVxAXGWX2ADWkEbbg177PM44%3DWS8J0p15Ny7BENOSeOrHoiMhQBGPtO9SvJAHLeSNXnR5s6UwsI" "https://api.twitter.com/2/tweets/20"
# Create API object
api = tweepy.API(auth)

# Build the model.
text_model = markovify.Text(text,state_size=3)
# Create a tweet
api.update_status(text_model.make_short_sentence(280))


curl --request POST --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=<http://listz.org/>' --header 'authorization: OAuth oauth_consumer_key="hwKC5YHpox2n1OhnEkVRj0kgV", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="1314907291934748673-FZh4mJF0Ul7QPFWCz46TfpXHjGAErk", oauth_version="1.0"'

#AAAAAAAAAAAAAAAAAAAAAJEBIgEAAAAAWnKfuDcZbVXwLasRtT4O6lLsIfo%3DCckrIRbNFN8YrY6yyyr5L0xgulDuRaFk0rxhxcChSXOimAeJz9


# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))
   
