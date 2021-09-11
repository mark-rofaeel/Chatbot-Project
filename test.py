import os, sys 
from flask import Flask, request 
import json

app = Flask(__name__)

VERIFICATION_TOKEN = "hello"

@app.route('/', methods=['GET'])
def verify():

    # when the endpoint is registered as a webhook, it must echo back 
    # the 'hub.challenge' value it receives in the query arguments 
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
            #you can replace VERIFICATION_TOKEN with os.environ["VERIFY_TOKEN"] 
            return "Verification token mismatch", 403 
        return request.args["hub.challenge"], 200 
    return "Hello-world", 200

@app.route('/', methods=['POST']) 
def webhook(): 
    log("I am here") 
    data = request.get_json()
    printmsg(data) 
    printmsg(request.data) 

    return "okk",200

def printmsg(msg): 
    print(msg) 
    sys.stdout.flush()

if __name__=="__main__": 
    app.run(debug=True, port=90)