import Adafruit_BBIO.GPIO as GPIO

def red(user, args):
    RED_LED = 'P8_8'

    if GPIO.gpio_function(RED_LED) != GPIO.OUT:
        GPIO.setup(RED_LED, GPIO.OUT)

    if len(args) == 0:
        state = GPIO.input(RED_LED)
        print("Red light is...", state)

        if state == 1:
            GPIO.output(RED_LED, GPIO.LOW)
        elif state == 0:
            GPIO.output(RED_LED, GPIO.HIGH)

        return "Toggling the red light for %s!" % user

    if args[0].lower() == "on" or args[0] == "1":
        GPIO.output(RED_LED, GPIO.HIGH)
        return "Turning on the red light for %s!" % user

    if args[0].lower() == "off" or args[0] == "0":
        GPIO.output(RED_LED, GPIO.LOW)
        return "Turning on the red light for %s!" % user

    else:
        return "Command usage: \"!red on\" or \"!red off\""

