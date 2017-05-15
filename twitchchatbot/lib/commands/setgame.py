
def setgame(user, args):
    try:
        gameToSet = ' '.join(args)
    except:
        queueEvent = {
                'msg' : ("Hey %s, you need to actually give me a game to "
                    "set!" % user),

                'eventType' : 'electrical',
                'event'     : 'red toggle'
        }
        return queueEvent


    queueEvent = {
            'eventType': 'twitchapi',
            'event'    : 'setgame %s' % gameToSet,
            'msg'      : ('%s is attempting to set channel game.'
                ' Please refresh!'%user)
    }

    return queueEvent
