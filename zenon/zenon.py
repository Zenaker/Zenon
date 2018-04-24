import requests
import threading #just in case
from messages.messages import Messages
from actions.reactions import Reaction
from actions.server import Server

class Client(object):
    def __init__(self, token, discord = "https://discordapp.com/api/v6/", proxy = None):
        self.token = token
        self.discord = discord
        self.preproxy = proxy
        if self.preproxy is not None:
            self.proxy = {"http":"http://"+self.preproxy, "https":"https://"+self.preproxy, "ftp":"ftp://"+self.preproxy}
        else:
            self.proxy = ""
    
    def send_message(self, chatid, content):
        """
        sends a message to a specific channel or
        a person
        """
        return Messages(self.token).send_message(chatid, content, self.proxy)
        
    def typing_action(self, chatid):
        """
        sends the typing message to the specific channel
        """
        return Messages(self.token).typing_action(chatid, self.proxy)
        
    def pinMessage(self, chatid, msgid):
        """
        pins a the specific message id to the specifc
        channel
        """
        return Messages(self.token).pinMessage(chatid, msgid, self.proxy)
        
    def deleteMessage(self, chatid, messageid):
        """
        deletes the message from the specific channel
        """
        return Messages(self.token).deleteMessage(chatid, messageid, self.proxy)
        
    def editMessage(self, chatid, messageid, text):
        """
        it edits the message from the specific channel id
        """
        return Messages(self.token).editMessage(chatid, messageid, text, self.proxy)
        
    def sendFile(self, chatid, file, content):
        """
        sends a file to the specific channel
        """
        return Messages(self.token).sendFile(chatid, file, content, self.proxy)
        
    def get_message(self, chatid):
        """
        gets the last message that has been sent from the specific channel
        """
        return Messages(self.token).get_message(chatid, self.proxy)
        
    def get_author(self, chatid):
        """
        gets the last message author from the specific channel
        """
        return Messages(self.token).get_author(chatid, self.proxy)
        
    def join_server(self, invite):
        """
        it joins the server from the specific invite parameter that the
        user has entered
        """
        return Server(self.token).join_server(invite, self.proxy)
        
    def leave_server(self, serverid):
        """
        the userbot will leave the specific server
        """
        return Server(self.token).leave_server(serverid, self.proxy)
        
    def createServer(self, logo, name, region):
        """
        it creates a server with the spefic logo, name, and region
        """
        return Server(self.token).createServer(logo, name, region, self.proxy)
        
    def kick(self, chatid, userid, reason):
        """
        the userbot will kick the specific user from the server
        """
        return Server(self.token).kick(chatid, userid, reason, self.proxy)
        
    def ban(self, chatid, userid, reason):
        """
        the userbot will ban the user from the server
        """
        return Server(self.token).ban(chatid, userid, reason, self.proxy)
        
    def addReaction(self, chatid, msgid, reactionid):
        """
        the userbot will add the specific reaction id to the message
        """
        return Reaction(self.token).addReaction(chatid, msgid, reactionid, self.proxy)
        
    def removeReaction(self, chatid, msgid, reactionid):
        """
        it removes the reaction id from the specific message
        """
        return Reaction(self.token).removeReaction(chatid, msgid, reactionid, self.proxy)
        
    def sendFriendRequest(self, username, discriminator):
        """
        it sends a friend request to the user mentioned
        """
        return requests.post(self.discord + "users/@me/relationships", headers={"Authorization":self.token, "Content-Type":"application/json"}, proxies=self.proxy, data={"username":username, "discriminator":discriminator}).text
        
    def func_loop(self, func):
        self.thread = threading.Thread(target=func)
        return self.thread.start()
