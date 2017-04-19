import Adafruit_BBIO.GPIO as GPIO
import time

def xmas(user, args):
    GREEN_LED = 'P8_7'
    RED_LED = 'P8_8'

    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)

    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)


    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    return "Hey, %s! It's beginning to look a lot like Christmas!" % user

