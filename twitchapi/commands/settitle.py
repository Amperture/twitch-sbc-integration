from twitchapi.krakenv5.channels import setChannelTitle, getChannelId
import ConfigParser

def react_chat_settitle(args):
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    channelName = config.get('CHAT', 'channel')
    channel = str(getChannelId(channelName))
    setChannelTitle(channel, ' '.join(args))

