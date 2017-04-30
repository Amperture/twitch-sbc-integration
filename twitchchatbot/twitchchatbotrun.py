#!/usr/bin/python

import ConfigParser
import requests
import importlib
import socket
import cPickle as pickle
import time
import os
import re
from threading import Thread

from .lib.command_headers import commands
from .lib.commands.parsing import *
from .lib.irc_basic import *

from Queue import Queue


def irc_datastream_recv(con, data, q_irc):
    while True:
        data = data+con.recv(1024)
        data_split = re.split(r'[\r\n]+', data)
        data = data_split.pop()

        for line in data_split:
            line = str.split(line)
            if len(line) >= 1:
                q_irc.put(line)
                


def twitchchatbot_handler(botQueue):
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')

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

    q_irc_retrieve = Queue()
    t_irc_retrieve = Thread( target = irc_datastream_recv, args = [con, data, 
        q_irc_retrieve])
    t_irc_retrieve.setDaemon(True)
    t_irc_retrieve.start()

    while True:
        try:
            if not botQueue.empty():
                queueCheck = botQueue.get()
                if queueCheck['eventType'] == 'twitchchatbot':
                    send_message(
                            con,
                            CHAN,
                            queueCheck['event']
                    )
                else:
                    botQueue.put(queueCheck)


            if not q_irc_retrieve.empty():
                    line = q_irc_retrieve.get()

                    # Stay connected to the server
                    if line[0] == 'PING':
                        print(line[0] +':'+ line[1])
                        send_pong(con, line[1])

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

                        command_run = check_command(
                            con, 
                            parse,
                            botQueue
                        )

                        if command_run:
                            command_success = execute_command(
                                    con,
                                    parse,
                                    botQueue
                            )
                            if command_success:
                                update_command_last_used(
                                        parse['splitcommand'][0]
                                )

        except socket.error:
            print('Socket died')

        except socket.timeout:
            print('Socket timeout')


if __name__ == "__main__":
    q = Queue()
    run(q)
