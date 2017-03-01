#!/usr/bin/python

import ConfigParser
import requests
import importlib
import socket
import pickle
import time
import os
import re

import Adafruit_BBIO.GPIO as GPIO


Config = ConfigParser.ConfigParser()
Config.read('../config.ini')

mods = {}

# Get CHAT information
HOST = 'irc.twitch.tv'                          # Twitch IRC Network
PORT = 6667                                     # Default IRC-Port
CHAN = Config.get('CHAT', 'channel')
NICK = Config.get('CHAT', 'user')
OAUTH = Config.get('CHAT', 'oauth')

#Show info in Term
print('Connection Information:')
print('HOST = ' + HOST)
print('PORT = ' + str(PORT))
print('CHAN = ' + CHAN)
print('\n')
print('Chat Log:')


## Main Program ##
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
    i = 3
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


def send_nick(con, nick):
    con.send('NICK %s\r\n' % nick)


def send_pass(con, password):
    con.send('PASS %s\r\n' % password)


def join_channel(con, chan):
    con.send('JOIN %s\r\n' % chan)


def part_channel(con, chan):
    con.send('PART %s\r\n' % chan)


# Connect to the host and join the appropriate channel(s)
con = socket.socket()
con.connect((HOST, PORT))
data = ""
send_pass(con, OAUTH)
send_nick(con, NICK)
join_channel(con, CHAN)
while True:
    try:
        data = data+con.recv(1024)
        data_split = re.split(r'[\r\n]+', data)
        data = data_split.pop()

        for line in data_split:
            #print(line)
            #line = str.rstrip(line)
            line = str.split(line)

            if len(line) >= 1:

                # Stay connected to the server
                if line[0] == 'PING':
                    print(line[0] +':'+ line[1])
                    send_pong(con, line[1])

                #Add mod to dictionary
                message = ' '.join(line)
                x = re.findall('^:jtv MODE (.*?) \+o (.*)$', message) # Find the message
                if (len(x) > 0):
                    channel = x[0][0]
                    if (channel not in mods): # If the channel isn't already in the list
                        mods[channel] = []
                    modList = mods.get(channel)
                    # Experimental statement below...
                    if (type(modList) != str): # Check if the list is in str mode
                        modList.append(x[0][1])

                # Remove Mod
                y = re.findall('^:jtv MODE (.*?) \-o (.*)$', message)
                if (len(y) > 0):
                    channel = y[0][0]
                    if (channel in mods):
                        if (type(mods.get(channel)) != str):
                            mods.get(channel).remove(y[0][1]) 

                # Parse PRIVMSG
                if (line[1] == 'PRIVMSG'):
                    sender = get_sender(line[0])
                    message = get_message(line)
                    channel = line[2]
                    fileTime = time.strftime("%Y-%m-%d") + '.txt'
                    filename = os.getcwd() + '/Logs/' + fileTime
                    dir_ = os.getcwd() + '/Logs/'
                    print(time.strftime("%H:%M:%S") + ' | ' + sender + ' (' + channel + ')' + ': ' + message)
                    if not (os.path.exists(dir_)):
                        os.makedirs(dir_)
                    log = open(filename,'a')
                    log.write(time.strftime("%H:%M:%S") + ' | ' + sender + ' (' + channel + ')' + ': ' + message + '\n')
                    log.close()

                    ''' Thank new/recurring subs '''
                    if (sender == "twitchnotify"):
                        command = getattr(module_name, 'TwitchNotify')
                        command.excuteCommand(con, channel, sender, message, False, False)

                    ''' Load new commands whenever somebody adds a command '''
                    if (re.search('!com add \w*', message)):
                        cmds = pickle.load(open('cmds.p', 'r+'))

    except socket.error:
        print('Socket died')

    except socket.timeout:
        print('Socket timeout')
