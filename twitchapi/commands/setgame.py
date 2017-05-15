from twitchapi.krakenv5.channels import setChannelGame, getChannelId
import ConfigParser

def react_chat_setgame(args):
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    channelName = config.get('CHAT', 'channel')
    channel = str(getChannelId(channelName))
    setChannelGame(channel, ' '.join(args))
