import time

def react_chat_sub(eventType, GPIO):
    GREEN_LED = 'P8_7'
    RED_LED = 'P8_8'
    BLUE_LED = 'P8_9'

    for x in range(4):
        GPIO.output(GREEN_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(RED_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(BLUE_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(GREEN_LED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(RED_LED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(BLUE_LED, GPIO.LOW)
        time.sleep(0.33)
        GPIO.output(BLUE_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(RED_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(GREEN_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(BLUE_LED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(RED_LED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(GREEN_LED, GPIO.LOW)
