from flask import request

def test_text_is_correct(app):
    """
    The api should receive a json text data and a language and succesfully  tokenize it, and return a json document with the tokens
    """
    rv = app.test_client().post('/tokenize', 
        json={
            'text': "I still haven't found what i'm looking for",
            'lang': 'en'
        })
    json_data = rv.get_json()
    tokens = json_data['tokens']
    assert tokens == ['I', 'still', 'have', 'not', 'found', 'what', 'i', 'am', 'looking', 'for']
    
def test_lang_is_missing(app):
    """
    The api should receive a json with only the text data and succesfully identify the language, tokenize it, and return both in a json document
    """
    rv = app.test_client().post('/tokenize', 
        json={
            'text': "I still haven't found what i'm looking for",
        })
    json_data = rv.get_json()
    tokens = json_data['tokens']
    lang = json_data['lang']
    assert tokens == ['I', 'still', 'have', 'not', 'found', 'what', 'i', 'am', 'looking', 'for']
    assert lang == 'en'

def test_text_is_missing(app):
    """
    The api should receive an incorrect json and return a 400 error code
    """
    rv = app.test_client().post('/tokenize', json={})
    assert rv.status_code == 400

    rv = app.test_client().post('/tokenize', json={'txt':'This is the text.'})
    assert rv.status_code == 400


def test_lang_is_not_supported(app):
    """
    The api should receive an unknown language and return the corresponding error message
    """
    rv = app.test_client().post('/tokenize', json={
        'text':'这是中文'})
    json_data = rv.get_json()
    msg = json_data['message']
    assert msg == 'Language not supported'