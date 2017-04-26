'''
Chat commands executable by users.

Every command will have a series of 'tags'.

'limit': Cooldown limit for each command, per user, measured in seconds.

'userbadge': Restricted command to certain user groups. Unrestricted if empty,
             or non-populated.
    broadcaster
    moderator
    subscriber

'cost': The cost in a streamer's currency to execute a command. 0 means free.

'args': The number of arguments a command takes.

'return': Should always be either text, or a function that returns text.
    return tags such as '<user>' can be used, full list coming later

'log': Whether or not a command should be logged for later inspection

'''

import Adafruit_BBIO.GPIO as GPIO

import importlib

commands = {
        '!cmdlist':{
            'limit': 10,
            'return': 'command'
        }, 

        '!hello': {
            'limit': 10,
            'return': "Hello <user>!"
        },

        '!bigboss': {
            'limit': 10,
            'userbadge': 'broadcaster',
            'return': "Just remember! <user> is the boss around here!"
        },
        
        '!red': {
            'argc': 1,
            'limit': 5,
            'return': 'command'
        },

        '!green': {
            'argc': 1,
            'limit': 4,
            'return': 'command'
        },

        '!blue': {
            'argc': 1,
            'limit': 0,
            'return': 'But there is no blue light, <user>!'
        },
        '!modcheck': {
            'argc': 1,
            'userbadge': 'moderator',
            'limit': 0,
            'return': '<user> qualifies for Mod-limited commands!'
        },
        '!broadcastercheck': {
            'userbadge': 'broadcaster',
            'argc': 1,
            'limit': 0,
            'return': 'Yes, <user> is indeed the broadcaster!'
        },
        '!subcheck': {
            'userbadge': 'subscriber',
            'argc': 1,
            'limit': 0,
            'return': '<user>, you qualify for Subscriber-limited commands!'
        },

        '!xmas': {
            'argc': 0,
            'limit': 10,
            'return': 'command'
        },

        '!discord': {
                'argc': 0,
                'limit': 10,
                'return': ("<user>, you can find Amp's Discord server at: "
                    "https://discordapp.com/invite/7Z4muuK")
        }
}

'''
This function borrows heavily from aidanrwt's pass_to_function
'''
def pass_to_function(command, user):
    commandHead = command[0]
    commandList = list(command)

    # Command Message List has a nasty habit of having an empty string 
    # as final entry, best to remove that now.
    commandList.remove(commandHead)
    commandList.remove('')

    commandHead = commandHead.replace('!', '')

    module = importlib.import_module('chatbot.lib.commands.%s' % commandHead)
    function = getattr(module,commandHead)

    # If length of split command > 0, that means command has arguments
    return function(user, commandList)

for command in commands:
    commands[command]['last_used'] = 0
