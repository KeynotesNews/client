import requests
import api

url = 'https://api.keynotesnews.com/delete-content'

while True:
    message = input('Enter ID: ')
    requestData = {"id": message}
    try:
        request = requests.post(url, json = requestData, headers = {"Authorization": api.websiteAuth})
        print(request)
        print('Deleted')
    except: 
        print('There was an error delting the status')
