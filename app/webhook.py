import json
import datetime
from app.analytics import Account

ACCOUNT_ID = "5a563d355eaa612c093b0b8b"
CUSTOMER_ID = "5a563d355eaa612c093b0b89"

### Main import ###
def respond(json_dict):
	"""Identifies the intent within a json as a dict and returns the corresponding action"""
	intent = get_intent(json_dict)
	timeFrame = get_timeFrame(json_dict)

	if intent == 'Default Welcome Intent':
		return welcome()
	elif intent == "Balance":
		return balance()
	elif intent == "Habits":
		return habits(timeFrame)
	elif intent == "Predictions":
		return predictions(timeFrame)
	elif intent == "Recommendations":
		return recommendations(timeFrame)

### Intents ###
def welcome():
	return make_fulfillment("Hello")


def balance():
	#Hardcoded account
	account = Account(ACCOUNT_ID, CUSTOMER_ID)
	return make_fulfillment("Your balance is $" + str(account.get_balance()))


def habits(timeFrame):
	habits = 'test works for habits'
	return make_fulfillment(habits)


def predictions(timeFrame):
	predictions = 'test works for predictions'
	return make_fulfillment(predictions)


def recommendations(timeFrame):
	recommendations = 'test works for recommendations'
	return make_fulfillment(recommendations)

### Tools ###
def make_fulfillment(text):
	"""Returns a json str containing the text for Dialogflow"""
	response_dict = {'fulfillmentText':text}
	return json.dumps(response_dict)


def get_intent(json_dict):
	return json_dict['queryResult']['intent']['displayName']


def get_timeFrame(json_dict):
	if 'startDate' in 'parameters' in 'queryResult' in json_dict and 'endDate' in 'parameters' in 'queryResult' in json_dict:
		startDate = json_dict['queryResult']['parameters']['startDate'][0:10]
		endDate = json_dict['queryResult']['parameters']['endDate'][0:10]
		realStart = datetime.datetime.strptime(startDate, '%Y-%m-%d')
		realEnd = datetime.datetime.strptime(endDate, '%Y-%m-%d')
		timeFrame = realEnd - realStart
		return int(timeFrame.days)

	return 0
