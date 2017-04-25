def react_chat_green(eventType, GPIO):
    GREEN_LED = 'P8_7'

    if len(eventType) != 0:
        if eventType[0] == "on":
            print("GREEN ON")
            GPIO.output(GREEN_LED, GPIO.HIGH)

        elif eventType[0] == "off":
            print("GREEN OFF")
            GPIO.output(GREEN_LED, GPIO.LOW)

        elif eventType[0] == "toggle":
            print("GREEN TOGGLE")
            state = GPIO.input(GREEN_LED)

            if state == 1:
                GPIO.output(GREEN_LED, GPIO.LOW)
            elif state == 0:
                GPIO.output(GREEN_LED, GPIO.HIGH)
