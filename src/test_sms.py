# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa5bb8153262cdeb2f8ab7f0cb1da17d8'
auth_token = '6bc0633814f18406ff86d05f39b70568'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Testing123',
		 messaging_service_sid='MGf642327194a353ea756d1a67e11eac13',
         to='+12407557561'
     )

print(message.sid)

