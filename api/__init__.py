import os

from flask import Flask, request, jsonify

from .engine import Languages, TokenizerEngine
from .invalid_usage import InvalidUsage
from .validators import validate

port = int(os.environ.get("PORT", 5000))


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.te = TokenizerEngine()

    @app.route('/tokenize', methods=['POST'])
    def tokenize():
        """
        Run the tokenization for a given text
        """
        if request.method == 'POST':
            errors = validate(request)
            if errors is not None:
                print(errors)
                raise InvalidUsage(errors, status_code=400)
            response = app.te.tokenize(request)
            return response

    
    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        """
        Invalid usage is triggered by missing json fields or incorrect data types.
        """
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True, host = '0.0.0.0', port=port)
