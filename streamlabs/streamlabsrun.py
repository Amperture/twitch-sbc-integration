import requests
from config import STREAMLABS_SECRET, STREAMLABS_ID, STREAMLABS_REDIRECT
from decimal import Decimal
import pprint
import os
import json
import time

def streamlabs_handler(q_twitchbeagle, q_gpio):
    #Grab streamlabs tokens
    with open('slrefreshtoken', 'r') as f: 
        r_token = f.read().strip()

    while True:
        try:
            print("Checking the StreamElements API!")
            url = "https://api.streamelements.com/kappa/v2/tips/59bc175476eed8257aabcf8f"
            querystring = {
                    'offset':0,
                    'limit':1,
                    'sort':'-createdAt',
                    }
            headers = {
                    'accept': 'application/json',
                    'authorization': 'Bearer {}'.format(r_token)
                    }
            time.sleep(10)
            response = requests.get(url, headers=headers, params=querystring)
            pprint.pprint(response.json())
            donationinfo = response.json()['docs'][0]

            '''
            print('amount', donationinfo['donation']['amount'])
            print('donor', donationinfo['donation']['user']['username'])
            print('message', donationinfo['donation']['message'])
            '''

            with open("streamlabs_latest_donation", 'r') as f:
                latestdonation = f.read()

            if latestdonation != donationinfo['_id']:
                queueEvent = {
                        'eventType' : 'electrical',
                        'event'     : 'bits %d' % 
                            int(float(donationinfo['donation']['amount']) * 100)
                }
                q_twitchbeagle.put(queueEvent)
                TWOPLACES = Decimal(10) ** -2
                queueEvent = {
                        'eventType' : 'twitchchatbot',
                        'event'     : 'Donation from %s for $%s.' % (
                            donationinfo['donation']['user']['username'], 
                            Decimal(donationinfo['donation']['amount']).\
                                    quantize(TWOPLACES))
                }
                q_twitchbeagle.put(queueEvent)
                with open("streamlabs_latest_donation", 'w') as f:
                    print(donationinfo['_id'])
                    print("WE ARE WRITING TO THE FILE")
                    f.write(str(donationinfo['_id']))
                    print("WE HAVE WRITTEN TO THE FILE")

        except Exception,e:
            print e 
            pass

        """

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
            with open("streamlabs_latest_donation", 'r') as f:
                latestdonation = int(f.read())
            if latestdonation != donationinfo['donation_id']:
                print(int(float(donationinfo['amount']) * 100))
                queueEvent = {
                        'eventType' : 'electrical',
                        'event'     : 'bits %d' % 
                            int(float(donationinfo['amount']) * 100)
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
            """


