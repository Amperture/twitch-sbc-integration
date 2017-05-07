import time
import ConfigParser
import importlib

from threading import Thread
from Queue import Queue
#from pubsub.pubsubex import pubsubex

'''
from twitchchatbot.twitchchatbotrun import twitchchatbot_handler 
from twitchapi.currency_handler import currency_handler
from electrical.gpiorun import gpio_handler
from timer.timerrun import timer_handler
from twitchapi.twitchapirun import twitchapi_handler
'''

'''
Currently "enabled" modules:
    - twitchchatbot
    - currency
    - electrical
    - timer
    - twitchapi
'''

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

q_twitchbeagle = Queue()

enabledModules = Config.get('MODULES', 'enabled').split(',')
moduleThreads = {}

for module in enabledModules:
    moduleThreads[module] = {}
    moduleThreads[module]['import'] = importlib.import_module(
            '%s.%srun' % (module, module)
    ) 
    moduleThreads[module]['function'] = getattr(
            moduleThreads[module]['import'],
            '%s_handler' % module
    )
    moduleThreads[module]['thread'] = Thread( 
            target = moduleThreads[module]['function'],
            args = (q_twitchbeagle,)
    )
    moduleThreads[module]['thread'].setDaemon(True)
    moduleThreads[module]['thread'].start()

#pubsubex(q_twitchbeagle)
    
    
'''
q_chatbot = Queue()
t_chatbot = Thread(target = twitchchatbot_handler, args=(q_chatbot,))

q_currency = Queue()
t_currency = Thread(target = currency_handler, args=(q_currency,))

q_electrical = Queue()
t_electrical = Thread(target = gpio_handler, args=(q_electrical,))

q_timer = Queue()
t_timer = Thread(target = timer_handler, args=(q_timer,))

q_twitchapi = Queue()
t_twitchapi = Thread(target = twitchapi_handler, args=(q_twitchapi,))


t_chatbot.setDaemon(True)
t_chatbot.start()

t_currency.setDaemon(True)
t_currency.start()

t_electrical.setDaemon(True)
t_electrical.start()

t_timer.setDaemon(True)
t_timer.start()

t_twitchapi.setDaemon(True)
t_twitchapi.start()
'''

while True:
    time.sleep(1)
'''
    if not q_chatbot.empty():
        q_chatbot_get = q_chatbot.get()

        if q_chatbot_get['eventType'] == "gpio":
            q_electrical.put(q_chatbot_get)
        else:
            q_chatbot.put(q_chatbot_get)

    if not q_timer.empty():
        q_timer_get = q_timer.get()

        if q_timer_get['eventType'] == "chat":
            print (q_timer_get)
            q_chatbot.put(q_timer_get)
        else:
            q_timer.put(q_timer_get)

    if not q_twitchapi.empty():
        q_twitchapi_get = q_twitchapi.get()

        if q_twitchapi_get['eventType'] == "gpio":
            print (q_twitchapi_get)
            q_chatbot.put(q_twitchapi_get)
        else:
            q_twitchapi.put(q_twitchapi_get)
'''
