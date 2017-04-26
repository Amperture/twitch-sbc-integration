"""
THIS FUNCTION WILL SERVE AS A COMMAND TEMPLATE

The function name must be the same as the command name in the command
headers list.

All functions must take two arguments, the first is the username, the second
will be a list of command arguments as a string.

The list will always have a non-zero chance of being either empty, or full.
Please account for this when writing command code.

"""

def command(user, args):
    if len(args) == 0:
        return "Command was executed without argument by %s." % user

    if args[0] == "1":
        return "Command executed by %s with argument 1" % user

    else if args[0] == "2":
        return "Command executed by %s with argument 2" % user

    else:
        return "Command Usage: \"!command 1\" or \"!command 2\"

