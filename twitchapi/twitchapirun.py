import requests
import importlib
import time
import json
import ConfigParser
from twitchapi.krakenv5 import channels

def twitchapi_handler(q_twitchbeagle, q_twitchapi): 

    requests.packages.urllib3.disable_warnings()
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    channelName = Config.get('CHAT', 'channel')

    while(True):
        time.sleep(0.05)
        try:
            if not q_twitchapi.empty():
                event = q_twitchapi.get()['event'].split(' ')
                eventArgs = list(event)
                eventHead = event[0]
                eventArgs = remove(eventHead)
                module = importlib.import_module(
                        'twitchapi.commands.%s' % eventHead
                        )
                apiFunc = getattr(module, "react_chat_%s" % eventHead)
                apiFunc(eventArgs)

                '''
                queueCheck = q_twitchapi.get()
                if queueCheck['eventType'] == 'twitchapi':
                    queueEvent = queueCheck['event'].split(' ')
                    queueHead = queueEvent[0]
                    queueArgs = list(queueEvent)
                    queueArgs.remove(queueHead) 

                    module = importlib.import_module(
                            'twitchapi.commands.%s' % queueHead
                            )
                    apiFunc = getattr(module, "react_chat_%s" % queueHead)
                    apiFunc(queueArgs)
                else:
                    q_twitchapi.put(queueCheck)
                '''

            checkForNewFollower(channelName, q_twitchbeagle)
            time.sleep(5)
        except Exception,e:
            with open('twitchapi/errors', "a") as f:
                f.write(str(time.time()) + " API ERROR \r\n\r\n" + str(e))
            pass

def checkForNewFollower(channel, q_twitchbeagle):
    followers = channels.getChannelFollowers(channel)

    latestDisplay = followers["follows"][0]['user']['display_name'].encode(
            'utf-8')
    latestUsername = followers["follows"][0]['user']['name']
    latestId = followers["follows"][0]['user']['_id']

    event = {
            'eventType' : 'currency',
            'event'     : 'follower %d %s %s' %(latestId, 
                latestUsername, latestDisplay)

    }
    q_twitchbeagle.put(event)
    '''
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
        '''
