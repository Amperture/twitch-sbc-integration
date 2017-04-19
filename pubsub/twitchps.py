#!/usr/bin/python2.6

import websocket
import thread
import time
import json

clientID = "3774415"
with open("ampertureoauth", 'r') as f:
    ampOauth = f.read().rstrip('\n')

listenDict = {
        'type':"LISTEN",
        'nonce':"twitchPubSub",
        'data': {
            'topics' : [
                'chat_moderator_actions.' + clientID + '.' + clientID
                ],
            'auth_token': ampOauth
        } 
}

def on_message(ws, message):
    print json.loads(message)

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def ping_socket(ws):
    print("Are we okay now?")
    while True:
        time.sleep(240)
        ws.send(json.dumps(pingDict)) 

def on_open(ws):
    ws.send(json.dumps(listenDict))
    thread.start_new_thread(ping_socket, (ws,))

pingDict = {
        'type': 'PING'
}


if __name__ == "__main__":
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("wss://pubsub-edge.twitch.tv/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()


