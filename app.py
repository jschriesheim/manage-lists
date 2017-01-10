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
    listname = req.get("result").get("parameters").get("list")    
    speech = ""
    
    if intent == "CreateList":
        print ("*** about to create list ***")
        if createList(listname) == True:
            speech = "Created list " + listname
        else:
            speech = "List " + listname + " already exists"
        print ("*** attempted to creat list ***")
    elif intent == "DeleteList":
        if deleteList(listname) == True:
            speech = "List " + listname + " deleted"
        else:
            speech = "List " + listname + " not found"
    elif intent == "AddItem":
        itemname = req.get("result").get("parameters").get("item")
        if addItem(itemname, listname) == True:
            speech = itemname + " added to " + listname + " list"
        else:
            speech = 'List ' + listname + ' not found'
    elif intent == "RemoveItem":
        itemname = req.get("result").get("parameters").get("item")
        if removeItem(itemname, listname) == True:
            speech = itemname + " removed from " + listname + " list"
        else:
            speech = "Couldn't remove " + itemname + " from " + listname + " list"
    elif intent == "ReadList":
        items = readList(listname)
        if len(items) == 0:
            speech = listname + " list not found or empty"
        else:
            speech = listname + " list contains "
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
