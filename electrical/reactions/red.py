def react_chat_red(eventType, GPIO):
    RED_LED = 'P8_8'

    if len(eventType) != 0:
        if eventType[0] == "on":
            print("RED ON")
            GPIO.output(RED_LED, GPIO.HIGH)

        elif eventType[0] == "off":
            print("RED OFF")
            GPIO.output(RED_LED, GPIO.LOW)

        elif eventType[0] == "toggle":
            print("RED TOGGLE")
            state = GPIO.input(RED_LED)

            if state == 1:
                GPIO.output(RED_LED, GPIO.LOW)
            elif state == 0:
                GPIO.output(RED_LED, GPIO.HIGH)

