def green(user, args):
    queueEvent = {
            'eventType' : 'gpio',
    }

    if len(args) == 0:
        queueEvent['event'] = "green toggle"
        queueEvent['msg'] = "Toggling the green light for %s" % user

    elif args[0].lower() == "on" or args[0] == "1":
        queueEvent['event'] = "green on"
        queueEvent['msg'] = "Turning on the green light for %s" % user

    elif args[0].lower() == "off" or args[0] == "0":
        queueEvent['event'] = "green off"
        queueEvent['msg'] = "Turning off the green light for %s" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = "Command usage: \"!green on \" or \"!green off\""

    return queueEvent
