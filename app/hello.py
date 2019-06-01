'''
Hello is a simple web api that just says "Hello, World!"
'''

import json
import random
from flask import Response
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    msg = {'msg':'Hello, World!'}
    return Response(json.dumps(msg), mimetype='application/json')

@app.route('/<name>')
def show_user_profile(name):
    msg = {'msg':'Hello, {}!'.format(name.capitalize())}
    return Response(json.dumps(msg), mimetype='application/json')

@app.route('/health')
def health_check():
    latency = random.uniform(0.1, 5.0)
    healthy = False if latency > 4.0 else True
    status = {'healthy': healthy,'latency': latency}
    msg = json.dumps(status)
    return Response(json.dumps(msg), mimetype='application/json')
