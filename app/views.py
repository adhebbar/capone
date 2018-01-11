from flask import render_template, jsonify, redirect, flash, request
from app import app
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dialogflow', methods=['POST'])
def dialogflow(request):
    requestDict = json.loads(request)



    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
