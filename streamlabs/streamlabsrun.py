import requests
from config import STREAMLABS_SECRET, STREAMLABS_ID, STREAMLABS_REDIRECT
from decimal import Decimal
import pprint
import os
import json
import time

def streamlabs_handler(q_twitchbeagle, q_gpio):
    #Grab streamlabs tokens

    headers = []
    while True:
        try:
            with open('slrefreshtoken', 'r') as f:
                r_token = f.read()

            with open('slaccesstoken', 'r') as f:
                a_token = f.read()

            token_call = {
                    'grant_type'    : 'refresh_token',
                    'client_id'     : STREAMLABS_ID,
                    'client_secret' : STREAMLABS_SECRET,
                    'redirect_uri'  : STREAMLABS_REDIRECT,
                    'refresh_token' : r_token
            }
            donations_params = { 
                    'access_token' : a_token,
                    'limit'        : 1, 
                    'currency'     : "USD"
            }
            time.sleep(10)
            r = requests.post(
                    'https://streamlabs.com/api/v1.0/token',
                    data = token_call,
                    headers = headers
            )
            a_token = r.json()['access_token']
            r_token = r.json()['refresh_token']

            with open('slaccesstoken', 'w') as f:
                f.write(a_token)
                donations_params['access_token'] = a_token
            with open('slrefreshtoken', 'w') as f:
                f.write(r_token)

            donationsurl = "https://streamlabs.com/api/v1.0/donations"

            donate = requests.get(
                    donationsurl,
                    headers = headers,
                    params = donations_params
            )
            #usd_two_places = float(format(usd_value, '.2f')))
            donationinfo = donate.json()['data'][0]
            #print('amount', donationinfo['amount'])
            #print('donor', donationinfo['name'])
            #print('message', donationinfo['message'])
            with open("streamlabs_latest_donation", 'r') as f:
                latestdonation = int(f.read())
            if latestdonation != donationinfo['donation_id']:
                queueEvent = {
                        'eventType' : 'electrical',
                        'event'     : 'bits'
                }
                q_twitchbeagle.put(queueEvent)
                TWOPLACES = Decimal(10) ** -2
                queueEvent = {
                        'eventType' : 'twitchchatbot',
                        'event'     : 'Donation from %s for $%s.' % (
                            donationinfo['name'], 
                            Decimal(donationinfo['amount']).\
                                    quantize(TWOPLACES))
                }
                q_twitchbeagle.put(queueEvent)
                with open("streamlabs_latest_donation", 'w') as f:
                    print(donationinfo['donation_id'])
                    print("WE ARE WRITING TO THE FILE")
                    f.write(str(donationinfo['donation_id']))
                    print("WE HAVE WRITTEN TO THE FILE")

        except Exception,e:
            print e
            pass

