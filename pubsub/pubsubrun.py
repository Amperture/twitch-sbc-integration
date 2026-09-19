import websocket
import ast
import thread
import time
import json
import ConfigParser
from twitchapi.krakenv5.channels import getChannelId
from config import EDITOR_TOKEN

config = ConfigParser.ConfigParser()
config.read('config.ini')


pingDict = {
        'type': 'PING'
}

channelId = str(getChannelId(config.get('CHAT', 'channel')))

listenDict = {
        'type':"LISTEN",
        'nonce':"twitchPubSub",
        'data': {
            'topics' : [
                'chat_moderator_actions.' + channelId + '.' + channelId,
                'channel-bits-events-v1.' + channelId,
                'channel-subscribe-events-v1.' + channelId
                ],
            'auth_token': EDITOR_TOKEN
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
        print(jsonmessage)
        print(type(jsonmessage))
        if jsonmessage['type'] != 'PONG' and jsonmessage['type'] != 'RESPONSE': 
            print(jsonmessage['data']['topic'])

        try: 
            message_check = jsonmessage['data']
            if ("topic" in message_check) and \
                    message_check['topic'] == 'channel-bits-events-v1.%s' \
                    % channelId:
                print("BITS EVENT DETECTED")
                message_bits = json.loads(message_check['message'])
                bits_used = str(message_bits['data']['bits_used'])
                print(bits_used)
                queueEvent = {}
                queueEvent['eventType'] = 'electrical'
                queueEvent['event'] = 'bits %s' % bits_used
                print(queueEvent)
                q_twitchbeagle.put(queueEvent)


                message_bits = json.loads(message_check['message'])
                user_name = message_bits['data']['user_name']
                channel_name = message_bits['data']['channel_name']

                queueEvent = {}
                queueEvent['eventType'] = 'twitchchatbot'
                queueEvent['event'] = ("Thank you, %s, for sending %s Bit(s) "
                        "to %s!!" % (user_name, bits_used, channel_name))
                print(queueEvent)
                q_twitchbeagle.put(queueEvent)


            
            elif "topic" in message_check and \
                message_check['topic'] == 'channel-subscribe-events-v1.%s' \
                % channelId:

                print ("SUBSCRIBE EVENT DETECTED")

                queueEvent = {}
                queueEvent['eventType'] = 'electrical'
                queueEvent['event'] = 'sub'
                q_twitchbeagle.put(queueEvent)

                subMsgJson = json.loads(message_check['message'])
                user_name = subMsgJson['display_name']

                print(user_name)
                channel_name = subMsgJson['channel_name']
                print(channel_name)

                queueEvent = {}
                queueEvent['eventType'] = 'twitchchatbot'
                if "recipient_display_name" in subMsgJson:
                    sub_recipient = subMsgJson['recipient_display_name']
                    queueEvent['event'] = ("%s just gifted a subscription to "
                            "%s!! Thank you both!" 
                            % (user_name, sub_recipient))
                else: 
                    queueEvent['event'] = ("Thank you, %s, for subscribing "
                            "to %s!!" % (user_name, channel_name))

                q_twitchbeagle.put(queueEvent)

        except Exception, e: 
            print(e)
            pass

    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("wss://pubsub-edge.twitch.tv/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
