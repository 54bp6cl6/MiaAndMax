MAX_ID = "U53a98b69664f53719b2029433d4c8175"

def Authenticate(user_id):
    if user_id == MAX_ID:
        return True
    
    (bound, mia_id) = getMiaId()
    if bound and user_id == mia_id:
        return True
    
    return False
        
def getMiaId():
    return (False, "")