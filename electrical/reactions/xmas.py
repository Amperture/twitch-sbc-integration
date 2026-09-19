import time

def react_chat_xmas(eventType, GPIO, spi):
    stripframe = [

            [0xEF, 0x00, 0x01, 0x00],
            [0xEF, 0x00, 0x05, 0x00],
            [0xEF, 0x00, 0x09, 0x00],
            [0xEF, 0x00, 0x0A, 0x00],
            [0xEF, 0x00, 0x0E, 0x00],
            [0xEF, 0x00, 0x12, 0x00],
            [0xEF, 0x00, 0x0E, 0x00],
            [0xEF, 0x00, 0x0A, 0x00],
            [0xEF, 0x00, 0x09, 0x00],
            [0xEF, 0x00, 0x05, 0x00],
            [0xEF, 0x00, 0x01, 0x00],

            [0xEF, 0x00, 0x00, 0x01],
            [0xEF, 0x00, 0x00, 0x05],
            [0xEF, 0x00, 0x00, 0x09],
            [0xEF, 0x00, 0x00, 0x0A],
            [0xEF, 0x00, 0x00, 0x0E],
            [0xEF, 0x00, 0x00, 0x12],
            [0xEF, 0x00, 0x00, 0x0E],
            [0xEF, 0x00, 0x00, 0x0A],
            [0xEF, 0x00, 0x00, 0x09],
            [0xEF, 0x00, 0x00, 0x05],
            [0xEF, 0x00, 0x00, 0x01],

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
    GREEN_LED = 'P8_7'
    RED_LED = 'P8_8'

    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)

    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)

    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_LED, GPIO.LOW)

    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_LED, GPIO.LOW)
    '''
