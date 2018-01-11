import requests
API_KEY = "0f983c8b824d8c325f6fbee1a9f63f0e"
ACCOUNT_ID = "5a563d355eaa612c093b0b8b"
CUSTOMER_ID = "5a563d355eaa612c093b0b89"

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

def requestBillsByCustomerID(account_id):
    r = requests.get("http://api.reimaginebanking.com/accounts/" + account_id + "/bills?key=" + API_KEY)

def create(self, account_id, status, payee, nickname, payment_date, recurring_date, payment_amount):
        """
        Create - Create a bill for a given account
        Params:
            account_id - Acccount to create bill for
            status (string) - Status of the bill e.g. completed, recurring, etc = ['pending', 'cancelled', 'completed', 'recurring']
            payee (string) - The entity the bill will be paid to. Example: Comcast, Washington Gas
            nickname (string) (optional) - A nickname for the bill to help you identify it
            payment_date (string, optional) - Date when bill is going to be paid or was paid. e.g. 1/30/2014
            recurring_date (integer) (optional) - Date of month bill will recur, e.g. 15th of every month
            payment_amount (double) - Bill amount
        Returns:
            response (dict) - Response from the Nessie API
        """
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

if __name__ == '__main__':
    print(requestAccountByAccountID(ACCOUNT_ID))
    print(requestAccountByCustomerID(CUSTOMER_ID))
    print(requestBillsByAccountID(ACCOUNT_ID))
