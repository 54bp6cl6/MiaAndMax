import sys
from controller.base import Controller
from controller.miaBinding import MiaBindingController
from db.firestoreService import FirestoreService
from model.service.replyService import ReplyService
from model.service.userService import UserService
from view import base
from linebot import LineBotApi

class Router:
    def __init__(self, bot: LineBotApi, dbService: FirestoreService):
        self.bot = bot
        self.dbService = dbService
        self.middlewares = [
            self.useLinebotErrorMessage,
            self.useUserService,
            self.useMiaBinding,
            self.useDefautReply,
        ]
        self.replyService = ReplyService(self.bot)
        
    def route(self, event):
        params = {
            "event": event,
        }
        self.nextMiddleware(params)
        
    def nextMiddleware(self, params):
        if len(self.middlewares) > 0:
            next = self.middlewares.pop(0)
            print("Into:",next.__name__,"middleware")
            next(params)
    
    #　========== Middlewares ==========
    def useLinebotErrorMessage(self, params):
        try:
            self.nextMiddleware(params)
        except :
            self.replyService.replyMessage(params["event"], base.TextMessage(str(sys.exc_info())))

    def useUserService(self, params):
        self.userService = UserService(self.dbService, self.replyService)
        self.nextMiddleware(params)

    def useMiaBinding(self, params):
        controller = MiaBindingController(self.replyService, self.userService)
        if not controller.handleEvent(params):
            self.nextMiddleware(params)
        return

    def useDefautReply(self, params):
        controller = Controller(self.replyService)
        controller.handleEvent(params)
        return