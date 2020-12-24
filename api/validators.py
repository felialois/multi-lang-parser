from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from flask import jsonify

"""
Schema to validate the inputs to the api.
"""
tokenizer_schema = {
    'type': 'object',
    'properties': {
        'text': {'type': 'string'},
        'lang': {'type': 'string'}
    },
    'required': ['text']
}


def validate(request):
    """
    Runs the flask input validation and returns a list of errors if any are found
    """
    inputs = TokenizerInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors


class TokenizerInputs(Inputs):
    json = [JsonSchema(schema=tokenizer_schema)]
