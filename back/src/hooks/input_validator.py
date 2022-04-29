from flask import request, make_response, jsonify
from functools import wraps

def json_input(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "Send a json format."
            }), 400)
        return func(*args, **kwargs)
    return wrapped
