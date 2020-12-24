import spacy
from spacy_langdetect import LanguageDetector

from .languages import Languages, tokenizer_exceptions, custom_functions

MIN_CONFIDENCE = 0.7
UNKNOWN = 'UNKNOWN'

models = {
        Languages.ENGLISH: 'en_core_web_sm',
        Languages.SPANISH: 'es_core_news_sm',
        Languages.FRENCH: 'fr_core_news_sm',
        Languages.PORTUGUESE: 'pt_core_news_sm',
    }

class Tokenizer:

    def load_spacy_model(self):
        """
        Load the correct model for the selected language.
        Trim the pipeline to speed up the process
        """
        return spacy.load(models[self.lang])

    def __init__(self, lang: Languages):
        self.lang = lang
        self.nlp = self.load_spacy_model()
        # Add the language detector. It'll be turned off for normal tokenizing
        self.nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)
        # Add all the custom exceptions
        exceptions = tokenizer_exceptions.get(self.lang, {})
        for term, exception in exceptions.items():
            self.nlp.tokenizer.add_special_case(term, exception)
        # Add custom function
        self.fn = custom_functions.get(self.lang, fn)

    
    def tokenize(self, text: str) -> list:
        """
        Tokenize a text, return a list of valid tokens (removing punctuation and spaces.)
        """
        with self.nlp.disable_pipes("ner", 'language_detector'):
            return [self.fn(tkn) for tkn in self.nlp(text) if self.is_valid(tkn)]

    def is_valid(self, token):
        """
        Validate if the token is a word.
        """
        return not token.is_space and not token.is_punct
    
        
    def detect_language(self, text: str) -> Languages:
        """
        Run the language detector and return the code of the text's language.
        If the confidence is too low, consider it unknown
        """
        detector_response = self.nlp(text)._.language
        lang, score = detector_response['language'], detector_response['score']
        if score > MIN_CONFIDENCE:
            return lang
        else:
            return UNKNOWN

def fn(token):
    """
    Handles correct tokenizing of words with an apostrophe
    """
    if token.is_title:
        return token.norm_.title()
    else:
        return token.norm_