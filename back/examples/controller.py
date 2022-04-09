from flask import request, make_response, jsonify
from flask.views import MethodView
# Import another module: from src.dirname.file import class. Example: from src.validators.user import CreateUserSchema

class ExampleController(MethodView):

    def __init__(self):
        # Do something, like initialize validator instance. Example: self.validator = CreateUserSchema()
        pass

    def post(self):
        if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "Not JSON received"
            }), 400)

        content = request.get_json()
        errors = self.validator.validate(content) # Validate data

        if errors:
            return make_response(jsonify({
                "status": 400,
                "errors": errors
            }), 400)

        # Do somethig, if all is ok:

        return make_response(jsonify({
            "status": 200,
            "response": "Ok",
        }), 200)
