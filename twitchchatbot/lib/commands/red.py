def red(user, args):
    queueEvent = {
            'eventType' : 'electrical',
    }

    if len(args) == 0:
        queueEvent['event'] = "red toggle"
        queueEvent['msg'] = "Hey %s, watch the red lights glow!" % user

    elif args[0].lower() == "on" or args[0] == "1":
        queueEvent['event'] = "red on"
        queueEvent['msg'] = "Hey %s, watch the red lights glow!" % user

    elif args[0].lower() == "off" or args[0] == "0":
        queueEvent['event'] = "red off"
        queueEvent['msg'] = "Hey %s, watch the red lights glow!" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = "Command usage: \"!red on \" or \"!red off\""

    return queueEvent
