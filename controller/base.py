from linebot.models import (
    FollowEvent, UnfollowEvent, JoinEvent, LeaveEvent, MemberJoinedEvent, MemberLeftEvent, 
    MessageEvent, PostbackEvent, AccountLinkEvent, BeaconEvent, ThingsEvent
)

class Controller:
    
    def __init__(self, bot):
        self.bot = bot
        
    def handleEvent(self, event):
        if isinstance(event, FollowEvent):
            self.handleFollowEvent(event)
        elif isinstance(event, UnfollowEvent):
            self.handleUnfollowEvent(event)
        elif isinstance(event, JoinEvent):
            self.handleJoinEvent(event)
        elif isinstance(event, LeaveEvent):
            self.handleLeaveEvent(event)
        elif isinstance(event, MemberJoinedEvent):
            self.handleMemberJoinedEvent(event)
        elif isinstance(event, MemberLeftEvent):
            self.handleMemberLeftEvent(event)
        elif isinstance(event, MessageEvent):
            self.handleMessageEvent(event)
        elif isinstance(event, PostbackEvent):
            self.handlePostbackEvent(event)
        elif isinstance(event, AccountLinkEvent):
            self.handleAccountLinkEvent(event)
        elif isinstance(event, BeaconEvent):
            self.handleBeaconEvent(event)
        elif isinstance(event, ThingsEvent):
            self.handleThingsEvent(event)
        
    def defaultReaction(self, event):
        pass
        
    def handleFollowEvent(self, event):
        self.defaultReaction(event)
        
    def handleUnfollowEvent(self, event):
        self.defaultReaction(event)
    
    def handleJoinEvent(self, event):
        self.defaultReaction(event)
    
    def handleLeaveEvent(self, event):
        self.defaultReaction(event)
        
    def handleMemberJoinedEvent(self, event):
        self.defaultReaction(event)
        
    def handleMemberLeftEvent(self, event):
        self.defaultReaction(event)

    def handleMessageEvent(self, event):
        self.defaultReaction(event)
        
    def handlePostbackEvent(self, event):
        self.defaultReaction(event)
        
    def handleAccountLinkEvent(self, event):
        self.defaultReaction(event)
        
    def handleBeaconEvent(self, event):
        self.defaultReaction(event)
        
    def handleThingsEvent(self, event):
        self.defaultReaction(event)