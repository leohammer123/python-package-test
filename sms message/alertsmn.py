from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACef6302e2af77181d03db93758a816e54"
# Your Auth Token from twilio.com/console
auth_token  = "02706b1514f17376db723cb908bf00e0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886966309501", 
    from_="+18326647285",
    body="牙牙牙牙牙牙")

print(message.sid)
#Iw376f5JQHShLzKyWZC-j1gxCMNQyK-WNarkR89s