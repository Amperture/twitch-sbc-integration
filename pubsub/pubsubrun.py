import websocket
import ast
import thread
import time
import json

clientID = "3774415"
psynapsID = "26158435"
with open("pubsub/ampertureoauth", 'r') as f:
    ampOauth = f.read().rstrip('\n')

pingDict = {
        'type': 'PING'
}

listenDict = {
        'type':"LISTEN",
        'nonce':"twitchPubSub",
        'data': {
            'topics' : [
                'chat_moderator_actions.' + clientID + '.' + clientID,
                'channel-bits-events-v1.' + clientID
                ],
            'auth_token': ampOauth
        } 
}

def pubsub_handler(q_twitchbeagle, q_pubsub):

    def on_error(ws, error):
        print error

    def on_close(ws):
        print "### closed ###"

    def ping_socket(ws):
        while True:
            time.sleep(240)
            ws.send(json.dumps(pingDict)) 

    def on_open(ws):
        ws.send(json.dumps(listenDict))
        thread.start_new_thread(ping_socket, (ws,))

    def on_message(ws, message):
        jsonmessage = json.loads(message)
        try: 
            message_check = json.loads(jsonmessage['data']['message'])
            if message_check['message_type'] == 'bits_event':
                queueEvent = {}
                queueEvent['eventType'] = 'electrical'
                queueEvent['event'] = 'bits'
                q_twitchbeagle.put(queueEvent)

                bits_used = str(message_check['data']['bits_used'])
                user_name = message_check['data']['user_name']
                channel_name = message_check['data']['channel_name']

                queueEvent = {}
                queueEvent['eventType'] = 'twitchchatbot'
                queueEvent['event'] = ("Thank you, %s, for sending %s Bit(s) "
                        "to %s!!" % (user_name, bits_used, channel_name))
                q_twitchbeagle.put(queueEvent)

        except: 
            pass

    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("wss://pubsub-edge.twitch.tv/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
