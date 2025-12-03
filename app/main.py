#!/usr/bin/env python3
from flask import Flask, jsonify
import os


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
'message': os.getenv('WELCOME_MESSAGE', 'Hello from Distroless & Normal Python app!')
})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))