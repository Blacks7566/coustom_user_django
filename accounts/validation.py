import re 


def cheak_mobile(mob):
    cheak = re.fullmatch("[6-9]\d{9}",mob)

    if cheak!=None:
        return True
    else:
        return False

def cheak_email(email):

    chaek = re.fullmatch("\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",email)
    
    if chaek!= None:
        return True
    
    else:
        return False