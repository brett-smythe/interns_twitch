"""Entry point for interns_twitch service"""
from interns_twitch.workers import chat_worker
from interns_twitch.utils import interns_logger
from interns_twitch.settings import chat as chat_settings

def run():
    """Entry point for interns_twitch service"""
    interns.logger.info('Starting interns_twitch service')
    # Later handle multiple channels, have the bot join all of them?
    chatWorker = chat_worker.TwitchTvChatWorker(
            chat_settings.server, chat_settings.port,
            chat_settings.channel_names[0], chat_settings.bot_name
    )
    chatWorker.start()
