from flask import render_template, request
from app import app
from app.webhook import respond

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dialogflow', methods=['POST'])
def dialogflow_webhook():
	json_dict = request.get_json()
	return respond(json_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
