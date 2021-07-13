import string


def is_isogram(word: str) -> bool:
    word = word.lower()
    for l in string.ascii_lowercase:
        if word.count(l) > 1:
            return False
    return True
