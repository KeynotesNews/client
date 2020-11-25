from onesignal_sdk.client import Client
import api

oneSignal = Client(app_id = api.oneSignalAppID, rest_api_key = api.oneSignalAppKey, user_auth_key = api.oneSignalUserKey)

update = input("Enter update: ")

notification_body = {
    'contents': {'en': update},
    'included_segments': ['All'],
}

response = oneSignal.send_notification(notification_body)
print(response.body)
