import time

def react_chat_bits(eventType, GPIO):

    GREEN_LED = 'P8_7'

    for x in range(10):
        GPIO.output(GREEN_LED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(GREEN_LED, GPIO.HIGH)
        time.sleep(0.1)
