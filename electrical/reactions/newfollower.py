import time

def react_chat_newfollower(eventType, GPIO):
    RED_LED = "P8_8"
    GREEN_LED = "P8_7"

    GPIO.setup("P8_7", GPIO.OUT)
    GPIO.setup("P8_8", GPIO.OUT)

    GPIO.output(GREEN_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(RED_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(GREEN_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(RED_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(GREEN_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(RED_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(GREEN_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.output(RED_LED, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(GREEN_LED, GPIO.LOW)
