import sys

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

from urlchecker import checkurl_title
from cmds import do_cmd

class TcxBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    # Przesłananie metod klasy SingleServerIRCBot
    def start(self):
        self._connect()
        super(irc.bot.SingleServerIRCBot, self).start()
        
    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        do_cmd(c, e, self.channel)

    def on_pubmsg(self, c, e):
        checkurl_title(c, e, self.channel)
        do_cmd(c, e, self.channel)

    # Odpowiedz bota na zapytanie CTCP Version
    def get_version(self):
        return "Telecomix Poland Press Agency Bot (Gniewomir)"


def main():
    server = 'chat.freenode.net'
    port = 6667
    channel = '#tcxpl-bureau'
    nickname = 'Gniewomir'

    bot = TcxBot(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()


