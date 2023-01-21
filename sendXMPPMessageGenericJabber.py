#pip install xmpppy
import xmpp

username = 'user'
passwd = 'password'
to='anotheruser@jabber.org'
msg='Test Message'


client = xmpp.Client('jabber.tld')
client.connect(server=('jabber.tld,5222))
client.auth(username, passwd, 'mybot')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)
