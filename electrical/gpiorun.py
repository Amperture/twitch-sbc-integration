import ConfigParser
import Adafruit_BBIO.GPIO as GPIO
import importlib

def gpio_handler(q_gpio):
    '''
    SETUP GPIO HERE
    '''
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')

    gpioOutSetup = Config.get('GPIO', 'out').split(',')
    gpioInSetup = Config.get('GPIO', 'in').split(',')

    for setup in gpioOutSetup:
        GPIO.setup(setup, GPIO.OUT)

    for setup in gpioInSetup:
        GPIO.setup(setup, GPIO.IN)
        
    while True:
        '''
        CHECK q_gpio for messages, execute messages accordingly
        '''
        q_gpio_check = q_gpio.get()
        if q_gpio_check:

            queueEvent = q_gpio_check['event'].split(' ')
            queueHead = queueEvent[0]
            queueArgs = list(queueEvent)
            queueArgs.remove(queueHead) 

            module = importlib.import_module(
                    'electrical.reactions.%s' % queueHead
                    )
            gpioFunc = getattr(module, "react_chat_%s" % queueHead)
            gpioFunc(queueArgs, GPIO)
