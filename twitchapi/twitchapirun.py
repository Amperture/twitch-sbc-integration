import requests
import serial
import time
import json

def twitchapi_handler(q_twitchapi): 
    with open('LaunchpadBot_ClientID', 'r') as f:
        client_id = f.read().strip()

    url = "https://api.twitch.tv/kraken/channels/amperture/follows"
    headers = {
            'Client-ID': client_id
            }

    requests.packages.urllib3.disable_warnings()

    while(True):
        try:
            r = requests.get(url, headers=headers)

            reqReturn = r.json()
            latest = r.json()["follows"][0]['user']['display_name']

            with open('twitchapi/latestfollower', "r") as f:
                stored = f.read()

            if latest != stored:
                with open('twitchapi/latestfollower', "w+") as f:
                        f.write(latest)
                queueEvent = {
                        'eventType' : 'electrical',
                        'event'     : 'newfollower'
                }
                q_twitchapi.put(queueEvent)

                queueEvent = {
                        'eventType' : 'twitchchatbot',
                        'event'     : ('%s has followed the channel! '
                            'Thank you so much! Enjoy your dancing light '
                            'show!' % latest)
                }
                q_twitchapi.put(queueEvent)

            time.sleep(5)
        except:
            with open('twitchapi/errors', "a") as f:
                f.write(time.time() + " API ERROR \r\n\r\n" + reqReturn)
            print reqReturn
            pass
