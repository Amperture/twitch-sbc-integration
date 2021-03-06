def red(user, args):
    queueEvent = {
            'eventType' : 'electrical',
    }

    if len(args) == 0:
        queueEvent['event'] = "red toggle"
        queueEvent['msg'] = "Toggling the red light for %s" % user

    elif args[0].lower() == "on" or args[0] == "1":
        queueEvent['event'] = "red on"
        queueEvent['msg'] = "Turning on the red light for %s" % user

    elif args[0].lower() == "off" or args[0] == "0":
        queueEvent['event'] = "red off"
        queueEvent['msg'] = "Turning off the red light for %s" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = "Command usage: \"!red on \" or \"!red off\""

    return queueEvent
