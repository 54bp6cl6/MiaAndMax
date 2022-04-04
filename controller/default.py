from controller.base import Controller
from service.reply import ReplyService
from service.user import UserService
from view import (
    base
)
from linebot.models import (
    FollowEvent, UnfollowEvent, TextMessage
)


class DefaultController(Controller):
    def __init__(self, replyService: ReplyService):
        super().__init__(replyService)

    def handleMessageEvent(self, params):
        event = params["event"]
        if isinstance(event.message, TextMessage):
            if event.message.text == "寶欸我愛尼!!!":

        else:
            pass
