from twitchchatbot.lib.commands.parsing import commands
import json

def addcom(user, args):
    # Concatenate a list of strings down to a single, space delimited string.
    queueEvent = {
            'eventType' : 'msg'
    }

    if len(args) < 2:
        queueEvent['msg'] = "Proper usage: !addcom <cmd> <Text to send>"

    else:
        commandHead = "!" + args[0]
        commands[commandHead] = {
                'limit' : 10,
                'userbadge' : 'moderator',
                'last_used' : 0

        }
        del args[0]

        commands[commandHead]['return'] = " ".join(args)
        
        with open("commands.json", "w") as f:
            json.dump(commands, f, indent=1)

        queueEvent['msg'] = "%s has added the %s command!" %( \
                user, commandHead)

    return queueEvent
