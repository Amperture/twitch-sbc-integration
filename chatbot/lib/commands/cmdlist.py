import Adafruit_BBIO.GPIO as GPIO
from chatbot.lib.commands.parsing import commands

def cmdlist(user, args):


    queueEvent = {
            'eventType' : 'txt',
    }
    queueEvent['msg'] = "GhostyAmp Command List: " + ", ".join(commands)

    return queueEvent

