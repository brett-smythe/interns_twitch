"""An IRC bot to just listen to IRC chat"""
import irc.bot

class ListenerBot(irc.bot.SingleServerIRCBot):
    """An IRC bot for only listening"""
    def __init__(self, channel, nickname, server, port):
        # Why the double nickname?
        irc.bot.SingleServerIRCBot.__init__(
                self, [(server, port)], nickname, nickname
        )
