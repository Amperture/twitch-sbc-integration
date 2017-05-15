from twitchapi.krakenv5.channels import setChannelGame

def react_chat_setgame(args):
    #todo: grab channel id programmatically
    print "attemptting to set game"
    setChannelGame('3774415', ' '.join(args))
