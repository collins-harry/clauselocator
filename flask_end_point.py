from flask import Flask, request, jsonify
from clauselocator import locate_clause
from timer import timer
import IPython



app = Flask(__name__)


@app.route('/resource', methods=['GET'])
def resource():
    return handle_request()

@timer
def handle_request():
    if request.method == 'GET':
        # handle GET request
        text = request.args.get('text')
        clause = request.args.get('sentence')
        # print(text)
        # print(clause)
        indicies = locate_clause(text, clause)
        # IPython.embed()
        return jsonify(indicies), 200


if __name__ == '__main__':
    app.run()
