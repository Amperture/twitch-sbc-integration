import Adafruit_BBIO.GPIO as GPIO

def green(user, args):
    queueEvent = {
            'event' : 'gpio'
    }
    GREEN_LED = 'P8_7'

    if GPIO.gpio_function(GREEN_LED) != GPIO.OUT:
        GPIO.setup(GREEN_LED, GPIO.OUT)

    if len(args) == 0:
        state = GPIO.input(GREEN_LED)

        if state == 1:
            GPIO.output(GREEN_LED, GPIO.LOW)
        elif state == 0:
            GPIO.output(GREEN_LED, GPIO.HIGH)

        queueEvent['event'] = "green toggle"
        queueEvent['msg'] = "Toggling the green light for %s" % user
        #return "Toggling the green light for %s!" % user

    elif args[0].lower() == "on" or args[0] == "1":
        GPIO.output(GREEN_LED, GPIO.HIGH)
        queueEvent['event'] = "green on"
        queueEvent['msg'] = "Turning on the green light for %s" % user
        #return "Turning on the green light for %s!" % user

    elif args[0].lower() == "off" or args[0] == "0":
        GPIO.output(GREEN_LED, GPIO.LOW)
        queueEvent['event'] = "green off"
        queueEvent['msg'] = "Turning off the green light for %s" % user
        #return "Turning on the green light for %s!" % user

    else:
        queueEvent['eventType'] = None
        queueEvent['msg'] = ("Command usage: \"!green on\" or \"!green "
         "off\"")
        #return "Command usage: \"!green on\" or \"!green off\""

    return queueEvent
