from google.cloud import firestore

MIA = "Mia"
MAX = "Max"
TEST = "TEST"

def getDatabase():
    return firestore.Client()


def getChannelVars(db):
    '''
    Get Line Channel Access Token and Secret,
    return (access_token, secret).
    '''
    config = db.collection(u'linebot').document(u'config').get().to_dict()
    return (config["LINE_CHANNEL_ACCESS_TOKEN"], config["LINE_CHANNEL_SECRET"])