from chatbot.lib.command_headers import commands
from chatbot.lib.irc_basic import *
import time


def get_valid_command(command):
    if command[0] in commands:
        return True

def get_command_cooldown(command):
    try:
        return commands[command]['limit']
    except:
        return

def get_command_userbadge(command):
    if commands[command]['userbadge']:
        return commands[command]['userbadge']

def get_command_cost(command):
    if commands[command]['cost']:
        return commands[command]['cost']

def get_command_last_used(command):
    return commands[command]['last_used']

def check_command_is_function(command):
    if commands[command]['return'] == "command":
        return True

def get_command_arg_length(command):
    try:
        return commands[command]['argc']
    except KeyError:
        return 0


def update_command_last_used(command):
    try: 
        #print("Updating command, last used: ",time.time())
        commands[command]['last_used'] = time.time()
        return True
    except:
        print("Something went wrong!")
        return False

def check_command_cooled_down(command):
    cooldown = get_command_cooldown(command)
    if not cooldown:
        #print("Command has no cooldown, executing!")
        return True
    last_used = get_command_last_used(command)
    now = time.time()
    #print("Command was last used: ", last_used)
    #print("Command has cooldown of: ", cooldown)
    #print("Time until cooled down: ", (now - last_used))
    if (time.time() - last_used >= cooldown):
        return True
    else:
        return False


'''
User badges that are relevant to the bot are:
    broadcaster
    moderator
    subscriber
'''
def check_valid_userbadge(command, userBadges):
    # If there's no 'userbadge' in the command listing, no badges
    # are required.
    try:
        badgeRequired = commands[command]['userbadge']
        print(badgeRequired)
    except KeyError:
        return True

    if badgeRequired == "broadcaster":
        if "broadcaster" in userBadges:
            return True
        else:
            return False

    if badgeRequired == "moderator":
        if ("broadcaster" or "moderator") in userBadges:
            return True
        else:
            return False

    if badgeRequired == "subscriber":
        if ("broadcaster" or "moderator" or "subscriber") in userBadges:
            return True
        else:
            return False


'''
Check all parameters for valid command usage:
    -- Is the command a function?
        -- If so, does the command have appropriate arguments?
    -- Does the user have enough currency? 
    -- Is the command a simple text return, or does it require code?
'''
#TODO: IMPLEMENT CURRENCY SYSTEM
def check_command(con, msgDict, botQueue):
    commandHead = msgDict['splitcommand'][0]

    #Check if chat message is a command
    commandValid = get_valid_command(msgDict['splitcommand'])
    if not commandValid:
        return

    #Check commands cooldown
    commandCooldown = check_command_cooled_down(commandHead)
    if not commandCooldown:
        '''
        send_message(
            con, 
            msgDict['channel'], 
            "%s command is currently on cooldown. Please try again later!" 
            % msgDict['splitcommand'][0]
        )
        '''
        return

    #Check if the user has access rights to the command
    commandBadgeAccess = check_valid_userbadge(
            commandHead,
            msgDict['badges']
    )
    if not commandBadgeAccess:
        '''
        send_message(
            con, 
            msgDict['channel'], 
            "Sorry, you do not have access rights to the %s command." 
            % msgDict['splitcommand'][0]
        )
        '''
        return

    return True


def execute_command(con, msgDict, botQueue):
    commandHead = msgDict['splitcommand'][0]
    if check_command_is_function(commandHead): 

        from chatbot.lib.command_headers import pass_to_function
        commandReturn = pass_to_function(
            msgDict['splitcommand'], 
            msgDict['display-name'],
        )

        msg = commandReturn.pop('msg', None) 
        botQueue.put(commandReturn) 

        if msg: 
            send_message(
                    con,
                    msgDict['channel'],
                    msg
            )

    else:
        returnText = commands[commandHead]['return'].replace(
                "<user>",
                msgDict['display-name']
        )
        send_message(
                con, 
                msgDict['channel'], 
                returnText
        )
    return True
