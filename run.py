from threading import Thread
from Queue import Queue

from chatbot.bot import run as chatbotrun
from twitchapi.currency_handler import currency_handler
from electrical.gpiorun import gpio_handler

q_chatbot = Queue()
t_chatbot = Thread(target = chatbotrun, args=(q_chatbot,))

q_currency = Queue()
t_currency = Thread(target = currency_handler, args=(q_currency,))

q_electrical = Queue()
t_electrical = Thread(target = gpio_handler, args=(q_electrical,))


t_chatbot.setDaemon(True)
t_chatbot.start()

t_currency.setDaemon(True)
t_currency.start()

t_electrical.setDaemon(True)
t_electrical.start()

while True:
    q_chatbot_get = q_chatbot.get()
    if q_chatbot_get:
        print q_chatbot_get

        if q_chatbot_get['eventType'] == "gpio":
            q_electrical.put(q_chatbot_get)
