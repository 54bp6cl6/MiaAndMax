from asyncio import events
from controller.base import Controller
from service.replyService import ReplyService
from service.userService import UserService
from view import (
    base
)
from linebot.models import (
    FollowEvent, UnfollowEvent
)

class MiaBindingController(Controller):
    def __init__(self, replyService: ReplyService, userService: UserService):
        super().__init__(replyService)
        self.userService = userService

    def handleEvent(self, params):
        mia_id = self.userService.getMiaId()
        if mia_id == None and isinstance(params["event"], FollowEvent):
            self.handleFollowEvent(params)
        elif mia_id == params["event"].source.user_id and isinstance(params["event"], UnfollowEvent):
            self.handleUnfollowEvent(params)
        else: 
            return False
        return True
        
    def handleFollowEvent(self, params):
        self.userService.setMiaId(params["event"].source.user_id)
        self.replyService.replyMessage(params["event"], base.TextMessage("Mia 帳號綁定成功"))

    def handleUnfollowEvent(self, params):
        self.userService.setMiaId(None)
        self.userService.sendMessageToMax(base.TextMessage("Mia 帳號解除綁定"))