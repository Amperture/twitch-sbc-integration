#Exploits
Look for ways for !addcom to be exploited for fun and profit.

#Threading
* Look to grab config data inside parent thread. Feed to child threads through
    Queues.
* Covnert to master queue system instead of manually routing messages to
    threads.

#Twitch Chat Bot
* Emote parsing seems a bit more complicated. We'll need to figure that out.
    [twitchchatbot/lib/commands/parsing.py](twitchchatbot/lib/commands/parsing.py)
* Convert command storage file from Pickle to JSON for security purposes.
    * lib/commands/addcom.py

#Kraken API
* Work on setting up system to pull OAuth tokens automatically.
    * Start thinking about ways to set up client with application
        authorization url.
