def react_chat_green(eventType, GPIO):
    GREEN_LED = 'P8_7'

    if len(eventType) != 0:
        if eventType[0] == "on":
            GPIO.output(GREEN_LED, GPIO.HIGH)

        elif eventType[0] == "off":
            GPIO.output(GREEN_LED, GPIO.LOW)

        elif eventType[0] == "toggle":
            state = GPIO.input(GREEN_LED)

            if state == 1:
                GPIO.output(GREEN_LED, GPIO.LOW)
            elif state == 0:
                GPIO.output(GREEN_LED, GPIO.HIGH)
