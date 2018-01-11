import json


# This is an example piece of a user profile
balance = 10000


# takes string json, returns test reponse (for right now)
def dialogflow(request):
    requestDict = json.loads(request)
    intent = requestDict['queryResult']['intent']['displayName']
    responseDict = {}
    if intent == 'TestApp3':
        responseDict['fulfillmentText'] = 'Your balance is ' + str(balance) + ' :)'
    return responseDict