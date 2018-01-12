from nessie import requestPurchasesByAccountID, requestDepositsByAccountID, requestPurchasesByAccountIDJSON, requestDepositsByAccountIDJSON, ACCOUNT_ID
import json

"""
Sample Purchase:
[
   {
      "description":"Subway",
      "purchase_date":"2018-01-08",
      "amount":800,
      "type":"merchant",
      "payer_id":"5a563d355eaa612c093b0b8b",
      "payee_id":"57cf75cfa73e494d8675fa28",
      "status":"executed",
      "medium":"balance",
      "_id":"5a57aad66514d52c7774a395",
      "merchant_id":"57cf75cfa73e494d8675fa28"
   }
]
"""

def convertPurchasesToJSON():
    purchases = requestPurchasesByAccountIDJSON(ACCOUNT_ID)
    data = {}
    data["entries"] = []

    for purchase in purchases:
        data["entries"].append({
            "start": purchase['purchase_date'] + "T12:00:00Z",
            "end": purchase['purchase_date'] + "T13:00:00Z",
            "title": purchase['description'],
            "color": "#316509",
            "content": "Amount: {0} Status: {1} Medium: {2}".format(purchase["amount"], purchase["status"], purchase["medium"])
        })

    with open('entries.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':
    convertPurchasesToJSON()
