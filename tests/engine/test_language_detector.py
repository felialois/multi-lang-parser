from api.engine import Tokenizer, Languages

"""
The language detector should identify the language of the text for all the supported languages.
For other languages it should return the label OTHER
"""
def test_english_language_detector():
    text = 'This language is english.'
    ld = Tokenizer(Languages.ENGLISH)
    assert ld.detect_language(text) == 'en'

def test_spanish_language_detector():
    text = 'Este texto está en español.'
    ld = Tokenizer(Languages.ENGLISH)
    assert ld.detect_language(text) == 'es'

def test_portuguese_language_detector():
    text = 'Este texto esta em portugues.'
    ld = Tokenizer(Languages.ENGLISH)
    assert ld.detect_language(text) == 'pt'

def test_french_language_detector():
    text = 'Ce texte est en français.'
    ld = Tokenizer(Languages.ENGLISH)
    assert ld.detect_language(text) == 'fr'

def test_unknown_language_detector():
    text = 'Этот текст на русском'
    ld = Tokenizer(Languages.ENGLISH)
    assert ld.detect_language(text) == 'ru'

    text = 'Das Essen im Hotel hat ihm sehr gut geschmeckt.'
    ld = Tokenizer(Languages.ENGLISH)
    assert ld.detect_language(text) == 'de'