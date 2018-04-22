import requests

class Reaction(object):
    def __init__(self, token, discord = "https://discordapp.com/api/v6/"):
        self.token = token
        self.discord = discord
    
    def addReaction(self, chatid, msgid, reactionid, proxy):
        return requests.put(self.discord  + "channels/" + str(chatid) + "/messages/" + str(msgid) + "/reactions/" + str(reactionid) + "/@me", proxies=proxy, headers={"Authorization":self.token}).text
        
    def removeReaction(self, chatid, msgid, reactionid, proxy):
        return requests.delete(self.discord + "channels/" + str(chatid) + "/messages/" + str(msgid) + "/reactions/" + str(reactionid) + "/@me", proxies=proxy, headers={"Authorization":self.token}).text
        
    
    
