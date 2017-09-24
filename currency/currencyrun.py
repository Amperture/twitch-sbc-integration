import requests
import importlib
import time
import logging
from logging.handlers import RotatingFileHandler
from config import CLIENT_ID
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from twitchapi import db_models

def currency_handler(q_twitchbeagle, q_currency):
    requests.packages.urllib3.disable_warnings()

    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    url = "https://tmi.twitch.tv/group/user/amperture/chatters"
    headers = {}
    secondsPassed = 0

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.ERROR)
    handler = RotatingFileHandler("currency-log.txt", maxBytes=10000, 
            backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s' \
           + ' - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    while(True):
        time.sleep(1)
        secondsPassed += 1 
        if not q_currency.empty():
            queueEvent = q_currency.get()['event'].split(' ')
            queueHead = queueEvent[0]
            queueArgs = list(queueEvent)
            queueArgs.remove(queueHead) 

            module = importlib.import_module(
                    'currency.commands.%s' % queueHead
                    )
            apiFunc = getattr(module, "react_chat_%s" % queueHead)
            apiFunc(queueArgs, queue=q_twitchbeagle, session=session)

        if secondsPassed == 60:
            secondsPassed = 0
            r = requests.get(url, headers=headers)
            latest = r.json()
            chatters = []

            for mod in latest['chatters']['moderators']:
                chatters.append(mod)
            for viewer in latest['chatters']['viewers']:
                chatters.append(viewer)
            for global_mod in latest['chatters']['global_mods']:
                chatters.append(global_mod)
            for admin in latest['chatters']['admins']:
                chatters.append(admin)

            chatters = getInfoOnChatters(chatters, logger)

            for chatter in chatters:
                chatterDbCheck = session.query(db_models.Chatter).filter(
                        db_models.Chatter.userId == chatter['_id']).first()
                if chatterDbCheck:
                    chatterDbCheck.currency += 1
                    chatterDbCheck.totalMinutes += 1
                else: 
                    newChatter = db_models.Chatter(
                            userId = chatter['_id'],
                            name = chatter['name'],
                            display = chatter['display_name'],
                            currency = 1,
                            totalMinutes = 1,
                            follower = False) 
                    session.add(newChatter)
            session.commit()

def getInfoOnChatters(chatters, logger):
    usersUrl = "https://api.twitch.tv/kraken/users"
    payload = {
            'login': ','.join(chatters)
    }
    header = {
        u'Accept': u'application/vnd.twitchtv.v5+json',
        u'Content-Type': u'application/json',
        u'Client-ID'   : CLIENT_ID
    }
    while True:
        r = requests.get(usersUrl, headers=header, params=payload)

        try: 
            if r.status_code == 200:
                return r.json()['users']
            else:
                time.sleep(20)

        except Exception,e:
            logger.error(str(e))
            logger.error(traceback.format_exc())
            time.sleep(30)
            pass
