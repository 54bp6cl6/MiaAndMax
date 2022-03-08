from controller.base import Controller
from db import config
from view import (
    base,
)

class DbTestController(Controller):
    def __init__(self, bot, db):
        super().__init__(bot)
        self.db = db
        
    def defaultReaction(self, event):
        _, secret = config.getChannelVars(self.db)
        self.bot.reply_message(event.reply_token, base.TextMessage(secret))