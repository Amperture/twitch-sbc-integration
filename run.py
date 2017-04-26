import time

from threading import Thread
from Queue import Queue

from twitchchatbot.twitchchatbotrun import twitchchatbot_handler 
from twitchapi.currency_handler import currency_handler
from electrical.gpiorun import gpio_handler
from timer.timerrun import timer_handler

q_chatbot = Queue()
t_chatbot = Thread(target = twitchchatbot_handler, args=(q_chatbot,))

q_currency = Queue()
t_currency = Thread(target = currency_handler, args=(q_currency,))

q_electrical = Queue()
t_electrical = Thread(target = gpio_handler, args=(q_electrical,))

q_timer = Queue()
t_timer = Thread(target = timer_handler, args=(q_timer,))


t_chatbot.setDaemon(True)
t_chatbot.start()

t_currency.setDaemon(True)
t_currency.start()

t_electrical.setDaemon(True)
t_electrical.start()

t_timer.setDaemon(True)
t_timer.start()

while True:
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

    time.sleep(1)
