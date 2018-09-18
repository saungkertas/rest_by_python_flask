import json

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/postjson', methods=['POST', 'GET'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return str(json.dumps(content))


app.run(host='0.0.0.0', port=14022)
