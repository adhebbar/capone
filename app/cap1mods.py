import requests
API_KEY = "0f983c8b824d8c325f6fbee1a9f63f0e"
ACCOUNT_ID = "5a563d355eaa612c093b0b8b"
CUSTOMER_ID = "5a563d355eaa612c093b0b89"

# Account #

def requestAllAccount():
    r = requests.get("http://api.reimaginebanking.com/accounts?type=Checking&key=" + API_KEY)
    return r.json()

def requestAccountByAccountID(account_id):
    r = requests.get("http://api.reimaginebanking.com/accounts/" + account_id + "?key=" + API_KEY)
    return r.json()

def requestAccountByCustomerID(customer_id):
    r = requests.get("http://api.reimaginebanking.com/customers/" + customer_id + "/accounts?key=" + API_KEY)
    return r.json()

# Bills #

def requestBillsByAccountID(account_id):
    r = requests.get("http://api.reimaginebanking.com/accounts/" + account_id + "/bills?key=" + API_KEY)
    return r.json()

def requestBillsByCustomerID(account_id):
    r = requests.get("http://api.reimaginebanking.com/accounts/" + account_id + "/bills?key=" + API_KEY)
    return r.json()

def getBillByID(bill_id):
    url = "http://api.reimaginebanking.com/bills/{0}?key={1}".format(bill_id, self.api_key)
    response = req.get(url).json()
    return response

def createBill(account_id, status, payee, nickname, payment_date, recurring_date, payment_amount):
    url = "http://api.reimaginebanking.com/accounts/{0}/bills?key={1}".format(account_id, API_KEY)
    payload = json.dumps({
        'status': status,
        'payee': payee,
        'nickname': nickname,
        'payment_date': payment_date,
        'recurring_date': recurring_date,
        'payment_amount': payment_amount
    })
    response = req.post(url, payload).json()
    return response

def deleteBill(bill_id):
     url = "http://api.reimaginebanking.com/bills/{0}?key={1}".format(bill_id, API_KEY)
     response = req.delete(url).json()
     return response

# Deposits #

def requestDepositsByAccountID(account_id):
    r = requests.get("http://api.reimaginebanking.com/accounts/" + account_id + "/deposits?key=" + API_KEY)
    return r.json()

def getDepositsByDepositID(deposit_id):
    r = requests.get("http://api.reimaginebanking.com/deposits/" + deposit_id + "?key=" + API_KEY)
    return r.json()

def createDeposit(account_id, medium, date, status, description):
    url = "http://api.reimaginebanking.com/accounts/{0}/deposits?key={1}".format(account_id, API_KEY)
    payload = json.dumps({
        "medium": medium,
        "transaction_date": date,
        "status": status,
        "description": description
    })
    response = req.post(url, payload).json()
    return response

def deleteDeposit(deposit_id):
    url = "http://api.reimaginebanking.com/deposits/{0}?key={1}".format(deposit_id, API_KEY)
    response = req.delete(url).json()
    return response

# Purchases #

def requestPurchasesByAccountID(account_id):
    r = requests.get("http://api.reimaginebanking.com/accounts/" + account_id + "/purchases?key=" + API_KEY)
    return r.json()

def requestPurchasesByAccountAndMerchantID(account_id, merchant_id):
    r = requests.get("http://api.reimaginebanking.com/merchants/" + merchant_id + "/accounts/" + account_id + "/purchases?key=" + API_KEY)
    return r.json()

def requestPurchasesByMerchantID(merchant_id):
    r = requests.get("http://api.reimaginebanking.com/merchant/" + merchant_id + "/purchases?key=" + API_KEY)
    return r.json()

def getPurchasesByPurchaseID(purchase_id):
    r = requests.get("http://api.reimaginebanking.com/purchases/" + purchase_id + "?key=" + API_KEY)
    return r.json()

def createPurchase(account_id, merchant_id, medium, purchase_date, amount, status, description):
    url = "http://api.reimaginebanking.com/accounts/{0}/purchases?key={1}".format(account_id, API_KEY)
    payload = json.dumps({
        "merchant_id": merchant_id,
        "medium": medium,
        "purchase_date": purchase_date,
        "amount": amount,
        "status": status,
        "description": description
    })
    response = req.post(url, payload).json()
    return response

def deletePurchase(purchase_id):
    url = "http://api.reimaginebanking.com/purchases/{0}?key={1}".format(purchase_id, API_KEY)
    response = req.delete(url).json()
    return response

if __name__ == '__main__':
    # Test Get Requests
    print(requestAccountByAccountID(ACCOUNT_ID))
    print(requestAccountByCustomerID(CUSTOMER_ID))
    print(requestBillsByAccountID(ACCOUNT_ID))
    print(requestDepositsByAccountID(ACCOUNT_ID))
