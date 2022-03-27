import sys
from controller.base import Controller
from controller.miaBinding import MiaBindingController
from db.firestoreService import FirestoreService
from service.replyService import ReplyService
from service.userService import UserService
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
            self.useContext,
            self.useDefaultReply,
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
            print("Into:", next.__name__, "middleware")
            next(params)

    #　========== Middlewares ==========
    def useLinebotErrorMessage(self, params):
        try:
            self.nextMiddleware(params)
        except:
            self.replyService.replyMessage(
                params["event"], base.TextMessage(str(sys.exc_info())))

    def useUserService(self, params):
        self.userService = UserService(self.dbService, self.replyService)
        self.nextMiddleware(params)

    def useMiaBinding(self, params):
        controller = MiaBindingController(self.replyService, self.userService)
        if not controller.handleEvent(params):
            self.nextMiddleware(params)
        return

    def useAuthentication(self, params):
        if self.userService.authenticate(params["event"].source.user_id):
            self.nextMiddleware(params)
        else:
            self.replyService.replyMessage(
                params["event"], base.TextMessage("本服務只對尊貴且唯一的蘇苡甄小姐開放，謝謝。"))

    def useContext(self, params):
        self.nextMiddleware(params)

    def useDefaultReply(self, params):
        self.nextMiddleware(params)
