def blue(user, args):
    queueEvent = {
            'eventType' : 'electrical',
    }

    if len(args) == 0:
        queueEvent['event'] = "blue toggle"
        queueEvent['msg'] = "Toggling the blue light for %s" % user

    elif args[0].lower() == "on" or args[0] == "1":
        queueEvent['event'] = "blue on"
        queueEvent['msg'] = "Turning on the blue light for %s" % user

    elif args[0].lower() == "off" or args[0] == "0":
        queueEvent['event'] = "blue off"
        queueEvent['msg'] = "Turning off the blue light for %s" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = "Command usage: \"!blue on \" or \"!blue off\""

    return queueEvent
