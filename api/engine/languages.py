from enum import Enum
from spacy.attrs import ORTH, LEMMA, NORM, TAG

class Languages(Enum):
    __order__ = 'ENGLISH SPANISH FRENCH PORTUGUESE OTHER' 
    ENGLISH = 'en'
    SPANISH = 'es'
    FRENCH = 'fr'
    PORTUGUESE = 'pt'
    OTHER = 'other'

    def __str__(self):
        return str(self.value)
    

"""

In order to correctly tokenize certain words we need to add some exceptions.
English:
Spacy tokenizes a contraction like "don't" into tokens "do" and "'nt". 
The NORM version of the "'nt" token is usually the correct one to replace it with but there are some exceptions.

Spanish and Portuguese:
For spanish and portuguese the situation is different, as contractions are mandatory and are not separated by an apostrophe. 
Apostrophed words are not a thing in portuguese or spanish so we don't have to worry about it.

French:
In french, we need to use the lemma instead of the norm for cases like "C'" or "L'". So we need a custom function.
"""
tokenizer_exceptions = {
    Languages.ENGLISH: {
            "didn't": [
                {ORTH: "did", LEMMA: "do", NORM: 'did'},
                {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
            "can't": [
                {ORTH: "ca", LEMMA: "can", NORM: 'can'},
                {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
            "hadn't": [
                {ORTH: "had", LEMMA: "have", NORM: "had"},
                {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
            "won't": [
                {ORTH: "wo", LEMMA: "will", NORM: 'will'},
                {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
        },
    Languages.FRENCH: {
            "n'": [
                {ORTH: "ne", NORM: "ne", LEMMA: "ne"}],
            "t'": [
                {ORTH: "te", NORM: "te", LEMMA: "te"}],
        }

}

def french_fn(token):
    """
    Handles correct tokenizing of words with an apostrophe in french.
    """
    if "'" in token.text:
        if token.is_title:
            return token.lemma_.title()
        else:
            return token.lemma_
    else:
        return token.text

custom_functions = {
    Languages.FRENCH: french_fn
}
