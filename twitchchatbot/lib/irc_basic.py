def parse_line(line):
    parsed = {}
    parsed['sender'] = get_sender(line[1])
    parsed['channel'] = line[3]
    parsed['message'] = get_message(line)
    parsed['splitcommand'] = str.split(get_message(line), ' ')

    tagList = str.split(line[0], ';')
    for tag in tagList:
        splitTag = str.split(tag,'=')
        parsed[splitTag[0].replace('@','')] = splitTag[1]

    badgeList = str.split(parsed['badges'],',')
    parsed['badges'] = {}
    for badge in badgeList:
        splitBadge = str.split(badge, '/')
        if splitBadge[0]: 
            parsed['badges'][splitBadge[0]] = splitBadge[1]

    '''
    emoteList = str.split(parsed['emotes'],',')
    parsed['emotes'] = {}
    for emote in emoteList:
        splitEmote = str.split(emote, ':')
        if splitEmote[0]: 
            print splitEmote
            parsed['emotes'][splitEmote[0]] = splitEmote[1]
    '''
    return parsed

def get_sender(msg):
    result = ''
    for char in msg:
        if char == '!':
            break
        if char != ':':
            result += char
    return result

def get_message(msg):
    result = ''
    i = 4
    length = len(msg)
    while i < length:
        result += msg[i] + ' '
        i += 1
    result = result.lstrip(':')
    return result

# Generic IRC Commands
def send_pong(con, msg):
    con.send('PONG %s\r\n' % msg)


def send_message(con, chan, msg):
    con.send('PRIVMSG %s :%s\r\n' % (chan, msg))
    print("BOT: " + msg)

def send_whisper(con, user, msg):
    con.send('PRIVMSG #jtv :/w %s %s\r\n' % (user, msg))
    print("BOT: /w %s %s" %(user, msg))


def send_nick(con, nick):
    con.send('NICK %s\r\n' % nick)


def send_pass(con, password):
    con.send('PASS %s\r\n' % password)


def join_channel(con, chan):
    con.send('JOIN %s\r\n' % chan)


def part_channel(con, chan):
    con.send('PART %s\r\n' % chan)
