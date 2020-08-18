# DailySMS

Anastasia M. B. is the inspiration for this project.

## Local setup requires you to have your own Twilio account and follow the setup steps found here:

- https://www.twilio.com/docs/sms/quickstart/python-msg-svc

### More to come...

### Add your own `src/credentials/config.py` file like so:

```
#!/usr/bin/env python

account_sid = 'someString'
auth_token = 'someString'
messaging_service_sid = 'someString'
twilio_number = '+ some number from Twilio you want to send from'
stasia_number = '+ some number starting with, must start with +1 for US numbers'

```
