import json
import pprint
with open('examplebits.json', 'r') as f:
    bitsmessage = json.loads(json.load(f)['data']['message'])

pprint.pprint(bitsmessage)

if bitsmessage['message_type'] == 'bits_event':
    print("BITS SENT: " + str(bitsmessage['data']['bits_used']))
    print("SENT FROM: " + bitsmessage['data']['user_name'])
    print("SENT TO: " + bitsmessage['data']['channel_name'])

