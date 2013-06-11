import memo
import socialstuff as ss
from access import have_access

def do_cmd(c, e, channel):
    # Komendy
    nick = e.source.nick
    msg = e.arguments[0].split(None, 1)
        
    if len(msg) == 2:
        cmd, arg = msg
    else:
        cmd = msg[0]

    if '!' == cmd[0]:
        if cmd == "!kill":
            kill(c, nick)
        elif cmd == "!notka":
            memo.memo_save(nick, arg, c)
        elif cmd == "!sprawdznotki":
            memo.memo_read(nick, c)
        elif cmd == "!publikuj":
            ss.twitter_send(c, nick, arg)
        elif cmd == "!ver":
            show_version(c, channel)
        else:
            c.notice(nick, "Nieprawidłowa komenda: " + cmd)
                                                                        
                        
def show_version(c, channel):
    ver = "0.5.3"
    c.privmsg(channel, "Aktualna wersja Gniewomira to: " + ver)

def kill(c, nick):    
    if have_access(nick) is True:
        c.disconnect()
    else:
        c.notice(nick, "Brak uprawnień do komendy")
