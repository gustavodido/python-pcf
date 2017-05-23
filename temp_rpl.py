from flask import Flask
from flask import jsonify

import os

app = Flask(__name__)

port = int(os.getenv("PORT", 8099))

@app.route('/api/rpl/checkrplstatus')
def checkrplstatus():
    return jsonify({"MAINTAINED_IN_RPL":"N"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)