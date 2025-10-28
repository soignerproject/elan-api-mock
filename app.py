from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Élan API Mock!"})

@app.route('/v1/modules')
def modules():
    return jsonify({
        "modules": [
            {"name": "Process Engineering", "status": "Active"},
            {"name": "Leadership Training", "status": "In Development"},
            {"name": "Hospitality Systems", "status": "Beta"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
