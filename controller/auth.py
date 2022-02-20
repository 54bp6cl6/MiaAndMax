from base import Controller
from view import (
    base, auth
)

class AuthController(Controller):
    def __init__(self, bot):
        super().__init__(bot)
        
    def defaultReaction(self, event):
        self.bot.reply_message(event.reply_token, auth.refuseToServe())