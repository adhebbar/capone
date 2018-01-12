import pandas as pd
from app.nessie import requestDepositsByAccountID, requestPurchasesByAccountID

class Account:
	def __init__(self, account_id, customer_id):
		self.account_id = account_id
		self.customer_id = customer_id
		self.deposits = pd.read_json(requestDepositsByAccountID(self.account_id))
		self.purchases = pd.read_json(requestPurchasesByAccountID(self.account_id))

	def get_balance(self):
		return self.deposits["amount"].sum() - self.purchases["amount"].sum()

	def get_monthly_spending():
		return

	def get_segmented_spending():
		return

	def predict_weekly_expense(self, weeks):
		return
