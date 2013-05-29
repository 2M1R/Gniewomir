import os
import twitter

from access import have_access

def twitter_connect():
    # Informacje o kluczach aplikacji dla api twittera
    twitter_key = ''
    twitter_secret = ''
    twitter_authfile = '.twitter_authdata'
        
    if not os.path.exists(twitter_authfile):
        twitter.oauth_dance("Gniewomir - TelecomixPL News Bot", twitter_key, twitter_secret,
                            twitter_authfile)
        
    twitter_oauth_token, twitter_oauth_secret = twitter.read_token_file(twitter_authfile)

    # Łączenie z twitterem
    t = twitter.Twitter(auth=twitter.OAuth(
                    twitter_oauth_token, twitter_oauth_secret, twitter_key, twitter_secret))
    return t

def twitter_send(c, sender, msg):
    if have_access(sender) is True:
        twitt.statuses.update(status=msg)
        c.notice(sender, "Twitt o treści '{0}' został opublikowany".format(msg))
    else:
        c.notice(sender, "Nie masz uprawnień do wysyłania wiadomości")
                
twitt = twitter_connect()