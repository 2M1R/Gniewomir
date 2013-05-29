import os

def have_access(nickname):
    with open(".accesslist", 'r') as accessfile:
        accesslist = list(accessfile)
        
        for n in accesslist:
            if nickname == n.strip():
                return True
        return False