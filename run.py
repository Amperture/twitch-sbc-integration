from threading import Thread
from Queue import Queue

from chatbot.bot import run as chatbotrun
from twitchapi.currency_handler import currency_handler

q_chatbot = Queue()
t_chatbot = Thread(target = chatbotrun, args=(q_chatbot,))

q_currency = Queue()
t_currency = Thread(target = currency_handler, args=(q_currency,))


#t_chatbot.setDaemon(True)
t_chatbot.start()

#t_currency.setDaemon(True)
t_currency.start()

while True:
    print (q_chatbot.get())
