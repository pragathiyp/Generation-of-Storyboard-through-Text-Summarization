from flask import Flask, render_template, request, jsonify
import requests
from flask import jsonify
from aiohttp import ClientSession
import json
import asyncio
app = Flask(__name__)

# Render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the file and text from the form
    file = request.files['file']
    text = request.form['text']

    # Send a POST request to the API
    api_url = 'http://1ed8-34-23-193-123.ngrok-free.app'
    files = {'file': (file.filename, file.read())}
    data = {'text': text}
    response = requests.post(api_url, files=files, data=data)

    # Return the response from the API
    return jsonify(response.json())


@app.route('/get')
async def gets():
    async with ClientSession() as session:
        api_url = 'http://localhost:8000/get'
        async with session.get(api_url, timeout=900000000) as response:
            response_json = await response.json()

    return json.dumps(response_json)

@app.route('/generate')
async def generate():
    async with ClientSession() as session:
        api_url = 'http://localhost:7000/generate'
        async with session.get(api_url, timeout=900000000) as response:
            response_json = await response.json()

    return response_json;



if __name__ == '__main__':
    app.run(debug=True)
