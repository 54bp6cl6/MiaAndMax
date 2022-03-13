from linebot import LineBotApi

class ReplyService:
    def __init__(self, bot: LineBotApi):
        self.bot = bot
        self.replied = False

    def replyMessage(self, event, message):
        if not self.replied:
            self.bot.reply_message(event.reply_token, message)
            self.replied = True
        else:
             self.bot.push_message(event.source.user_id, message)

    def sendMessage(self, user_id: str, message):
        self.bot.push_message(user_id, message)