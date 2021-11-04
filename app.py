from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
      'greeting': 'Hello World!'
    })

if __name__ == '__main__':
    port = os.environ.get("PORT")
    app.run(host='0.0.0.0',port=port)
