import requests
import api

url = 'https://api.keynotesnews.com/post-content'

while True:
    message = input('Enter message: ')
    requestData = {"content": message)
    try:
        request = requests.post(url, json = requestData, headers = {"Authorization": api.websiteAuth})
        print(request)
        print('UPDATED SITE')
    except: 
        print('There was an error updating the website')


