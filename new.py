import tweepy
from hootsweet import HootSweet
import os
import subprocess
import requests
import json
import onesignal as onesignal_sdk
from PIL import Image, ImageDraw, ImageFont
import PIL
import glob
import api

class colour:
    purple = '\033[95m'
    green = '\033[92m'
    red = '\033[91m'
    blue = '\033[94m'
    bold = '\033[1m'
    end = '\033[0m'

circleLogo = Image.open('/Users/noah/Keynotes/logo-sc.png')

def textImage(text):
    image_width = 1024
    image_height = 1024
    img = Image.new('RGB', (image_width, image_height), color=(0, 0, 0))
    # create the canvas
    canvas = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Users/noah/Library/Fonts/Aleo-Light.ttf', size=48)
    text_width, text_height = canvas.textsize(text, font=font)
    print(f"Text width: {text_width}")
    print(f"Text height: {text_height}")
    x_pos = int((image_width - text_width) / 2)
    y_pos = int((image_height - text_height) / 2)
    canvas.text((x_pos, y_pos), text, font=font, fill='#FFFFFF')
    img.save('/Users/noah/Keynotes/image.png',optimize=True,quality=100)
    img.close()
    print('Closed image')
    bgImg = Image.open('/Users/noah/Keynotes/image.png')
    circleLogo = Image.open('/Users/noah/Keynotes/logo-text.png')
    
    bgImg.paste(circleLogo, (770,770), circleLogo)
    print('Pasted image')
    bgImg.save('/Users/noah/Keynotes/image.png',optimize=True,quality=100)
    print('Saved finalimage')
    

#tkinter = Tk()


auth = tweepy.OAuthHandler(api.twitterConsumerKey, api.twitterConsumerSecret)
auth.set_access_token(api.twitterAccessKey, api.twitterAccessSecret)
twitter = tweepy.API(auth)
'''
oneSignal = onesignal_sdk.Client(user_auth_key = api.oneSignalUserKey,
app_auth_key = api.oneSignalAppKey,
app_id = api.oneSignalAppID)

hootClientID = "Your-HootSuite-Client-ID"
client_secret = "Your-HootSuite-Client-Secret"
redirect_uri = "http://redirect.uri/"
'''
print(colour.purple, 'Connected to Twitter and OneSignal API', colour.end)

while True:
    update = input('Enter an update: ')

    imageQ = input('Press any key + enter to add a screenshot ')
    if imageQ == "":
        textImage(text=update)
    else:
        #os.system('screencapture ~/Keynotes/image.png -c -D 2')
        screenshot = Image.open("/Users/noah/Keynotes/image.png")
        # 1840 1488
        screenshot.paste(circleLogo, (1300,950), circleLogo)
        screenshot.save('/Users/noah/Keynotes/image.png',optimize=True,quality=100)
        print('Saved image')
    
    for attempt in range(3):
        try:
            twitterImage = twitter.media_upload('/Users/noah/Keynotes/image.png')
            twitter.update_status(status=update, media_ids=[twitterImage.media_id])
            print('Sent Tweet')
            break
        except:
            print('Error sending Tweet')
            continue
    '''

    image = '/Users/noah/Keynotes/image.png'
    for attempt in range(3):
        try:
            with client(instagramUsername, instagramPassword) as instagram:
                instagram.upload(image, update)
                print('Posted to Instagram')
            break
        except:
            print('Error posting to Instagram')
            continue
    

    siteFile = open('/Users/noah/Documents/Keynotes News/site/post.html', 'w')
    siteFile.seek(0)
    siteFile.truncate(0)
    siteFile.write(update)
    siteFile.close()
    print('Updated file')
    #command = 'cd "/Users/noah/Documents/Keynotes News/site" | git commit post.html -m "Live Updates" | git push'
    subprocess.call(['sh', 'sh /Users/noah/keynotes-git.sh'])
    print('Pushed to git')
    

    

    new_notification = oneSignal.Notification(post_body={
        "contents": {"en": update},
        "included_segments": ["All"]
    })
    
    for attempt in range(3):
        try:
            oneSignalResponse = oneSignal.send_notification(new_notification)
            print('Sent notification')
        except:
            print('Error sending notification')
    

    




'''