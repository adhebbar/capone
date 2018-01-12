import json
import datetime
import math

### Main import ###
def respond(json_dict, account):
	"""Identifies the intent within a json as a dict and returns the corresponding action"""
	intent = get_intent(json_dict)
	timeFrame = get_timeFrame(json_dict)

	if intent == 'Default Welcome Intent':
		return welcome(account)
	elif intent == "Balance":
		return balance(account)
	elif intent == "Habits":
		return habits(account,timeFrame)
	elif intent == "Predictions":
		return predictions(account,timeFrame)
	elif intent == "Recommendations":
		return recommendations(account,timeFrame)

### Intents ###
def welcome(account):
	return make_fulfillment("Hello")

def balance(account):
	#Hardcoded account

	return make_fulfillment("Your balance is $" + str(int(account.get_balance())))


def habits(account, timeFrame):
	habits = 'test works for habits'
	return make_fulfillment(habits)


def predictions(account, timeFrame):
	weeks, days = timeFrame
	PredictedExpense = str(int(account.predict_weekly_expense(weeks, days)))
	return make_fulfillment("Your predicted expenses are $" + PredictedExpense)

def recommendations(account, timeFrame):
	weeks, days = timeFrame
	PredictedExpense = str(int(account.predict_weekly_expense(weeks, days)))
	return make_fulfillment("Your predicted expenses are $" + PredictedExpense)

### Tools ###
def make_fulfillment(text):
	"""Returns a json str containing the text for Dialogflow"""
	response_dict = {'fulfillmentText':text}
	return json.dumps(response_dict)


def get_intent(json_dict):
	return json_dict['queryResult']['intent']['displayName']


# returns number of weeks. includes decimals in case user chooses days instead of weeks
# to predict money spent with decimals, I suggest
def get_timeFrame(json_dict):
	if get_intent(json_dict) == 'Predictions' or get_intent(json_dict) == 'Habits':
		print(json_dict)
		startDate = json_dict['queryResult']['parameters']['date-period']['startDate'][0:10]
		endDate = json_dict['queryResult']['parameters']['date-period']['endDate'][0:10]
		realStart = datetime.datetime.strptime(startDate, '%Y-%m-%d')
		realEnd = datetime.datetime.strptime(endDate, '%Y-%m-%d')
		timeFrame = realEnd - realStart
		return (int(timeFrame.days/7), timeFrame.days%7 ) # return weeks and days
	return 'lol what'


#weeks = 1.34
#roundDown = math.floor(weeks)
#remainder = weeks - roundDown
#totalMoney = 0
#for i in range(roundDown):
#	totalMoney += 1
