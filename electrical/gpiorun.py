import Adafruit_BBIO.GPIO as GPIO
import importlib

def gpio_handler(q_gpio):
    '''
    SETUP GPIO HERE
    '''
    GPIO.setup("P8_8", GPIO.OUT)
    GPIO.setup("P8_7", GPIO.OUT)

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

            if queueHead == "red":
                print queueArgs
                module = importlib.import_module(
                        'electrical.reactions.red'
                )
                gpioFunc = getattr(module, "react_chat_red")

                gpioFunc(queueArgs, GPIO)

                #react_chat_red(queueEvent, GPIO)
            if queueHead == "green":
                return "TODO"
                #react_chat_red(queueEvent, GPIO)
            if queueHead == "xmas":
                return "TODO"
                #react_chat_red(queueEvent, GPIO)


