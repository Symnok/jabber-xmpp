import xmpp

username = '10000000001' #Sender
passwd = 'passwordqwerty' #password
to='1000000000002@odnoklassniki.ru' #Destonation
msg='Test Message' # message


client = xmpp.Client('xmpp.odnoklassniki.ru')
client.connect(server=('xmpp.odnoklassniki.ru',5222))
client.auth(username, passwd)
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)
