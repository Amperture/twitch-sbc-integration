import Adafruit_BBIO.GPIO as GPIO

def green(user, args):
    GREEN_LED = 'P8_7'

    if GPIO.gpio_function(GREEN_LED) != GPIO.OUT:
        GPIO.setup(GREEN_LED, GPIO.OUT)

    if len(args) == 0:
        state = GPIO.input(GREEN_LED)
        print("Red light is...", state)

        if state == 1:
            GPIO.output(GREEN_LED, GPIO.LOW)
        elif state == 0:
            GPIO.output(GREEN_LED, GPIO.HIGH)

        return "Toggling the green light for %s!" % user

    if args[0].lower() == "on" or args[0] == "1":
        GPIO.output(GREEN_LED, GPIO.HIGH)
        return "Turning on the green light for %s!" % user

    if args[0].lower() == "off" or args[0] == "0":
        GPIO.output(GREEN_LED, GPIO.LOW)
        return "Turning on the green light for %s!" % user

    else:
        return "Command usage: \"!green on\" or \"!green off\""
