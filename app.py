#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

from lists import *

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    intent = req.get("result").get("metadata").get("intentName")
    item = req.get("result").get("parameters").get("Item")
    list = req.get("result").get("parameters").get("List")
    
    print "Intent: " + intent + " Item: " + item + " List: " + list
    speech = ""
    
    if intent == "CreateList":
        if createList(list) == True:
            speech = "Created list " + list
        else:
            speech = "List " + list + " already exists"
    elif intent == "DeleteList":
        if deleteList(list) == True:
            speech = "List " + list + " deleted"
        else:
            speech = "List " + list + " not found"
    elif intent == "AddItem":
        if addItem(item, list) == True:
            speech = item + " added to " + list + " list"
        else:
            speech = 'List ' + list + ' not found'
    elif intent == "RemoveItem":
        if removeItem(item, list) == True:
            speech = item + " removed from " + list + " list"
        else:
            speech = "Couldn't remove " + item + " from " + list + " list"
    elif intent == "ReadList":
        items = readList(list)
        if items.count() == 0:
            speech = list + " list not found or empty"
        else:
            speech = list + " list contains "
            for each in items:
                speech += each
                speech += ", "

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "source": "manage-lists"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
