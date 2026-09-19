import time
import random

def react_chat_bits(eventType, GPIO, spi):

    '''
    colors:
        1 bit = 69696a
        100 bits = 9647f0
        1000 bits = 11ebda
        5000 bits = 2665c1
        10000 bits = fd342e
    '''
    
    onebit = [0xEF, 0x6A, 0x69, 0x69]
    hundredbits = [0xEF, 0x6A, 0x47, 0x96]
    onekbits = [0xEF, 0xDA, 0xeb, 0x11]
    fivekbits = [0xEF, 0xC1, 0x65, 0x26]
    tenkbits = [0xEF, 0x2E, 0x34, 0xFD]

    if len(eventType) != 0:
        bitsAmount = int(eventType[0])
    else: 
        bitsAmount = random.randrange(1, 10000)

    if bitsAmount >= 1: 
        bitsColor = onebit
    if bitsAmount >= 100: 
        bitsColor = hundredbits
    if bitsAmount >= 1000: 
        bitsColor = onekbits
    if bitsAmount >= 5000: 
        bitsColor = fivekbits
    if bitsAmount >= 10000: 
        bitsColor = tenkbits

    ledcount = 120

    for x in range(ledcount):
        time.sleep(0.01)
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        for y in range(ledcount):
            if y <= x: spi.writebytes(bitsColor)
            else: spi.writebytes([0xE0, 0x00, 0x00, 0x00])
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        spi.writebytes([0x00, 0x00, 0x00, 0x00])

    for x in range(ledcount):
        time.sleep(0.01)
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        for y in range(ledcount):
            if y <= x: spi.writebytes([0xE0, 0x00, 0x00, 0x00])
            else: spi.writebytes(bitsColor)
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        spi.writebytes([0x00, 0x00, 0x00, 0x00])
        spi.writebytes([0x00, 0x00, 0x00, 0x00])

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    for x in range(ledcount):
        spi.writebytes([0xE0, 0x00, 0x00, 0x00])

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])
