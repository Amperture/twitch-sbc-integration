import json
import ast
import pprint

def pubsubex(q_pubsubex):
    with open('pubsubex.json', 'r') as f:
        pubsubmsg = f.read()

    pubsubbits = ast.literal_eval(pubsubmsg)['data']['message']
    pubsubjson = json.loads(pubsubbits)
    pprint.pprint(pubsubjson)

    if pubsubjson['message_type'] == 'bits_event':
        print "BITS EVENT FOUND"
        bits_used = str(pubsubjson['data']['bits_used'])
        user_name = pubsubjson['data']['user_name']
        channel_name = pubsubjson['data']['channel_name']
        print(bits_used, user_name, channel_name)

        queueEvent = {}
        queueEvent['eventType'] = 'electrical'
        queueEvent['event'] = 'bits'
        q_pubsubex.put(queueEvent)

        queueEvent = {}
        queueEvent['eventType'] = 'twitchchatbot'
        queueEvent['event'] = ("Thank you, %s, for sending %s Bit(s) to %s!!"
                % (user_name, bits_used, channel_name))
        q_pubsubex.put(queueEvent)

