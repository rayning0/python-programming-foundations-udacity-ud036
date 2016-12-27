from twilio.rest import TwilioRestClient
import secret

client = TwilioRestClient(secret.ACCOUNT_SID, secret.AUTH_TOKEN)

message = client.messages.create(
    body="Do you want pepperoni on that pizza, Raymond?",
    to=secret.PHONE_NO,
    from_=secret.TWILIO_PHONE_NO)

print(message.sid)
