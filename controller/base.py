class Controller:
    
    def __init__(self, bot):
        self.bot = bot
        
    def defaultReaction(self, event):
        pass
        
    def handleFollowEvent(self, event):
        self.defaultReaction(event)
    
    def handleMessageEvent(self, event):
        self.defaultReaction(event)