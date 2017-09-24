import requests
import importlib
import time
import json
import ConfigParser
import logging
import traceback

from logging.handlers import RotatingFileHandler
from datetime import datetime
from twitchapi.krakenv5 import channels

def twitchapi_handler(q_twitchbeagle, q_twitchapi): 

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.ERROR)
    handler = RotatingFileHandler("twitchapi-log.txt", maxBytes=10000, 
            backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s' \
           + ' - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    requests.packages.urllib3.disable_warnings()
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    channelName = Config.get('CHAT', 'channel')

    while(True):
        time.sleep(0.05)
        if not q_twitchapi.empty():
            event = q_twitchapi.get()['event'].split(' ')
            eventArgs = list(event)
            eventHead = event[0]
            eventArgs.remove(eventHead)
            module = importlib.import_module(
                    'twitchapi.commands.%s' % eventHead
                    )
            apiFunc = getattr(module, "react_chat_%s" % eventHead)
            apiFunc(eventArgs)

        checkForNewFollower(channelName, q_twitchbeagle, logger)
        time.sleep(5)

def checkForNewFollower(channel, q_twitchbeagle, logger):
    try:
        followers = channels.getChannelFollowers(channel)
        latestDisplay = followers["follows"][0]['user']['display_name'].encode(
                'utf-8')
        latestUsername = followers["follows"][0]['user']['name']
        latestId = followers["follows"][0]['user']['_id']
        print("FOLLOWCHECK", latestDisplay, latestUsername, latestId)

        event = {
                'eventType' : 'currency',
                'event'     : 'follower %d %s %s' %(latestId, 
                    latestUsername, latestDisplay)
        }

        q_twitchbeagle.put(event)
    except Exception,e:
        logger.error(str(e))
        logger.error(traceback.format_exc())
        time.sleep(30)
        pass

    return 0
