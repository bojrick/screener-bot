from twilio.rest import Client

# put your twilio account SID and auth_token below.
account_sid = 'AC69a424d9b37cec23e36998ab70b3d096'
auth_token = 'b27bb96965366343043817fc7a9a5bd3'
client = Client(account_sid, auth_token)


# define a function eg. send_text
def send_text(text):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=text,
        to='whatsapp:+918000818487')

    print(message.sid)