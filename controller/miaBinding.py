from controller.base import Controller
from view import (
    base
)

class MiaBindingController(Controller):
    def __init__(self, bot):
        super().__init__(bot)
        
    def defaultReaction(self, event):
        self.bot.reply_message(event.reply_token, base.TextMessage("Mia 尚未綁定帳號。"))