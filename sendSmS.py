from twilio.rest import TwilioRestClient
account_sid = "ACacc5b191edf563d53e03c61ba6976fdb" # Your Account SID from www.twilio.com/console
auth_token  = "e5bb35f70f41ed1414ff943fa59d8456"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+16476670714",    # Replace with your phone number
    from_="+13069940151") # Replace with your Twilio number

print(message.sid)