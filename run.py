from threading import Thread
from Queue import Queue

from chatbot.bot import run as chatbotrun

q_chatbot = Queue()
t_chatbot = Thread(target = chatbotrun, args=(q_chatbot,))

t_chatbot.setDaemon(True)
t_chatbot.start()

while True:
    print (q_chatbot.get())
