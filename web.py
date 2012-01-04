from flask import Flask, request
from imo import Endpoint, Portal
app = Flask(__name__)

def get_args(request_args, required, optional):
    args = {}
    for arg in required:
        args[arg] = request_args[arg]
    for arg in optional:
        if arg in request_args:
            args[arg] = request_args[arg]
    return args

@app.route('/search')
def search():
    return str(portal.search(**get_args(request.args, ['query', 'result_size'], ['dym_size', 'filter', 'format', 'page'])))

@app.route('/count')
def count():
    return str(portal.count(**get_args(request.args, ['query'], ['filter', 'format'])))

@app.route('/detail')
def detail():
    return str(portal.search(**get_args(request.args, ['code', 'payload'], [])))

@app.route('/cross')
def cross():
    return str(portal.cross(**get_args(request.args, ['segment_id'], ['codes_a', 'codes_b'])))

if __name__ == '__main__':
    portal = Portal(org_id='36b2cee0ad54b925', host=Endpoint.SANDBOX, port=42011)
    app.run(host='66.228.59.249', port=88, debug=True)
