import requests

class SMSService():

    def donationComplete(phone, pharmacy):
        ENDPOINT = 'https://www.bulksmsnigeria.com/api/v1/sms/create'
        HEADERS = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json'
        }
        #Bearer FLWSECK-6aad26f4c82fc347d8e1c98ed32fb5f4-X
        DATA = {
            "api_token": "p0E9gMfwDQBdgEPCLwe5aWQe0KadA3Imod50lWRN3YF8RCuIOwILZ9RpyER6",
            "to": phone,
            "from": "FreePad",
            "body": f'Your request has been fulfilled! You can pickup your pad at {pharmacy}',
            "append_sender": "FreePad",
        }
        r = requests.post(url=ENDPOINT, headers=HEADERS, json=DATA)
        print(r.content)

    def donationThanks(phone, title):
        ENDPOINT = 'https://www.bulksmsnigeria.com/api/v1/sms/create'
        HEADERS = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json'
        }
        #Bearer FLWSECK-6aad26f4c82fc347d8e1c98ed32fb5f4-X
        DATA = {
            "api_token": "p0E9gMfwDQBdgEPCLwe5aWQe0KadA3Imod50lWRN3YF8RCuIOwILZ9RpyER6",
            "to": phone,
            "from": "FreePad",
            "body": f'Thank you for your donation to {title}. We really appreciate',
            "append_sender": "FreePad",
        }
        r = requests.post(url=ENDPOINT, headers=HEADERS, json=DATA)
        print(r.content)