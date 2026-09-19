import time
import random

ledcount = 120

sparkleGradient = [
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
        0x06,
        0x07,
        0x08,
        0x09,
        0x0A,
        0x0B,
        0x0C,
        0x0D,
        0x0E,
        0x0F,
        0x0E,
        0x0D,
        0x0C,
        0x0B,
        0x0A,
        0x09,
        0x08,
        0x07,
        0x06,
        0x05,
        0x04,
        0x03,
        0x02,
        0x01
        ]


def stripSparkles(spi, state):
    time.sleep(0.01)
    spi.writebytes([0x00, 0x00, 0x00, 0x00])

    for y in range(ledcount):
        if y in state:
            spi.writebytes([0xEF, state[y], 0x00, 0x00])
        else: 
            spi.writebytes([0xE0, 0x00, 0x00, 0x00])

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])

def react_chat_blue(eventType, GPIO, spi):

    sparkleCount = 40
    spi.writebytes([0,0,0,0])

    randomSparkles = []
    for x in range(sparkleCount):
        randomSparkles.append( random.randrange(0,ledcount) )

    stateMap = {}
    for x in range(sparkleCount):
        stateMap[randomSparkles[x]] = 0x00

    for i in range(sparkleCount + len(sparkleGradient)):
        for j in range(sparkleCount):
            if (j <= i) and (j >= i - len(sparkleGradient) ):
                sparkGradZero = i - len(sparkleGradient) + 1
                gradSpark = j - sparkGradZero
                stateMap[randomSparkles[j]] = sparkleGradient[gradSpark]
            #else if (j < i) or (j > i + len(sparkleGradient):
            else: 
                stateMap[randomSparkles[j]] = 0x00
        stripSparkles(spi, stateMap)

    spi.writebytes([0x00, 0x00, 0x00, 0x00])

    for y in range(ledcount):
        spi.writebytes([0xE0, 0x00, 0x00, 0x00])

    spi.writebytes([0x00, 0x00, 0x00, 0x00])
    spi.writebytes([0x00, 0x00, 0x00, 0x00])


