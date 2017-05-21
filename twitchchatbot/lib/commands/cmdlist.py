import Adafruit_BBIO.GPIO as GPIO
from twitchchatbot.lib.commands.parsing import commands

def cmdlist(user, args):
    queueEvent = {}
    queueEvent['msg'] = "GhostyAmp Command List: " + ", ".join(commands)
    return queueEvent

