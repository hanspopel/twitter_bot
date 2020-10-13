#!/usr/bin/env python3

import markovify
import tweepy
from mtranslate import translate
import json

import re
from itertools import chain
from nltk.corpus import wordnet


def atest(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

# Get raw text as string.
with open("./resources/trump.txt") as f:
    text = f.read()

#with open('text_model.txt') as json_file:
 #   data = json.load(json_file)


#text.rstrip()
#s = '<@ """@$ FSDF >something something <more noise>'
# text.sub('<[^>]+>', '', text)
#text = atest(text)
#text.rstrip()

# with open('text_model.txt', 'w') as outfile:
#    json.dump(model_json, outfile)

# with open('whats_app_clean.txt', 'w') as outfile:
#     json.dump(model_json, outfile)

#with open("trump.txt", "w") as text_file:
#   text_file.write(text)

# Authenticate to Twitter


auth = tweepy.OAuthHandler("hwKC5YHpox2n1OhnEkVRj0kgV", "3CGDdBgfPboB40Z5NrpH7YZQhiuc18dBjpvnUsaX9NvqzuBqtq")
auth.set_access_token("1314907291934748673-FZh4mJF0Ul7QPFWCz46TfpXHjGAErk", "VZ5sfcTWmAh9m2LBM1RihCg26lhbIGUckxqRwRAFVoLix")

# AAAAAAAAAAAAAAAAAAAAAJEBIgEAAAAAlGxFVxAXGWX2ADWkEbbg177PM44%3DWS8J0p15Ny7BENOSeOrHoiMhQBGPtO9SvJAHLeSNXnR5s6UwsI
# curl -X GET -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAJEBIgEAAAAAlGxFVxAXGWX2ADWkEbbg177PM44%3DWS8J0p15Ny7BENOSeOrHoiMhQBGPtO9SvJAHLeSNXnR5s6UwsI" "https://api.twitter.com/2/tweets/20"
# Create API object
api = tweepy.API(auth)

# Build the model.
text_model = markovify.Text(text)

# result = text_model.make_short_sentence(280)
# print(result)

word = 'car'


synonyms = wordnet.synsets(text)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))

# result = translate(result, 'de')

#api.update_status(result)
#print(result)
#for i in range(4):
#   print(text_model.make_short_sentence(280))



#reconstituted_model = markovify.Text.from_json(data)

#reconstituted_model.reconstituted_model

#model_json = text_model.to_json()
#with open('text_model.txt', 'w') as outfile:
#    json.dump(model_json, outfile)

# Create a tweet
#api.update_status(text_model.make_short_sentence(280))
# api.update_status("Media put out false reports that it is too slow.")

#api.update_status("Our focus is on the Apprentice Season Eight!!!! AMAZING woman!")
# Our focus is on the Apprentice Season Eight!!!! AMAZING woman!

#curl --request POST --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=<http://listz.org/>' --header 'authorization: OAuth oauth_consumer_key="hwKC5YHpox2n1OhnEkVRj0kgV", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="1314907291934748673-FZh4mJF0Ul7QPFWCz46TfpXHjGAErk", oauth_version="1.0"'

#AAAAAAAAAAAAAAAAAAAAAJEBIgEAAAAAWnKfuDcZbVXwLasRtT4O6lLsIfo%3DCckrIRbNFN8YrY6yyyr5L0xgulDuRaFk0rxhxcChSXOimAeJz9
#api.update_status("Europe has had to endure.")


#result = reconstituted_model.make_short_sentence(280)
#print(result)
#result2 = translate("Joe Biden is a PUPPET of CASTRO-CHAVISTAS like Crazy Bernie, AOC and Castro-lover Karen Bass.", 'de')
#print(result2)
#result3 = translate(result2, 'de')
#print(result3)
#result4 = translate(result3, 'fr')
#print(result4)
#result5 = translate(result4, 'en')
#print(result5)
#result6 = translate(result5, 'fr')
#print(result6)
#result7 = translate(result6, 'ru')
#print(result7)
#result8 = translate(result7, 'se')
#print(result8)
#result9 = translate(result8, 'en')
#print(result9)
# Print five randomly-generated sentences
#for i in range(1):
#    print(text_model.make_sentence())
#    print("______________________________")

# Print three randomly-generated sentences of no more than 280 characters
#for i in range(1):
#    print(text_model.make_short_sentence(280))
#    print("______________________________")

  

#result = text_model.make_short_sentence(280)
#print(result)

#result3 = translate(result2, 'en')
#print(result3)


