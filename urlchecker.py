from pyquery import PyQuery as pq

def checkurl_title(c, e, channel):
    try:
        for word in e.arguments[0].split():
            if 'http://' in word:
                url = pq(url=word.strip())
                title = url("title").text()
                c.privmsg(channel, "[URL Title] " + title)
    except:
            c.privmsg(channel, "[URL Title] Nie można odczytać adresu")