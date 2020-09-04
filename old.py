import tweepy
import os
import json
import requests
import onesignal as onesignal_sdk

#Sets Font For Print
class colour:
    purple = '\033[95m'
    green = '\033[92m'
    red = '\033[91m'
    blue = '\033[94m'
    bold = '\033[1m'
    end = '\033[0m'

from api import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

onesignal_client = onesignal_sdk.Client(user_auth_key="API",
app_auth_key="API",
app_id="API")

print(colour.purple, 'Connected to Twitter and OneSignal API', colour.end)

# Upload image
print(colour.bold, colour.blue)
image = input('Drag in an image path, or press enter to Tweet without an image: ')
print(colour.end)
if image == '':
    print(colour.bold, colour.blue)
    tweet = str(input('Enter Tweet: '))
    print(colour.end)
    
    try:
        post_result = api.update_status(tweet)
        print(colour.bold, colour.green, 'TWEETED:', colour.end, colour.green, tweet, colour.end)
    except:
        print(colour.bold, colour.red, 'There was an error sending the Tweet', colour.end)
else:
    print(colour.bold, colour.green, 'Uploading image...', colour.end)
    media = api.media_upload(image)
    print(colour.bold, colour.blue)
    tweet = input('Enter Tweet: ')
    print(colour.end)
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])   
    print(colour.bold, colour.green, 'TWEETED:', colour.end, colour.green, tweet, colour.end)

#Notification

new_notification = onesignal_sdk.Notification(post_body={
    "contents": {"en": tweet},
    "included_segments": ["All"]
})

try:
    onesignal_response = onesignal_client.send_notification(new_notification)
    print(colour.bold, colour.green, 'SENT NOTIFCATION:', colour.end, colour.green, tweet, colour.end)
except:
    print(colour.bold, colour.red, 'There was an error sending the notification', colour.end)

#Website

tweet = str(tweet)
url = 'INSERT-URL-HERE'
request = {'message': tweet}

try:
    x = requests.post(url, json = request, headers = {"Authorization": "INSERT-AUTH-HERE"})
    print(colour.bold, colour.green, 'UPDATED SITE:', colour.end, colour.green, tweet, colour.end)
except: 
    print(colour.bold, colour.red, 'There was an error updating the website', colour.end)
