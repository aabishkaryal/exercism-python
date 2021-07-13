import string


def is_pangram(sentence: str):
    s = sentence.lower()
    alphabets = list(string.ascii_lowercase)
    for a in alphabets:
        if s.count(a) == 0:
            return False
    return True
