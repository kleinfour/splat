from flask import Flask, send_from_directory, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/')
def serve_index():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html'))

@app.route('/<path:filename>.splat')
def serve_splat_file(filename):
    return send_from_directory('static/splat/', filename + '.splat')

@app.route('/<path:path>')
def catch_all(path):
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html'))

if __name__ == '__main__':
    app.run(port=8000)