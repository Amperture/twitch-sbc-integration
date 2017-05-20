# -*- coding: utf-8 -*- 
import basic as endpoints
import pprint
import ConfigParser
import json
from config import EDITOR_TOKEN, CLIENT_ID

def getChannelFollowers(channel):
    endpoint_args = [
            channel,
            'follows'
            ]
    followers = endpoints.endpoint_get("channels", CLIENT_ID,
            endpoint_args=endpoint_args)

    return followers

def getChannelObject(channel):
    args = [channel]
    channel_object = endpoints.endpoint_get('channels', CLIENT_ID,
            endpoint_args = args)
    return channel_object

def getChannelOauth(channel):
    args = []

    header = {
            "Authorization" : "OAuth %s" %EDITOR_TOKEN,
            'Accept'        : 'application/vnd.twitchtv.v5+json'
            }

    channel_object = endpoints.endpoint_get('channel', CLIENT_ID,
            endpoint_args = args, header = header)
    return channel_object

def getLastSeen(channel):
    channel = getChannelObject(channel, CLIENT_ID)
    last_seen_info = {
            'name' : channel['display_name'],
            'game' : channel['game'],
            }
    return last_seen_info

def setChannelTitle(channel, title):
    args = [channel]
    header = {
            u'Accept': u'application/vnd.twitchtv.v5+json',
            u'Authorization' : u'OAuth %s' % EDITOR_TOKEN,
            u'Content-Type': u'application/json',
    }

    data = {
        u'channel' : {
            u'status' : title
        }
    }

    if len(title) < 1 or len(title) > 140:
        return "Title String is not an appropriate length"

    status = endpoints.endpoint_put('channels', CLIENT_ID,
        data=json.dumps(data), header=header, endpoint_args = args)

    return status


def setChannelGame(channel, game):
    args = [channel]
    header = {
            u'Accept': u'application/vnd.twitchtv.v5+json',
            u'Authorization' : u'OAuth %s' % EDITOR_TOKEN,
            u'Content-Type': u'application/json',
    }

    data = {
        u'channel' : {
            u'game' : game
        }

    }
    status = endpoints.endpoint_put('channels', CLIENT_ID,
        data=json.dumps(data), header=header, endpoint_args = args)

    return status

def getChannelId(channel):
    return getChannelObject(channel)['_id']

if __name__ == "__main__":
    followers = getChannelFollowers('amperture')
    for user in followers['follows']:
        print("ID: %d"% user['user']['_id'])
        print("Username: %s" %user['user']['name'])
        print("Type: %s" %user['user']['type'])
        print user['user']['display_name'].encode('utf-8')
        print "\r\n"
