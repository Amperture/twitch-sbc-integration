import time

def react_chat_green(eventType, GPIO, spi):
    for x in range(2):
        ledcount = 120
        green = 0

        for x in range(ledcount):
            spi.writebytes([0x00, 0x00, 0x00, 0x00])

            for y in range(x):
                spi.writebytes([0xE0, 0x01, 0x01, 0x01])

            spi.writebytes([0xEF, 0x00, 0x03, 0x00])
            spi.writebytes([0xEF, 0x00, 0x09, 0x00])
            spi.writebytes([0xEF, 0x00, 0x0F, 0x00])
            spi.writebytes([0xEF, 0x00, 0x15, 0x00])
            spi.writebytes([0xEF, 0x00, 0x1A, 0x00])

            for y in range(ledcount - 5 - x):
                spi.writebytes([0xE0, 0x01, 0x01, 0x01])

            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            time.sleep(0.004)

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    for x in range(ledcount):
        spi.writebytes([0xE0, 0x00, 0x00, 0x00])

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])

    '''
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
    '''
