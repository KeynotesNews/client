import tweepy
from hootsweet import HootSweet
import os
import subprocess
import requests
import json
from onesignal_sdk.client import Client
from PIL import Image, ImageDraw, ImageFont
import PIL
import glob
import api
import datetime
import pyperclip

# Functions
def textImage(text):
    # Image specifics
    image_width = 1024
    image_height = 1024
    img = Image.new('RGB', (image_width, image_height), color=(0, 0, 0))
    canvas = ImageDraw.Draw(img)
    # Text specifics
    font = ImageFont.truetype('/Users/noah/Library/Fonts/Aleo-Light.ttf', size=48)
    text_width, text_height = canvas.textsize(text, font=font)
    x_pos = int((image_width - text_width) / 2)
    y_pos = int((image_height - text_height) / 2)
    # Add text to image
    canvas.text((x_pos, y_pos), text, font=font, fill='#FFFFFF')
    # Save and close image
    img.save('/Users/noah/Keynotes/image.png',optimize=True,quality=100)
    img.close()

# Colours for print 
class colour:
    purple = '\033[95m' # API connections
    green = '\033[92m' # Success
    red = '\033[91m' # Error
    blue = '\033[94m' # General info
    bold = '\033[1m' # All
    end = '\033[0m' # End the font

# Auth
# Twitter
auth = tweepy.OAuthHandler(api.twitterConsumerKey, api.twitterConsumerSecret)
auth.set_access_token(api.twitterAccessKey, api.twitterAccessSecret)
twitter = tweepy.API(auth)
lastTweetID = '1326229055587446792'
username = '@KeynotesNews'
# OneSignal
oneSignal = Client(app_id = api.oneSignalAppID, rest_api_key = api.oneSignalAppKey, user_auth_key = api.oneSignalUserKey)
# Website
websiteURL = 'https://api.keynotesnews.com/post-content'




print(colour.purple, 'Connected to Twitter and OneSignal API', colour.end)

while True:
    # Get update to share
    update = input('Enter an update: ')

    # Choose type of image
    imageQ = input('Press s to add a screenshot, t for a text image, or n to have no image: ')
    if imageQ == "t":
        # Render and save the text image
        textImage(text=update)
        # Twitter
        for attempt in range(3):
            try:
                # Upload to Twitter
                twitterImage = twitter.media_upload('/Users/noah/Keynotes/image.png')
                # Post the Tweet w/ image
                twitterPost = twitter.update_status(status=f'{username} {update}' ,media_ids=[twitterImage.media_id], in_reply_to_status_id = lastTweetID)
                lastTweetID = twitterPost.id_str
                print('Sent Tweet')
                break
            except:
                print('Error sending Tweet:', twitterPost)
                continue

        # Website
        # Compose request
        requestData = {"content": update}
        for attempt in range(3):
            try:
                # POST to the API
                request = requests.post(websiteURL, json = requestData, headers = {'Authorization': api.websiteAuth})
                print('UPDATED SITE')
                break
            except: 
                print('There was an error updating the website:', request)
        
        # OneSignal Notifications
        # Compose the notification
        notificationContent = {
            'contents': {'en': update},
            'included_segments': ['All'],
        }

        for attempt in range(3):
            try:
                # Send the notification
                response = oneSignal.send_notification(notificationContent)
                print('SENT NOTIFICATION')
                break
            except:
                print('There was an error sending the notification:', response.body)
     
    if imageQ == "n":
        # No image
        # Twitter
        for attempt in range(3):
            try:
                # Post the Tweet
                twitterPost = twitter.update_status(status=f'{username} {update}', in_reply_to_status_id = lastTweetID)
                lastTweetID = twitterPost.id_str

                print('Sent Tweet')
                break
            except:
                print('Error sending Tweet:', twitterPost)
                continue

        # Website
        # Compose request
        requestData = {"content": update}
        for attempt in range(3):
            try:
                # POST to the API
                request = requests.post(websiteURL, json = requestData, headers = {'Authorization': api.websiteAuth})
                print('UPDATED SITE')
                break
            except: 
                print('There was an error updating the website:', request)
        
        # OneSignal Notifications
        # Compose the notification
        notificationContent = {
            'contents': {'en': update},
            'included_segments': ['All'],
        }

        for attempt in range(3):
            try:
                # Send the notification
                response = oneSignal.send_notification(notificationContent)
                print('SENT NOTIFICATION')
                break
            except:
                print('There was an error sending the notification:', response.body)

    if imageQ == "s":
        # Screenshot
        # Capture screenshot
        os.system('screencapture -D 3 ~/Keynotes/image.png')


        # Twitter
        for attempt in range(3):
            try:
                # Upload to Twitter
                twitterImage = twitter.media_upload('/Users/noah/Keynotes/image.png')
                # Post the Tweet w/ image
                twitterPost = twitter.update_status(status=f'{username} {update}' ,media_ids=[twitterImage.media_id], in_reply_to_status_id = lastTweetID)
                lastTweetID = twitterPost.id_str

                print('Sent Tweet')
                break
            except:
                print('Error sending Tweet:', twitterPost)
                continue

        # Website
        # Compose request
        requestData = {"content": update}
        for attempt in range(3):
            try:
                # POST to the API
                request = requests.post(websiteURL, json = requestData, headers = {'Authorization': api.websiteAuth})
                print('UPDATED SITE')
                break
            except: 
                print('There was an error updating the website:', request)
        
        # OneSignal Notifications
        # Compose the notification
        notificationContent = {
            'contents': {'en': update},
            'included_segments': ['All'],
        }

        for attempt in range(3):
            try:
                # Send the notification
                response = oneSignal.send_notification(notificationContent)
                print('SENT NOTIFICATION')
                break
            except:
                print('There was an error sending the notification:', response.body)
    


