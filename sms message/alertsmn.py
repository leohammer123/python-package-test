from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACef6302e2af77181d03db93758a816e54"
# Your Auth Token from twilio.com/console
auth_token  = "954e140ab41ee1c86753f00996ef9d4d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886966309501", 
    from_="+18326647285",
    body="Hello from Python!")

print(message.sid)
