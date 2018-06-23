from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from controller import Controller



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


if __name__ == "__main__":
    app.run(debug=True)
    #send("hello",'+18585220812')
