import zenon

token = "NDA5NDIyMjMxMjY2MTMxOTY5.DVeX1g.qbeYOIqtEcxZxgY7D_zcClsAkew"

def on_message():
    while True:
        chatid = "409879939400335362"
        message = client.get_message(chatid)
        if message == "!test":
            client.send_message(chatid, "sei grassa!")
        
if __name__ == '__main__':
    client = zenon.Client(token)
    client.func_loop(on_message)