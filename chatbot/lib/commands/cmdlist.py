import Adafruit_BBIO.GPIO as GPIO
from chatbot.lib.command_headers import commands

def cmdlist(user, args):


    queueEvent = {
            'eventType' : 'txt',
    }
    queueEvent['msg'] = "GhostyAmp Command List: " + ", ".join(commands)

    return queueEvent



'''
MAIN PROGRAM:
    -- Chatbot (GhostyAmp)
    -- Twitch API (New followers)
    -- Chatters (Currency)
    -- PubSub (Mod Logs, New Subs, Bits) 
    -- Streamlabs (Paypal/CC, Bitcoin donations)
    -- Fizz (Physical Interactions/Reactions)
'''
