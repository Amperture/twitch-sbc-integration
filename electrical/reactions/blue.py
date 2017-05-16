
def react_chat_blue(eventType, GPIO):
    BLUE_LED = 'P8_9'

    if len(eventType) != 0:
        if eventType[0] == "on":
            GPIO.output(BLUE_LED, GPIO.HIGH)

        elif eventType[0] == "off":
            GPIO.output(BLUE_LED, GPIO.LOW)

        elif eventType[0] == "toggle":
            state = GPIO.input(BLUE_LED)

            if state == 1:
                GPIO.output(BLUE_LED, GPIO.LOW)
            elif state == 0:
                GPIO.output(BLUE_LED, GPIO.HIGH)

