# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="파이썬 최종 연습!\nTwilio를 활용하여 문자메시지 보내기!\n성공!",
                     from_='+12565107501',
                     to='+821042313017'
                 )

print(message.sid)
