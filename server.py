from flask import Flask, render_template, request, jsonify
from array import *
import socket
from logic import *

app = Flask(__name__)
print("Running server....")

# route, then create function (unique only)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/logic', methods=['GET'])
def createLogic():
    grid = make2DArray()
    generateGrid(grid)
    return jsonify(grid)
# Creates the reciver API POST endpoint to recieve
@app.route('/Testing', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers


if __name__ == '__main__':
    app.run(host="127.0.0.1", port = 5000, debug= True)