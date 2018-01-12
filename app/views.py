from flask import render_template, request
from app import app
from app.webhook import respond
from app.analytics import Account

ACCOUNT_ID = "5a563d355eaa612c093b0b8b"
CUSTOMER_ID = "5a563d355eaa612c093b0b89"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dialogflow', methods=['POST'])
def dialogflow_webhook():
	json_dict = request.get_json()
	account = Account(ACCOUNT_ID, CUSTOMER_ID)
	return respond(json_dict, account)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
