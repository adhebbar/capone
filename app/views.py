from flask import render_template, jsonify, redirect, flash, request
from app import app
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dialogflow', methods=['POST'])
<<<<<<< HEAD
def dialogflow(request):
    requestDict = json.loads(request)



    return response
=======
def dialogflow_webhook():
	json_req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(json_req, indent=4))
	return render_template("index.html")
>>>>>>> 8b67e81b849e01759a644470d6f711b5bd068b85

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
