from twitchapi.krakenv5.channels import setChannelTitle
def react_chat_settitle(args):
    #todo: grab channel id programmatically
    print "attemptting to set title"
    setChannelTitle('3774415', ' '.join(args))

