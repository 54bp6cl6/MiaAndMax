from db.firestoreService import FirestoreService
from model.service.replyService import ReplyService


MAX_ID = "U53a98b69664f53719b2029433d4c8175"
MIA_STR = "Mia"

class UserService:
    def __init__(self, dbService: FirestoreService, replyService: ReplyService):
        self.dbService = dbService
        self.replyService = replyService
            
    def getMiaId(self) -> str | None:
        return self.dbService.getUserId(MIA_STR)

    def setMiaId(self, user_id: str):
        if user_id == None:
            self.dbService.deleteUserId(MIA_STR)
        else:
            self.dbService.setUserId(MIA_STR, user_id)

    def sendMessageToMax(self, message: str):
        self.replyService.sendMessage(MAX_ID, message)

    def authenticate(self, user_id: str):
        return user_id != "" and (user_id == MAX_ID or user_id == self.getMiaId) 