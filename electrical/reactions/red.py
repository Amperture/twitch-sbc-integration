import time

def react_chat_red(eventType, GPIO, spi):
    print "RUNNING THE RED COMMAND"
    for x in range(3):
        ledcount = 120
        red = 0

        while red <= 0x0F:
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            for x in range(ledcount):
                spi.writebytes([0xEF, 0x00, 0x00, red])
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            time.sleep(0.02)

            red += 1

        while red > 0:
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            for x in range(ledcount):
                spi.writebytes([0xEF, 0x00, 0x00, red])
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            spi.writebytes([0x00, 0x00, 0x00, 0x00])
            red -= 1
            time.sleep(0.02)

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    for x in range(ledcount):
        spi.writebytes([0xE0, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    red -= 1
    time.sleep(0.02)

    '''
    RED_LED = 'P8_8'

    if len(eventType) != 0:
        if eventType[0] == "on":
            GPIO.output(RED_LED, GPIO.HIGH)

        elif eventType[0] == "off":
            GPIO.output(RED_LED, GPIO.LOW)

        elif eventType[0] == "toggle":
            state = GPIO.input(RED_LED)

            if state == 1:
                GPIO.output(RED_LED, GPIO.LOW)
            elif state == 0:
                GPIO.output(RED_LED, GPIO.HIGH)
'''
