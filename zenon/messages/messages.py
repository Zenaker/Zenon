import requests

class Messages(object):
    def __init__(self, token, Discord = "https://discordapp.com/api/v6/"):
        self.token = token
        self.discord = Discord
        
    def send_message(self, chatid, content): # it can also be use as a private message
        return requests.post(self.discord + "channels/" + str(chatid) + "/messages#", data={"content":str(content), "nonce":str(chatid)}, headers={"Authorization":self.token}).text
        
    def typing_action(self, chatid):
        return requests.post(self.discord + "channels/" + str(chatid) + "/typing", headers={"Authorization":self.token}).text
    
    def pinMessage(self, chatid, msgid):
        return requests.post(self.discord + "channels/" + str(chatid) + "/pins/" + str(msgid), headers={"Authorization":self.token}).text
    
    def deleteMessage(self, chatid, messageid):
        return requests.delete(self.discord + "channels/" + str(chatid) + "/messages/" + str(messageid), headers={"Authorization":self.token}).text
    
    def editMessage(self, chatid, messageid, text):
        return requests.patch(self.discord + "channels/" + str(chatid) + "/messages/" + str(messageid), headers={"Authorization":self.token}, data={"content":text}).text
        
    def sendFile(self, chatid, file, content):
        return requests.post(self.discord + "channels/" + str(chatid) + "/messages", headers={"Authorization":self.token, "content":str(content)}, files={"file":open(file, 'rb')}).text
        
    def get_message(self, chatid):
        res = requests.get(self.discord + "channels/" + str(chatid) + "/messages?limit=1", headers={"Authorization":self.token}).text
        return res.split('"content": "')[1].split('"')[0]
    
    def get_author(self, chatid):
        res = requests.get(self.discord + "channels/" + str(chatid) + "/messages?limit=1", headers={"Authorization":self.token}).text
        return res.split('"username": "')[1].split('"')[0]