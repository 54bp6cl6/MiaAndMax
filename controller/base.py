from math import fabs
from linebot.models import (
    FollowEvent, UnfollowEvent, JoinEvent, LeaveEvent, MemberJoinedEvent, MemberLeftEvent, 
    MessageEvent, PostbackEvent, AccountLinkEvent, BeaconEvent, ThingsEvent
)
from model.service.replyService import ReplyService
from view import base

class Controller:
    
    def __init__(self, replyService: ReplyService):
        self.replyService = replyService
        
    def handleEvent(self, params) -> bool:
        '''Retuen True if this controller already handled the event.'''
        print("Into: ",type(self).__name__, isinstance(params["event"], MessageEvent))
        if isinstance(params["event"], FollowEvent):
            self.handleFollowEvent(params)
        elif isinstance(params["event"], UnfollowEvent):
            self.handleUnfollowEvent(params)
        elif isinstance(params["event"], JoinEvent):
            self.handleJoinEvent(params)
        elif isinstance(params["event"], LeaveEvent):
            self.handleLeaveEvent(params)
        elif isinstance(params["event"], MemberJoinedEvent):
            self.handleMemberJoinedEvent(params)
        elif isinstance(params["event"], MemberLeftEvent):
            self.handleMemberLeftEvent(params)
        elif isinstance(params["event"], MessageEvent):
            self.handleMessageEvent(params)
        elif isinstance(params["event"], PostbackEvent):
            pass
        elif isinstance(params["event"], AccountLinkEvent):
            self.handleAccountLinkEvent(params)
        elif isinstance(params["event"], BeaconEvent):
            self.handleBeaconEvent(params)
        elif isinstance(params["event"], ThingsEvent):
            self.handleThingsEvent(params)
        else:
            return False
        return True
        
    def defaultReaction(self, params):
        pass
        
    def handleFollowEvent(self, params):
        self.defaultReaction(params)
        
    def handleUnfollowEvent(self, params):
        self.defaultReaction(params)
    
    def handleJoinEvent(self, params):
        self.defaultReaction(params)
    
    def handleLeaveEvent(self, params):
        self.defaultReaction(params)
        
    def handleMemberJoinedEvent(self, params):
        self.defaultReaction(params)
        
    def handleMemberLeftEvent(self, params):
        self.defaultReaction(params)

    def handleMessageEvent(self, params):
        self.defaultReaction(params)
        
    def handlePostbackEvent(self, params):
        self.defaultReaction(params)
        
    def handleAccountLinkEvent(self, params):
        self.defaultReaction(params)
        
    def handleBeaconEvent(self, params):
        self.defaultReaction(params)
        
    def handleThingsEvent(self, params):
        self.defaultReaction(params)