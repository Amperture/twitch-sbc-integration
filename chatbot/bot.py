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

from lib.command_headers import commands
from lib.commands.parsing import *
from lib.irc_basic import *


Config = ConfigParser.ConfigParser()
Config.read('../config.ini')

mods = {}

# Get CHAT information
HOST = 'irc.chat.twitch.tv'                     # Twitch IRC Network
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



# Connect to the host and join the appropriate channel(s)
con = socket.socket()
con.connect((HOST, PORT))
data = ""
send_pass(con, OAUTH)
send_nick(con, NICK)
join_channel(con, CHAN)
debugtest = 0
con.send('CAP REQ :twitch.tv/commands\r\n')
con.send('CAP REQ :twitch.tv/tags\r\n')
con.send('CAP REQ :twitch.tv/membership\r\n')

while True:
    try:

        data = data+con.recv(1024)
        data_split = re.split(r'[\r\n]+', data)
        data = data_split.pop()

        for line in data_split:
            line = str.split(line)

            if len(line) >= 1:
                #print(line)

                # Stay connected to the server
                if line[0] == 'PING':
                    print(line[0] +':'+ line[1])
                    send_pong(con, line[1])

                #Add mod to dictionary
                message = ' '.join(line)

                # Find the message
                x = re.findall('^:jtv MODE (.*?) \+o (.*)$', message)
                if (len(x) > 0):
                    channel = x[0][0]
                    # If channel isn't already in list...
                    if (channel not in mods): 
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
                if (len(line) >= 3 and line[2] == 'PRIVMSG'):
                    parse = parse_line(line)
                    fileTime = time.strftime("%Y-%m-%d") + '.txt'
                    filename = os.getcwd() + '/Logs/' + fileTime
                    dir_ = os.getcwd() + '/Logs/'
                    print(time.strftime("%H:%M:%S") + ' | ' + \
                            parse['display-name'] \
                            + ' (' + parse['channel'] + ')' + ': ' \
                            + parse['message'])
                    if not (os.path.exists(dir_)):
                        os.makedirs(dir_)
                    log = open(filename,'a')
                    log.write(time.strftime("%H:%M:%S") + ' | ' \
                            + parse['display-name'] \
                            + ' (' + parse['channel'] + ')' + ': ' \
                            + parse['message'] + '\n')
                    log.close()

                    '''
                    fileTime = time.strftime("%Y-%m-%d") + 'FullLog.txt'
                    filename = os.getcwd() + '/Logs/' + fileTime
                    dir_ = os.getcwd() + '/Logs/'
                    if not (os.path.exists(dir_)):
                        os.makedirs(dir_)
                    log = open(filename,'a')
                    log.write(time.strftime("%H:%M:%S") + '\r\n')
                    log.write(''.join(line))
                    log.write('\r\n')
                    log.close()
                    '''

                    ''' Load new commands whenever somebody adds a command '''
                    if (re.search('!com add \w*', message)):
                        cmds = pickle.load(open('cmds.p', 'r+'))

                    check_command(
                        con, 
                        parse
                    )

    except socket.error:
        print('Socket died')

    except socket.timeout:
        print('Socket timeout')
