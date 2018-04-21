import requests
import threading #just in case
from messages.messages import Messages
from actions.reactions import Reaction
from actions.server import Server

class Client(object):
    def __init__(self, token, discord = "https://discordapp.com/api/v6/"):
        self.token = token
        self.discord = discord
    
    def send_message(self, chatid, content):
        """
        sends a message to a specific channel or
        a person
        """
        return Messages(self.token).send_message(chatid, content)
        
    def typing_action(self, chatid):
        """
        sends the typing message to the specific channel
        """
        return Messages(self.token).typing_action(chatid)
        
    def pinMessage(self, chatid, msgid):
        """
        pins a the specific message id to the specifc
        channel
        """
        return Messages(self.token).pinMessage(chatid, msgid)
        
    def deleteMessage(self, chatid, messageid):
        """
        deletes the message from the specific channel
        """
        return Messages(self.token).deleteMessage(chatid, messageid)
        
    def editMessage(self, chatid, messsageid, text):
        """
        it edits the message from the specific channel id
        """
        return Messages(self.token).editMessage(chatid, messageid, text)
        
    def sendFile(self, chatid, file, content):
        """
        sends a file to the specific channel
        """
        return Messages(self.token).sendFile(chatid, file, content)
        
    def get_message(self, chatid):
        """
        gets the last message that has been sent from the specific channel
        """
        return Messages(self.token).get_message(chatid)
        
    def get_author(self, chatid):
        """
        gets the last message author from the specific channel
        """
        return Messages(self.token).get_author(chatid)
        
    def join_server(self, invite):
        """
        it joins the server from the specific invite parameter that the
        user has entered
        """
        return Server(self.token).join_server(invite)
        
    def leave_server(self, serverid):
        """
        the userbot will leave the specific server
        """
        return Server(self.token).leave_server(serverid)
        
    def createServer(self, logo, name, region):
        """
        it creates a server with the spefic logo, name, and region
        """
        return Server(self.token).createServer(logo, name, region)
        
    def kick(self, chatid, userid, reason):
        """
        the userbot will kick the specific user from the server
        """
        return Server(self.token).kick(chatid, userid, reason)
        
    def ban(self, chatid, userid, reason):
        """
        the userbot will ban the user from the server
        """
        return Server(self.token).ban(chatid, userid, reason)
        
    def addReaction(self, chatid, msgid, reactionid):
        """
        the userbot will add the specific reaction id to the message
        """
        return Reaction(self.token).addReaction(chatid, msgid, reactionid)
        
    def removeReaction(self, chatid, msgid, reactionid):
        """
        it removes the reaction id from the specific message
        """
        return Reaction(self.token).removeReaction(chatid, msgid, reactionid)
        
    def sendFriendRequest(self, username, discriminator):
        """
        it sends a friend request to the user mentioned
        """
        return requests.post(self.discord + "users/@me/relationships", headers={"Authorization":self.token, "Content-Type":"application/json"}, data={"username":username, "discriminator":discriminator}).text
        
    def func_loop(self, func):
        self.thread = threading.Thread(target=func)
        return self.thread.start()