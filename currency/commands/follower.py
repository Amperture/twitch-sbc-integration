from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from twitchapi import db_models

def react_chat_follower(args, **kwargs):
    followerId = args[0]
    followerName = args[1]
    followerDisplay = args[2]
    print("Checking for new follower: %s" % followerDisplay)

    followerCheck = kwargs['session'].query(db_models.Chatter).filter(
            db_models.Chatter.userId == followerId).first()

    if not followerCheck:
        print("Confirmed new follower not existing user!")
        newFollower = db_models.Chatter(
                userId = followerId,
                name = followerName,
                display = followerDisplay,
                currency = 1,
                totalMinutes = 1,
                follower = True
                )
        kwargs['session'].add(newFollower)
        kwargs['session'].commit()
        print("Preparing Lights Event")
        event = {
                'eventType' : 'electrical',
                'event'     : 'newfollower'
        }
        kwargs['queue'].put(event)
        print("Lights Event Queued")

        print("Preparing Chat Event")
        event = {
                'eventType' : 'twitchchatbot',
                'event'     : ('%s has followed the channel! '
                    'Thank you so much! Enjoy your dancing light '
                    'show!' % followerDisplay)
        }
        kwargs['queue'].put(event)
        print("Chat Event Queued")

    elif followerCheck and (followerCheck.follower == False):
        followerCheck.follower = True
        kwargs['session'].commit()
        print("Preparing Lights Event")
        event = {
                'eventType' : 'electrical',
                'event'     : 'newfollower'
        }
        kwargs['queue'].put(event)
        print("Lights Event Queued")

        print("Preparing Chat Event")
        event = {
                'eventType' : 'twitchchatbot',
                'event'     : ('%s has followed the channel! '
                    'Thank you so much! Enjoy your dancing light '
                    'show!' % followerDisplay)
        }
        kwargs['queue'].put(event)
        print("Chat Event Queued")
