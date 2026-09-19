def green(user, args):
    queueEvent = {
            'eventType' : 'electrical',
    }

    if len(args) == 0:
        queueEvent['event'] = "green toggle"
        queueEvent['msg'] = "Oh no! There's a green Python chasing %s!" % user

    elif args[0].lower() == "on" or args[0] == "1":
        queueEvent['event'] = "green on"
        queueEvent['msg'] = "Oh no! There's a green Python chasing %s!" % user

    elif args[0].lower() == "off" or args[0] == "0":
        queueEvent['event'] = "green off"
        queueEvent['msg'] = "Oh no! There's a green Python chasing %s!" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = "Command usage: \"!green on \" or \"!green off\""

    return queueEvent
