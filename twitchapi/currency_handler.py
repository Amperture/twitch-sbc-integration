import requests
import time
import requests.packages.urllib3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from twitchapi import db_models
#import twitchapi.db_models

def currency_handler(chattersQueue):
    requests.packages.urllib3.disable_warnings()

    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    url = "https://tmi.twitch.tv/group/user/amperture/chatters"
    headers = {}

    while(True):
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

        for chatter in chatters:
            chatterDbCheck = session.query(db_models.Chatter).filter(
                    db_models.Chatter.name == chatter).first()
            if chatterDbCheck:
                chatterDbCheck.currency += 1
                chatterDbCheck.totalMinutes += 1
            else: 
                newChatter = db_models.Chatter(
                        name = chatter,
                        currency = 1,
                        totalMinutes = 1,
                        follower = False) 
                session.add(newChatter)
        session.commit()
        print("New points doled out at: " , time.time())
        time.sleep(60)
