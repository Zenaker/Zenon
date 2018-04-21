import requests

class Server(object):
    def __init__(self, token, discord = "https://discordapp.com/api/v6/"):
        self.discord = discord
        self.token = token
        
    def join_server(self, invite):
        return requests.post(self.discord + "invite/" + invite, headers={"Authorization":self.token})
        
    def leave_server(self, serverid):
        return requests.delete(self.discord + "users/@me/guilds/" + str(serverid), headers={"Authorization":self.token}).text
        
    def createServer(self, logo, name, region):
        return requests.post(self.discord + "guilds", headers={"Authorization":self.token}, data={"icon":logo, "name":name, "region":region}).text
        
    def kick(self, chatid, userid, reason):
        return requests.delete(self.discord + "guilds/" + str(chatid) + "/members/" + str(userid) + "?reason=" + reason, headers={"Authorization":self.token}).text
        
    def ban(self, chatid, userid, reason):
        return requests.put(self.discord + "guilds/" + str(chatid) + "/bans/" + str(userid) + "?delete-message-days=0&reason=" + reason, headers={"Authorization":self.token}).text
        
    
        