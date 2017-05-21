#from config import CLIENT_ID, CLIENT_SECRET, CHAT_TOKEN, EDITOR_TOKEN
import time
import ConfigParser
import importlib

'''
from threading import Thread
from Queue import Queue
'''
import multiprocessing
import multiprocessing.queues
import Queue

#from pubsub.pubsubex import pubsubex

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

#q_twitchbeagle = Queue()
q_twitchbeagle = multiprocessing.queues.Queue()

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
    moduleThreads[module]['queue'] = multiprocessing.queues.Queue()
    #TODO: Test performance using multiprocessing vs. threading
    #moduleThreads[module]['thread'] = Thread( 
    moduleThreads[module]['thread'] = multiprocessing.Process( 
            target = moduleThreads[module]['function'],
            args = (q_twitchbeagle, moduleThreads[module]['queue'])
    )
    #moduleThreads[module]['thread'].setDaemon(True)
    moduleThreads[module]['thread'].start()

for thread in moduleThreads:
    print(thread, moduleThreads[thread]['thread'].pid)


while True:
    if not q_twitchbeagle.empty():
        queueEvent = q_twitchbeagle.get()
        eventType = queueEvent['eventType']
        moduleThreads[eventType]['queue'].put(queueEvent)
    time.sleep(0.1)
