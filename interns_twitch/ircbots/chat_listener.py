"""An IRC bot to just listen to IRC chat"""
import irc.bot

from interns_twitch.settings import chat

class ListenerBot(irc.bot.SingleServerIRCBot):
    """An IRC bot for only listening"""

    def __init__(self, server, port, channel, nickname):
        # Why the double nickname?
        irc.bot.SingleServerIRCBot.__init__(
                self, [(server, port)], nickname, nickname
        )

    def on_nicknameinuse(self, c, e):
        """What to do when the nickname is already in use"""
        # I'm not sure what if anything twitch does differently when a nick is
        # in use
        pass

    def on_pubmsg(self, c, e):
        # I think this is where normal chat messages will be handled
        print e.arguments[0]
        pass

    # This is how the Unity IRC client handles it's auth
    """
    output.WriteLine("PASS " + oauth);
    output.WriteLine("NICK " + nickName.ToLower());
    output.Flush();
    """
