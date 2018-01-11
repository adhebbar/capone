import json

### Main import ###
def respond(json_dict):
	"""Identifies the intent within a json as a dict and returns the corresponding action"""
	intent = get_intent(json_dict)

	if intent == 'Default Welcome Intent':
		return welcome()
	elif intent == "Balance":
		return balance()
	elif intent == "Habits":
		return habits()
	elif intent == "Predictions":
		return predictions()

### Intents ###
def welcome():
	return make_fulfillment("Hello")

def balance():
	balance = 1000
	return make_fulfillment("Your balance is $" + str(balance))

def habits():
	habits = 'test works for habits'
	return make_fulfillment(habits)

def predictions():
	predictions = 'test works for predictions'
	return make_fulfillment(predictions)

### Tools ###
def make_fulfillment(text):
	"""Returns a json str containing the text for Dialogflow"""
	response_dict = {'fulfillmentText':text}
	return json.dumps(response_dict)

def get_intent(json_dict):
	return json_dict['queryResult']['intent']['displayName']
