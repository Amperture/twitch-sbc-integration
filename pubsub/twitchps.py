#!/usr/bin/python2.6

import websocket
import thread
import time
import json
import pprint

clientID = "3774415"
psynapsID = "26158435"
with open("ampertureoauth", 'r') as f:
    ampOauth = f.read().rstrip('\n')

listenDict = {
        'type':"LISTEN",
        'nonce':"twitchPubSub",
        'data': {
            'topics' : [
                'channel-bits-events-v1.' + clientID
                ],
            'auth_token': ampOauth
        } 
}

def on_message(ws, message):
    jsonmessage = json.loads(message)
    print(jsonmessage)
    try: 
        jsonmessage2 = json.loads(jsonmessage['data']['message'])
        if message_check['message_type'] == 'bits_event':
            print("BITS SENT: " + str(message_check['data']['bits_used']))
            print("SENT FROM: " + message_check['data']['user_name'])
            print("SENT TO: " + message_check['data']['channel_name'])

    except: 
        pass
    
    '''
    for key, value in jsonmessage[0]:
        try:
            if key == "type":
                print value
        except:
            pass
    '''

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


