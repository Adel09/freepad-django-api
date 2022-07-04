import requests

class SMSService():
    #Send SMS to recipient informing them of donation
    def donationComplete(phone, pharmacy):
        ENDPOINT = 'https://www.bulksmsnigeria.com/api/v1/sms/create'
        HEADERS = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json'
        }
        
        DATA = {
            "api_token": "ALL LIES",
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
        
        DATA = {
            "api_token": "ALL LIES",
            "to": phone,
            "from": "FreePad",
            "body": f'Thank you for your donation to {title}. We really appreciate',
            "append_sender": "FreePad",
        }
        r = requests.post(url=ENDPOINT, headers=HEADERS, json=DATA)
        print(r.content)
