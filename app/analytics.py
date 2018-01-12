import pandas as pd
from app.arima import predict
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
		self.deposits = 29000
		self.purchases = pd.read_csv("app/static/data/mock_user.csv")
		self.purchases["Posted Date"] = pd.to_datetime(self.purchases["Posted Date"])
		self.purchases = self.purchases[["Posted Date", "Amount", "Category"]]

	def get_balance(self):
		#Uses local mock data, remove after
		return self.deposits - self.purchases["Amount"].sum()
		# return self.deposits["amount"].sum() - self.purchases["amount"].sum()

	def get_monthly_spending(self):
		cleaned_chase = chase.iloc[:,[0,1]]
		cleaned_chase.columns = ["purchase_date", "amount"]
		monthly_purchases = cleaned_chase.resample("M", on=0).sum().reset_index()
		return monthly_purchases.to_json()

	def get_segmented_spending(self):
		purchases = self.purchases.iloc[:, [1,0,2]]
		segmented_spending = purchases.groupby("Category").resample("M", on="Posted Date").sum()
		segmented_spending["Amount"] = segmented_spending["Amount"].fillna(0)
		segmented_spending = segmented_spending.reset_index().groupby("Category").sum() / purchases["Amount"].sum()
		top_3 = segmented_spending.sort_values("Amount", ascending=False)[:3]
		top_cats = top_3.index
		top_percentage = top_3.Amount
		return top_cats, top_percentage

	def predict_weekly_expense(self, weeks, days):
		purchaseData = self.purchases[["Posted Date", "Amount"]]
		prediction = predict(purchaseData, weeks+1)
		return prediction[:-1].sum() + prediction[-1] * days / 7  
