import time

def react_chat_newfollower(eventType, GPIO, spi):
    stripframe = [
            #0E3774

            [0xE1, 0x74, 0x37, 0x0E],
            [0xE3, 0x74, 0x37, 0x0E],
            [0xE7, 0x74, 0x37, 0x0E],
            [0xEF, 0x74, 0x37, 0x0E],
            [0xFF, 0x74, 0x37, 0x0E],
            [0xEF, 0x74, 0x37, 0x0E],
            [0xE7, 0x74, 0x37, 0x0E],
            [0xE3, 0x74, 0x37, 0x0E],
            [0xE1, 0x74, 0x37, 0x0E],

            #AF7107
            [0xE1, 0x07, 0x71, 0xAF],
            [0xE3, 0x07, 0x71, 0xAF],
            [0xE7, 0x07, 0x71, 0xAF],
            [0xEF, 0x07, 0x71, 0xAF],
            [0xFF, 0x07, 0x71, 0xAF],
            [0xEF, 0x07, 0x71, 0xAF],
            [0xE7, 0x07, 0x71, 0xAF],
            [0xE3, 0x07, 0x71, 0xAF],
            [0xE1, 0x07, 0x71, 0xAF],

            ]
    k = 0
    for x in range(50):
        ledcount = 120
        blue = 0xEF

        spi.writebytes([0x00, 0x00, 0x00, 0x00])

        i = 0
        j = 0 + k
        while i < ledcount:
            spi.writebytes(stripframe[j])
            i += 1
            j += 1
            if j == len(stripframe): j = 0

        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        k += 1
        if k == len(stripframe): k = 0
        time.sleep(0.08)

    spi.writebytes([0x00, 0x00, 0x00, 0x00])

    for x in range(ledcount):
        spi.writebytes([0xE0, 0x01, 0x01, 0x01])

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])

'''
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
'''
