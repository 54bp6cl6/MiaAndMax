import imp
from controller.auth import AuthController
from controller.miaBinding import MiaBindingController
from model import user

class Router:
    def __init__(self, bot):
        self.bot = bot
        self.middlewares = [
            self.UseMiaBinding,
            self.UseAuthentication
        ]
        
    def route(self, event):
        self.nextMiddleware(event)
        
    def nextMiddleware(self, event):
        if len(self.middlewares) > 0:
            next = self.middlewares.pop(0)
            next(event)
        return
    
    def UseMiaBinding(self, event):
        (bound, _) = user.getMiaId()
        if bound:
            self.nextMiddleware(event)
        else:
            MiaBindingController(self.bot).handleEvent(event)
    
    def UseAuthentication(self, event):
        if user.Authenticate(event.source.user_id):
            self.nextMiddleware(event)
        else:
            AuthController(self.bot).handleEvent(event)
        return