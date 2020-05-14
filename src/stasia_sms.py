# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import credentials.config as config
import random


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = config.account_sid
auth_token = config.auth_token

print(auth_token)
print(account_sid)

client = Client(account_sid, auth_token)

message_array=["Good morning beautiful, have a wonderful day!", "A nass ta see ya, SO NICE TO SEE YA. I love you baby.", 
"Good morning baby! It\'s a beautiful day to be alive! I love you sweetie", "Sometimes I wake up and think about how I'm going to make you smile that day. I hope you smile when you see this",
"I mean okay, maybe this isn't the greatest python script in the world. But how many women can say that their guy wrote a python script to say \"I love you, beautiful\" every day?",
]

the_message=message_array[random.randint(0,len(message_array)-1)]

message = client.messages \
    .create(
         body=the_message,
		     messaging_service_sid=config.messaging_service_sid,
         to='+12407557561'
     )

print(the_message + " - " + message.sid)
