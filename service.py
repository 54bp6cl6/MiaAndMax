from db import config
from router import Router
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import InvalidSignatureError

class Service:
    def __init__(self):
        self.middlewares = [
            self.useFirestoreDb,
            self.useLineBotApi,
            self.useWebhookParser,
            self.useRouter,
        ]

    def nextMiddleware(self, params):
        if len(self.middlewares) > 0:
            next = self.middlewares.pop(0)
            next(params)
        return 'OK'

    def useFirestoreDb(self, params):
        params["db"] = config.getDatabase()
        self.nextMiddleware(params)

    def useLineBotApi(self, params):
        (access_token, secret) = config.getChannelVars(params["db"])
        if secret is None: raise KeyError("LINE_CHANNEL_SECRET")
        if access_token is None: raise KeyError('LINE_CHANNEL_ACCESS_TOKEN')
        params["bot"] = LineBotApi(access_token)
        params["parser"] = WebhookParser(secret)
        self.nextMiddleware(params)

    def useWebhookParser(self, params):
        signature = params["request"].headers['X-Line-Signature']
        body = params["request"].get_data(as_text=True)
        try:
            params["events"] = params["parser"].parse(body, signature)
        except InvalidSignatureError:
            return 'ERROR'
        del params["request"]
        del params["parser"]
        self.nextMiddleware(params)

    def useRouter(self, params):
        router = Router(params["bot"], params["db"])
        for event in params["events"]:
            router.route(event)
        
        self.nextMiddleware()