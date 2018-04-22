import requests

class Server(object):
    def __init__(self, token, discord = "https://discordapp.com/api/v6/"):
        self.discord = discord
        self.token = token
        
    def join_server(self, invite, proxy):
        return requests.post(self.discord + "invite/" + invite, proxies=proxy, headers={"Authorization":self.token})
        
    def leave_server(self, serverid, proxy):
        return requests.delete(self.discord + "users/@me/guilds/" + str(serverid), proxies=proxy, headers={"Authorization":self.token}).text
        
    def createServer(self, logo, name, region, proxy):
        return requests.post(self.discord + "guilds", headers={"Authorization":self.token}, proxies=proxy, data={"icon":logo, "name":name, "region":region}).text
        
    def kick(self, chatid, userid, reason, proxy):
        return requests.delete(self.discord + "guilds/" + str(chatid) + "/members/" + str(userid) + "?reason=" + reason, proxies=proxy, headers={"Authorization":self.token}).text
        
    def ban(self, chatid, userid, reason, proxy):
        return requests.put(self.discord + "guilds/" + str(chatid) + "/bans/" + str(userid) + "?delete-message-days=0&reason=" + reason, proxies=proxy, headers={"Authorization":self.token}).text
        
    
        
