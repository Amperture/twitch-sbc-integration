import Adafruit_BBIO.GPIO as GPIO
from twitchchatbot.lib.commands.parsing import commands

def lights(user, args):
    queueEvent = {}
    queueEvent['msg'] = "The lights are part of Amp's Twitch Beagle Project, they will react with animations for events such as channel follows, subscriptions, bits, donations and chat commands! Type !cmdlist for a list of chat commands!"
    return queueEvent

