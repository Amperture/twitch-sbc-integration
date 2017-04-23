import Adafruit_BBIO.GPIO as GPIO

def red(user, args):
    RED_LED = 'P8_8'

    if GPIO.gpio_function(RED_LED) != GPIO.OUT:
        GPIO.setup(RED_LED, GPIO.OUT)

    queueEvent = {
            'eventType' : 'gpio',
    }

    if len(args) == 0:
        '''
        state = GPIO.input(RED_LED)

        if state == 1:
            GPIO.output(RED_LED, GPIO.LOW)
        elif state == 0:
            GPIO.output(RED_LED, GPIO.HIGH)
        '''

        queueEvent['event'] = "red toggle"
        queueEvent['msg'] = "Toggling the red light for %s" % user
        #return "Toggling the red light for %s!" % user

    elif args[0].lower() == "on" or args[0] == "1":
        #GPIO.output(RED_LED, GPIO.HIGH)
        queueEvent['event'] = "red on"
        queueEvent['msg'] = "Turning on the red light for %s" % user
        #return "Turning on the red light for %s!" % user

    elif args[0].lower() == "off" or args[0] == "0":
        #GPIO.output(RED_LED, GPIO.LOW)
        queueEvent['event'] = "red off"
        queueEvent['msg'] = "Turning off the red light for %s" % user
        #return "Turning on the red light for %s!" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = "Command usage: \"!red on \" or \"!red off\""
        #return "Command usage: \"!red on\" or \"!red off\""

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
