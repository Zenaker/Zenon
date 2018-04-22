# Zenon
a discord userbot framework to interact with users instead of normal bots

# Example
``` python
import zenon

token = "your-token"

def on_message():
    while True:
        chatid = "409879939400335362"
        message = client.get_message(chatid)
        if message == "!test":
            client.send_message(chatid, "sei grassa!")
        
if __name__ == '__main__':
    client = zenon.Client(token)
    client.func_loop(on_message)
```
