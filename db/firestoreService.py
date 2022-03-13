from google.cloud import firestore

class FirestoreService:
    def __init__(self):
        self.db = firestore.Client()

    def getChannelVars(self):
        '''
        Get Line Channel Access Token and Secret,
        return (access_token, secret).
        '''
        config = self.db.collection(u'linebot').document(u'config').get().to_dict()
        return (config["LINE_CHANNEL_ACCESS_TOKEN"], config["LINE_CHANNEL_SECRET"])

    def getUserId(self, username: str) -> str | None:
        users = self.db.collection(u'linebot').document(u'user').get().to_dict()
        return users[username] if username in users else None

    def setUserId(self, username: str, user_id: str):
        self.db.collection(u'linebot').document(u'user').update({
            username: user_id
        })
    
    def deleteUserId(self, username: str):
        self.db.collection(u'linebot').document(u'user').update({
            username: firestore.DELETE_FIELD
        })