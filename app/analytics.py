import pandas as pd
from app.nessie import requestDepositsByAccountID, requestPurchasesByAccountID

class Account:
	def __init__(self, account_id, customer_id):
		self.account_id = account_id
		self.customer_id = customer_id

		# If nessie api has mock data
		# self.deposits = pd.read_json(requestDepositsByAccountID(self.account_id))
		# self.purchases = pd.read_json(requestPurchasesByAccountID(self.account_id))
		# self.purchases["purchase_date"] = pd.to_datetime(self.purchases["purchase_date"])
		# self.purchases = self.purchases[["purchase_date", "amount"]]

		# Local mock data. Remove after testing
		self.deposits = 9000
		self.purchases = pd.read_csv("app/static/data/mock_user.csv")
		self.purchases["Posted Date"] = pd.to_datetime(self.purchases["Posted Date"])
		self.purchases = self.purchases[["Posted Date", "Amount", "Category"]]

	def get_balance(self):
		#Uses local mock data, remove after
		return self.deposits - self.purchases["amount"].sum()
		# return self.deposits["amount"].sum() - self.purchases["amount"].sum()

	def get_monthly_spending():
		return

	def get_segmented_spending():
		return

	def predict_weekly_expense(self, weeks):
		return
