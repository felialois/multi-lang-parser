from .tokenizer import Tokenizer
from .languages import Languages
import gc

SIMULTANEOUS_TOKENIZERS = 3


class TokenizerEngine:

    tokenizers = {}

    def tokenize(self, request):
        text = request.json.get('text', '')
        lang = request.json.get('lang', None)
        lang_in_response = False
        # If lang is missing, run the detector
        if lang is None:
            lang = self.detect_language(text)
            lang_in_response = True
        # Check if the lang is in the list of supported languages
        if lang in Languages._value2member_map_:
            lang = Languages(lang)
        # If the language is not in the list. The tokenizer doesn't run. Just return the detected language with an message.
        else:
            return {
                'lang': lang,
                'message': 'Language not supported'
            }
        tkns = self.tokenize_text(text, lang)
        response = {'tokens': tkns}
        # If the language was not given, we add the detected language to the response
        if lang_in_response:
            response.update({'lang': str(lang)})
        return response

    def detect_language(self, text: str) -> Languages:
        """
        Run the language detector spacy extension. Because the spacy extension works regardless of which model is used, it'll run on whatever model was loaded first.
        """
        # If no models are loaded load the ENGLISH one as it's fast to load and memory light.
        if len(self.tokenizers) == 0:
            self.load_tokenizer(Languages.ENGLISH)
        return self.tokenizers[list(self.tokenizers.keys())[0]].detect_language(text)

    def tokenize_text(self, text: str, lang: Languages):
        """
        Run the spacy tokenization pipeline.
        Load the corresponding model if it's not loaded.
        """
        if lang not in self.tokenizers:
            self.load_tokenizer(lang)
        return self.tokenizers[lang].tokenize(text)

    def load_tokenizer(self, lang: Languages):
        """
        Because of heroku memory issues (mostly caused by the size of the models in memory), we need to keep the number of loaded models limited.
        Once the limit is reached the current models are deleted from memory and must be loaded again.
        """
        if len(self.tokenizers) == SIMULTANEOUS_TOKENIZERS:
            # Delete the current tokenizers
            self.tokenizers = {}
            gc.collect()
        self.tokenizers[lang] = Tokenizer(lang)
        print(f'Language Tokenizer {lang} Loaded')
