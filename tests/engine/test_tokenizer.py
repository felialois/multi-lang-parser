from api.engine import Tokenizer, Languages

def test_english_tokenization():
    """
    The tokenizer should identify all the tokens correctly in this english sentence
    """
    text = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness.'
    tknzr = Tokenizer(Languages.ENGLISH)
    tokens = tknzr.tokenize(text)
    correct_tokens = ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']
    assert tokens == correct_tokens

def test_english_contractions():
    """
    The tokenizer should change the english contractions with an apostrophe to their base words.
    """
    tknzr = Tokenizer(Languages.ENGLISH)
    text = "Don't doesn't didn't can't couldn't I've haven't hasn't hadn't"
    tokens = tknzr.tokenize(text)
    correct_tokens = ['Do', 'not', 'does', 'not', 'did', 'not', 'can', 'not', 'could', 'not', 'I', 'have', 'have', 'not', 'has', 'not', 'had', 'not']
    assert tokens == correct_tokens 
    
    text = "I'll he'll she'll it'll won't wouldn't I'm"
    tokens = tknzr.tokenize(text)
    correct_tokens = ['I', 'will', 'he', 'will', 'she', 'will', 'it', 'will', 'will', 'not', 'would', 'not', 'I', 'am']
    assert tokens == correct_tokens

def test_spanish_tokenization():
    """
    The tokenizer should identify all the tokens correctly in a spanish text
    """
    tknzr = Tokenizer(Languages.SPANISH)
    text = "Era el mejor de los tiempos, era el peor de los tiempos, la edad de la sabiduría, y también de la locura"
    tokens = tknzr.tokenize(text)
    correct_tokens = ['Era', 'el', 'mejor', 'de', 'los', 'tiempos', 'era', 'el', 'peor', 'de', 'los', 'tiempos', 'la', 'edad', 'de', 'la', 'sabiduría', 'y', 'también', 'de', 'la', 'locura']
    assert tokens == correct_tokens 

def test_portuguese_tokenization():
    """
    The tokenizer should identify all the tokens correctly in a portuguese text
    """
    tknzr = Tokenizer(Languages.PORTUGUESE)
    text = "Aquele foi o melhor dos tempos, foi o pior dos tempos"
    tokens = tknzr.tokenize(text)
    correct_tokens = ['Aquele', 'foi', 'o', 'melhor', 'dos', 'tempos', 'foi', 'o', 'pior', 'dos', 'tempos']
    assert tokens == correct_tokens
    
def test_french_tokenization():
    """
    The tokenizer should identify all the tokens correctly in a french text
    """
    tknzr = Tokenizer(Languages.FRENCH)
    text = "C'était le meilleur des temps, c'était le pire des temps"
    tokens = tknzr.tokenize(text)
    correct_tokens = ['Ce', 'était', 'le', 'meilleur', 'des', 'temps', 'ce', 'était', 'le', 'pire', 'des', 'temps']
    assert tokens == correct_tokens 

def test_french_elisions():
    """
    The tokenizer should change the french contractions with an apostrophe to their base words.
    """
    tknzr = Tokenizer(Languages.FRENCH)
    text = "L'animal c'est d'azur j'aime m'habille s'adorent"
    tokens = tknzr.tokenize(text)
    correct_tokens = ['Le', 'animal', 'ce', 'est', 'de', 'azur', 'je', 'aime', 'me', 'habille', 'se', 'adorent']
    assert tokens == correct_tokens 

