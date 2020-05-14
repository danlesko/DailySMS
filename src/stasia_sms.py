# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa5bb8153262cdeb2f8ab7f0cb1da17d8'
auth_token = '6bc0633814f18406ff86d05f39b70568'
client = Client(account_sid, auth_token)

message_array=["Good morning beautiful, have a wonderful day!", "A nass ta see ya, SO NICE TO SEE YA. I love you baby.", 
"Good morning baby! It\'s a beautiful day to be alive! I love you sweetie", "Sometimes I wake up and think about how I'm going to make you smile that day. I hope you smile when you see this",
"I mean okay, maybe this isn't the greatest python script in the world. But how many women can say that their guy wrote a python script to say \"I love you, beautiful\" every day?",
]

the_message=message_array[random.randint(0,len(message_array))]

message = client.messages \
    .create(
         body=the_message,
		     messaging_service_sid='MGf642327194a353ea756d1a67e11eac13',
         to='+13304174796'
     )

print(the_message + " - " + message.sid)