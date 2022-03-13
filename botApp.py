from db.firestoreService import FirestoreService
from router import Router
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import InvalidSignatureError

class LineBotApp:
    def __init__(self):
        self.dbService = FirestoreService()
        
        (access_token, secret) = self.dbService.getChannelVars()
        if secret is None: raise KeyError("LINE_CHANNEL_SECRET")
        if access_token is None: raise KeyError('LINE_CHANNEL_ACCESS_TOKEN')
        self.bot = LineBotApi(access_token)
        self.parser = WebhookParser(secret)

    def serve(self, request):
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        try:
            events = self.parser.parse(body, signature)
        except InvalidSignatureError:
            return 'ERROR'

        router = Router(self.bot, self.dbService)
        for event in events:
            router.route(event)
        