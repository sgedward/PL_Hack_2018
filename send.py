from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from controller import Controller

account_sid = 'AC64cf4f87b08ff1e6b995f4b9fd34019c'
auth_token = 'adeebe189513f615440b93a34b7f064b'
c= Controller()


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_response():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response

    number=request.form['From']
    message_body=request.form['Body']
    response=c.parser(number,message_body)
    resp = MessagingResponse()

    # Add a message
    resp.message(response)

    return str(resp)


def send(msg,number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body=msg,
                     from_='+16195865091',
                     to=number
                    )

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    #send("hello",'+18585220812')
