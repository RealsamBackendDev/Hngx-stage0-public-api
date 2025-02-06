
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


EMAIL = "realsamuel114@gmail.com"
GITHUB_URL = "https://github.com/RealsamBackendDev/HNG-12-project"

@app.route('/', methods=['GET'])
def index():
    current_datetime = datetime.utcnow().isoformat() + 'Z'
    response = {
        "email": EMAIL,
        "current_datetime": current_datetime,
        "github_url": GITHUB_URL
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
