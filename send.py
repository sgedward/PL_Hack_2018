from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

account_sid = 'AC64cf4f87b08ff1e6b995f4b9fd34019c'
auth_token = 'adeebe189513f615440b93a34b7f064b'


def send(msg,number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body=msg,
                     from_='+16195865091',
                     to=number
                    )
