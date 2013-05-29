import os
import time

# Katalog notek
memodir = ".memos"
if not os.path.exists(memodir):
    os.mkdir(memodir)

def memo_save(nick, msg, c):
    r, memo = msg.split(None, 1)
    t = time.strftime("[%d.%m.%Y] [%H:%M]", time.gmtime())
                
    with open(memodir + '/' + r, 'at', encoding="utf-8") as memofile:
        memofile.writelines("Czas: {0}    Od: {1}    Treść notki: '{2}'".format(t, nick, memo))
    
    c.notice(nick, "Notka dodana")

def memo_read(nick, c):
    if nick in os.listdir(memodir):
        with open(memodir + '/' + nick, 'rt', encoding="utf-8") as memofile:
            c.notice(nick, "Oto lista notek adresowanych do ciebie:")
            
            for line in memofile:
                c.notice(nick, line)
                time.sleep(1)
            
        os.remove(memodir + '/' + nick)
        
    else:
        c.notice(nick, "Nie ma dla ciebie zadnych notek!")