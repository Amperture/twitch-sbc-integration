import requests
import importlib
import time
import json
import ConfigParser
from twitchapi.krakenv5 import channels

def twitchapi_handler(q_twitchapi): 

    requests.packages.urllib3.disable_warnings()
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    channelName = Config.get('CHAT', 'channel')

    while(True):
        try:
            if not q_twitchapi.empty():
                queueCheck = q_twitchapi.get()
                if queueCheck['eventType'] == 'twitchapi':
                    queueEvent = queueCheck['event'].split(' ')
                    queueHead = queueEvent[0]
                    queueArgs = list(queueEvent)
                    queueArgs.remove(queueHead) 

                    module = importlib.import_module(
                            'twitchapi.commands.%s' % queueHead
                            )
                    print "MODULE IMPORTED"
                    apiFunc = getattr(module, "react_chat_%s" % queueHead)
                    apiFunc(queueArgs)
                else:
                    q_twitchapi.put(queueCheck)

            checkForNewFollower(channelName, q_twitchapi)
            time.sleep(5)
        except Exception,e:
            with open('twitchapi/errors', "a") as f:
                f.write(str(time.time()) + " API ERROR \r\n\r\n" + str(e))
            pass

def checkForNewFollower(channel, q_twitchapi):
    followers = channels.getChannelFollowers(channel)
    latestFollower = followers["follows"][0]['user']['display_name']
    with open('twitchapi/latestfollower', 'r') as f:
        latestKnownFollower = f.read()

    if latestFollower == latestKnownFollower:
        return None
    else:
        with open('twitchapi/latestfollower', "w+") as f:
            f.write(latestFollower)

        queueEvent = {
                'eventType' : 'electrical',
                'event'     : 'newfollower'
        }
        q_twitchapi.put(queueEvent)

        queueEvent = {
                'eventType' : 'twitchchatbot',
                'event'     : ('%s has followed the channel! '
                    'Thank you so much! Enjoy your dancing light '
                    'show!' % latestFollower)
        }
        q_twitchapi.put(queueEvent)


