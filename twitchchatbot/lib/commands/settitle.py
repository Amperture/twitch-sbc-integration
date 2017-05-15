def settitle(user, args):
    try:
        titleToSet = ' '.join(args)
    except:
        queueEvent = {
                'msg' : ("Hey %s, you need to actually give me a title to "
                    "set!" % user),

                'eventType' : 'electrical',
                'event'     : 'red toggle'
        }
        return queueEvent


    queueEvent = {
            'eventType': 'twitchapi',
            'event'    : 'settitle %s' % titleToSet,
            'msg'      : ('%s is attempting to set channel title.'
                ' Please refresh!'%user)
    }

    return queueEvent
