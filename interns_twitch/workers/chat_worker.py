"""Worker for gathering twitch.tv chat data"""
from interns_twitch.utils import interns_logger

class TwitchTvChatWorker(object):
    """Worker to get TwitchTv chat data"""

    def __init__(self, server, port, channel, nickname):
        """Worker to get TwitchTv chat data"""
        interns_logger.info('Starting twitch chat worker')
        chat_worker = ListenerBot(server, port, channel, nickname)

    def start(self):
        """Start chat reading worker"""
        chat_worker.start()
