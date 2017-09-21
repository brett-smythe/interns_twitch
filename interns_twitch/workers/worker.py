"""Worker for gathering twitch.tv chat data"""
from interns_twitch.utils import interns_logger

class TwitchTvChatWorker(object):
    """Worker to get TwitchTv chat data"""

    def __init__(self):
        interns_logger.info('Starting twitch chat worker')


