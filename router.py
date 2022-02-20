from controller.auth import AuthController
from main import UseAuthentication


class Router:
    def __init__(self, bot):
        self.bot = bot
        
    def route(event):
        UseAuthentication(event)
    
    def UseAuthentication(self, event):
        AuthController(self.bot).handleMessageEvent(event)