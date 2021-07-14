# counts the number of words in the given sentence.
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    ''' count_words returns the number of words present in the sentence.\n
        For this function, a word is a:
        1. A number composed of one or more ASCII digits (ie "0" or "1234") OR
        2. A simple word composed of one or more ASCII letters (ie "a" or "they") OR
        3. A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
    '''
    sentence = sentence.replace(",", " ").replace("_", " ")
    words = [word.strip("':!!&@$%^&.").lower()
             for word in sentence.split() if word != '']
    return {word: words.count(word) for word in words}
