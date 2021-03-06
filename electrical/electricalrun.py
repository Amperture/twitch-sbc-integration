import ConfigParser
import Adafruit_BBIO.GPIO as GPIO
import importlib
import time

def electrical_handler(q_twitchbeagle, q_gpio):
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')

    gpioOutSetup = Config.get('GPIO', 'out').split(',')
    gpioInSetup = Config.get('GPIO', 'in').split(',')

    for setup in gpioOutSetup:
        GPIO.setup(setup, GPIO.OUT)

    for setup in gpioInSetup:
        GPIO.setup(setup, GPIO.IN)
        
    while True:
        time.sleep(0.05)
        if not q_gpio.empty():
            queueEvent = q_gpio.get()['event'].split(' ')
            queueHead = queueEvent[0]
            queueArgs = list(queueEvent)
            queueArgs.remove(queueHead) 

            module = importlib.import_module(
                    'electrical.reactions.%s' % queueHead
                    )
            gpioFunc = getattr(module, "react_chat_%s" % queueHead)
            gpioFunc(queueArgs, GPIO)
